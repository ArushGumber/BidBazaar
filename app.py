import streamlit as st
import pandas as pd
import mysql.connector
from mysql.connector import Error
import datetime
import time
import json
import random
from PIL import Image
import base64
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(
    page_title="BidBazar",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS styling
st.markdown("""
<style>
    /* Main color scheme */
    :root {
        --primary-color: #1e88e5;
        --secondary-color: #4caf50;
        --background-color: #f5f7f9;
        --card-color: white;
        --text-color: #333333;
    }
    
    /* Global styles */
    .stApp {
        background-color: var(--background-color);
        color: var(--text-color);
    }
    
    /* Header styles */
    .main-header {
        color: var(--primary-color);
        font-size: 40px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 20px;
        padding: 20px;
        border-bottom: 2px solid var(--primary-color);
    }
    
    /* Card styles */
    .card {
        background-color: var(--card-color);
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    
    /* Button styles */
    .stButton button {
        background-color: var(--primary-color);
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-weight: bold;
        border: none;
        transition: all 0.3s;
    }
    
    .stButton button:hover {
        background-color: #1565c0;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    
    /* Green button */
    .green-btn {
        background-color: var(--secondary-color) !important;
    }
    
    .green-btn:hover {
        background-color: #388e3c !important;
    }
    
    /* Section headers */
    .section-header {
        color: var(--primary-color);
        font-size: 24px;
        font-weight: bold;
        margin-top: 20px;
        margin-bottom: 10px;
        padding-bottom: 5px;
        border-bottom: 1px solid #ddd;
    }
    
    /* Dataframe styling */
    .dataframe-container {
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        padding: 10px;
        margin-bottom: 20px;
    }
    
    /* Status badges */
    .status-open {
        background-color: var(--secondary-color);
        color: white;
        padding: 3px 10px;
        border-radius: 20px;
        font-size: 14px;
    }
    
    .status-closed {
        background-color: #f44336;
        color: white;
        padding: 3px 10px;
        border-radius: 20px;
        font-size: 14px;
    }
    
    .status-pending {
        background-color: #ff9800;
        color: white;
        padding: 3px 10px;
        border-radius: 20px;
        font-size: 14px;
    }
    
    /* Form inputs */
    div[data-baseweb="input"] {
        border-radius: 5px !important;
    }
    
    /* Sidebar */
    .sidebar .sidebar-content {
        background-color: var(--primary-color);
    }
    
    /* Tab styling */
    button[data-baseweb="tab"] {
        background-color: transparent;
        color: var(--primary-color);
        border-bottom: 2px solid transparent;
        transition: all 0.3s;
    }
    
    button[data-baseweb="tab"][aria-selected="true"] {
        background-color: transparent;
        color: var(--primary-color);
        border-bottom: 2px solid var(--primary-color);
        font-weight: bold;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        margin-top: 50px;
        padding: 20px;
        border-top: 1px solid #ddd;
        color: #777;
    }
    
    /* Success message */
    .success-message {
        background-color: #dff0d8;
        color: #3c763d;
        padding: 15px;
        border-radius: 5px;
        margin-bottom: 20px;
    }
    
    /* Error message */
    .error-message {
        background-color: #f2dede;
        color: #a94442;
        padding: 15px;
        border-radius: 5px;
        margin-bottom: 20px;
    }
    
    /* Product card grid */
    .product-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
        gap: 20px;
    }
    
    .product-card {
        background-color: white;
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s;
    }
    
    .product-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
    }
    
    .product-info {
        padding: 15px;
    }
    
    .product-title {
        font-weight: bold;
        font-size: 18px;
        margin-bottom: 10px;
    }
    
    .product-price {
        font-size: 20px;
        color: var(--primary-color);
        font-weight: bold;
    }
    
    .bid-btn {
        width: 100%;
        padding: 8px;
        background-color: var(--secondary-color);
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-weight: bold;
        margin-top: 10px;
    }
</style>
""", unsafe_allow_html=True)

def create_connection():
    # Create a database connection to the MySQL database
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='BidBazar',
            user='root',
            password='awW5$metoO'
        )
        print("Successfully connected to MySQL database")
    except Error as e:
        st.error(f"Error connecting to MySQL database: {e}")
    
    return connection

def execute_query(connection, query, params=None):
    cursor = connection.cursor(dictionary=True)
    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        
        if query.strip().upper().startswith(('SELECT', 'SHOW')):
            result = cursor.fetchall()
            return result
        else:
            connection.commit()
            return cursor.lastrowid
    except Error as e:
        st.error(f"Error executing query: {e}")
        return None
    finally:
        cursor.close()

# Session state initialization
if 'user_id' not in st.session_state:
    st.session_state.user_id = None
if 'user_type' not in st.session_state:
    st.session_state.user_type = None
if 'user_name' not in st.session_state:
    st.session_state.user_name = None
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# Authentication functions
def login(email, password):
    # """Authenticate user with email and password"""
    # connection = create_connection()
    # if connection:
    #     query = "SELECT UserID, Name FROM User WHERE Email = %s AND Password = %s"
    #     result = execute_query(connection, query, (email, password))
    #     connection.close()
        
    #     if result and len(result) > 0:
    #         st.session_state.user_id = result[0]['UserID']
    #         st.session_state.user_name = result[0]['Name']
    #         st.session_state.logged_in = True
    #         return True
    #     else:
    #         return False
    # Temporary admin bypass for testing
    if email == "admin@bidbazar.com" and password == "admin123":
        st.session_state.user_id = 1
        st.session_state.user_name = "Admin User"
        st.session_state.logged_in = True
        return True
        
    # Normal database authentication continues below
    connection = create_connection()
    if connection:
        query = "SELECT UserID, Name FROM User WHERE Email = %s AND Password = %s"
        result = execute_query(connection, query, (email, password))
        connection.close()
        
        if result and len(result) > 0:
            st.session_state.user_id = result[0]['UserID']
            st.session_state.user_name = result[0]['Name']
            st.session_state.logged_in = True
            return True
        else:
            return False

def logout():
    st.session_state.user_id = None
    st.session_state.user_name = None
    st.session_state.user_type = None
    st.session_state.logged_in = False
    st.rerun()

def get_product_types():
    connection = create_connection()
    if connection:
        query = "SELECT DISTINCT ProductType FROM ProductConfiguration ORDER BY ProductType"
        result = execute_query(connection, query)
        connection.close()
        
        if result:
            product_types = [item['ProductType'] for item in result]
            return product_types
        else:
            return []

def get_products_by_type(product_type):
    connection = create_connection()
    if connection:
        query = "SELECT DISTINCT Product FROM ProductConfiguration WHERE ProductType = %s ORDER BY Product"
        result = execute_query(connection, query, (product_type,))
        connection.close()
        
        if result:
            products = [item['Product'] for item in result]
            return products
        else:
            return []

def get_available_auctions(filters=None):
    connection = create_connection()
    if connection:
        query = """
        SELECT 
            A.AuctionID, 
            A.ProductID, 
            PC.ProductType, 
            PC.Product, 
            A.AuctionStartTime, 
            A.AuctionEndTime, 
            A.AuctionStatus, 
            A.AuctionBasePrice,
            A.AuctionType,
            A.NegotiationEnabled,
            U.Name AS SellerName,
            U.UserID AS SellerID,
            (SELECT MAX(BidAmount) FROM Bid WHERE AuctionID = A.AuctionID) AS CurrentHighestBid,
            (SELECT COUNT(*) FROM Bid WHERE AuctionID = A.AuctionID) AS BidCount
        FROM Auction A
        JOIN ProductDetails PD ON A.ProductID = PD.ProductID
        JOIN ProductConfiguration PC ON PD.ConfigurationID = PC.ConfigurationID
        JOIN User U ON A.UserID = U.UserID
        WHERE A.AuctionStatus = 'Open'
        """
        
        # Add filters if provided
        params = []
        if filters:
            if 'product_type' in filters and filters['product_type']:
                query += " AND PC.ProductType = %s"
                params.append(filters['product_type'])
            
            if 'product' in filters and filters['product']:
                query += " AND PC.Product = %s"
                params.append(filters['product'])
            
            if 'price_min' in filters and filters['price_min']:
                query += " AND A.AuctionBasePrice >= %s"
                params.append(filters['price_min'])
            
            if 'price_max' in filters and filters['price_max']:
                query += " AND A.AuctionBasePrice <= %s"
                params.append(filters['price_max'])
        
        query += " ORDER BY A.AuctionEndTime ASC"
        
        if params:
            result = execute_query(connection, query, tuple(params))
        else:
            result = execute_query(connection, query)
            
        connection.close()
        return result
    return []

def get_product_attributes(product_id):
    connection = create_connection()
    if connection:
        query = """
        SELECT AttributeName, AttributeValue
        FROM ProductAttributes
        WHERE ProductID = %s
        """
        result = execute_query(connection, query, (product_id,))
        connection.close()
        
        return result
    return []

def get_user_auctions(user_id):
    connection = create_connection()
    if connection:
        query = """
        SELECT 
            A.AuctionID, 
            A.ProductID, 
            PC.ProductType, 
            PC.Product, 
            A.AuctionStartTime, 
            A.AuctionEndTime, 
            A.AuctionStatus, 
            A.AuctionBasePrice,
            (SELECT MAX(BidAmount) FROM Bid WHERE AuctionID = A.AuctionID) AS CurrentHighestBid,
            (SELECT COUNT(*) FROM Bid WHERE AuctionID = A.AuctionID) AS BidCount
        FROM Auction A
        JOIN ProductDetails PD ON A.ProductID = PD.ProductID
        JOIN ProductConfiguration PC ON PD.ConfigurationID = PC.ConfigurationID
        WHERE A.UserID = %s
        ORDER BY A.AuctionStartTime DESC
        """
        result = execute_query(connection, query, (user_id,))
        connection.close()
        
        return result
    return []

def get_user_bids(user_id):
    connection = create_connection()
    if connection:
        query = """
        SELECT 
            B.BidID, 
            B.AuctionID, 
            B.ProductID, 
            PC.ProductType, 
            PC.Product, 
            B.BidTimestamp, 
            B.BidAmount, 
            B.isWinningBid,
            A.AuctionStatus,
            A.AuctionEndTime
        FROM Bid B
        JOIN Auction A ON B.AuctionID = A.AuctionID
        JOIN ProductDetails PD ON B.ProductID = PD.ProductID
        JOIN ProductConfiguration PC ON PD.ConfigurationID = PC.ConfigurationID
        WHERE B.UserID = %s
        ORDER BY B.BidTimestamp DESC
        """
        result = execute_query(connection, query, (user_id,))
        connection.close()
        
        return result
    return []

def place_bid(auction_id, product_id, user_id, bid_amount, is_auto_bid=False, max_bid=None, step_rate=None):
    connection = create_connection()
    if connection:
        try:
            # Check if auction is still open
            query = "SELECT AuctionStatus FROM Auction WHERE AuctionID = %s"
            result = execute_query(connection, query, (auction_id,))
            
            if not result or result[0]['AuctionStatus'] != 'Open':
                connection.close()
                return {'success': False, 'message': 'This auction is no longer open for bidding.'}
            
            # Check if bid amount is greater than current highest bid
            query = "SELECT MAX(BidAmount) AS CurrentHighestBid FROM Bid WHERE AuctionID = %s"
            result = execute_query(connection, query, (auction_id,))
            current_highest_bid = result[0]['CurrentHighestBid'] if result[0]['CurrentHighestBid'] else 0
            
            if bid_amount <= current_highest_bid:
                connection.close()
                return {'success': False, 'message': f'Your bid must be greater than the current highest bid (${current_highest_bid}).'}
            
            # Get new BidID
            query = "SELECT MAX(BidID) AS MaxBidID FROM Bid"
            result = execute_query(connection, query)
            new_bid_id = (result[0]['MaxBidID'] if result[0]['MaxBidID'] else 0) + 1
            
            # Insert the bid
            query = """
            INSERT INTO Bid (BidID, AuctionID, ProductID, UserID, BidTimestamp, BidAmount, isWinningBid, isAutoBid)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            params = (new_bid_id, auction_id, product_id, user_id, datetime.datetime.now(), bid_amount, False, is_auto_bid)
            execute_query(connection, query, params)
            
            # If it's an auto bid, insert into AutoBid table
            if is_auto_bid and max_bid and step_rate:
                query = """
                INSERT INTO AutoBid (BidID, StartingBid, MaxBid, StepRate)
                VALUES (%s, %s, %s, %s)
                """
                params = (new_bid_id, bid_amount, max_bid, step_rate)
                execute_query(connection, query, params)
            
            connection.commit()
            connection.close()
            return {'success': True, 'message': f'Your bid of ${bid_amount} has been placed successfully!', 'bid_id': new_bid_id}
        
        except Error as e:
            connection.rollback()
            connection.close()
            return {'success': False, 'message': f'Error placing bid: {str(e)}'}
    
    return {'success': False, 'message': 'Could not connect to the database.'}

def create_new_auction(user_id, product_type, product_name, attributes, auction_details):
    connection = create_connection()
    if connection:
        try:
            # Start a transaction
            connection.start_transaction()
            
            # 1. Create ProductConfiguration entry
            query = "SELECT MAX(ConfigurationID) AS MaxID FROM ProductConfiguration"
            result = execute_query(connection, query)
            new_config_id = (result[0]['MaxID'] if result[0]['MaxID'] else 0) + 1
            
            query = """
            INSERT INTO ProductConfiguration (ConfigurationID, Created, ProductType, Product)
            VALUES (%s, %s, %s, %s)
            """
            params = (new_config_id, datetime.datetime.now(), product_type, product_name)
            execute_query(connection, query, params)
            
            # 2. Create ProductDetails entry
            query = "SELECT MAX(ProductID) AS MaxID FROM ProductDetails"
            result = execute_query(connection, query)
            new_product_id = (result[0]['MaxID'] if result[0]['MaxID'] else 0) + 1
            
            query = """
            INSERT INTO ProductDetails (ProductID, ConfigurationID, LatestAuctionStatus, Status)
            VALUES (%s, %s, %s, %s)
            """
            params = (new_product_id, new_config_id, 'Open', 'Available')
            execute_query(connection, query, params)
            
            # 3. Create ProductInventory entry
            query = """
            INSERT INTO ProductInventory (ProductID, PickupAddress, PickupDateTime, AmountForSeller)
            VALUES (%s, %s, %s, %s)
            """
            params = (
                new_product_id, 
                auction_details['pickup_address'], 
                auction_details['pickup_datetime'], 
                auction_details['base_price']
            )
            execute_query(connection, query, params)
            
            # 4. Add product attributes
            for key, value in attributes.items():
                if value:  # Only add non-empty attributes
                    query = """
                    INSERT INTO ProductAttributes (ProductID, AttributeName, AttributeValue)
                    VALUES (%s, %s, %s)
                    """
                    params = (new_product_id, key, value)
                    execute_query(connection, query, params)
            
            # 5. Create Auction entry
            query = "SELECT MAX(AuctionID) AS MaxID FROM Auction"
            result = execute_query(connection, query)
            new_auction_id = (result[0]['MaxID'] if result[0]['MaxID'] else 0) + 1
            
            query = """
            INSERT INTO Auction (
                AuctionID, ProductID, UserID, AuctionStartTime, AuctionEndTime, 
                AuctionStatus, AuctionType, SnippingFlag, AuctionBasePrice, NegotiationEnabled
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            params = (
                new_auction_id,
                new_product_id,
                user_id,
                auction_details['start_time'],
                auction_details['end_time'],
                'Open',
                auction_details['auction_type'],
                auction_details['snipping_flag'],
                auction_details['base_price'],
                auction_details['negotiation_enabled']
            )
            execute_query(connection, query, params)
            
            # Commit the transaction
            connection.commit()
            connection.close()
            
            return {
                'success': True, 
                'message': 'Your auction has been created successfully!',
                'auction_id': new_auction_id,
                'product_id': new_product_id
            }
            
        except Error as e:
            connection.rollback()
            connection.close()
            return {'success': False, 'message': f'Error creating auction: {str(e)}'}
    
    return {'success': False, 'message': 'Could not connect to the database.'}

def run_custom_query(query, params=None):
    connection = create_connection()
    if connection:
        try:
            result = execute_query(connection, query, params)
            connection.close()
            return {'success': True, 'result': result}
        except Error as e:
            connection.close()
            return {'success': False, 'message': f'Error executing query: {str(e)}'}
    
    return {'success': False, 'message': 'Could not connect to the database.'}

# UI Components
def show_header():
    st.markdown('<div class="main-header">BidBazar</div>', unsafe_allow_html=True)
    
    # Show login/user info in the sidebar
    with st.sidebar:
        if st.session_state.logged_in:
            st.success(f"Logged in as: {st.session_state.user_name}")
            
            # User type selector (only if logged in)
            user_type = st.radio(
                "Select your role:",
                options=["Buyer", "Seller"],
                horizontal=True,
                key="user_type_radio"
            )
            st.session_state.user_type = user_type.lower()
            
            if st.button("Logout"):
                logout()
        else:
            show_login_form()

def show_login_form():
    st.sidebar.markdown('<p class="section-header">Login</p>', unsafe_allow_html=True)
    email = st.sidebar.text_input("Email", key="login_email")
    password = st.sidebar.text_input("Password", type="password", key="login_password")
    
    # Login button
    if st.sidebar.button("Login"):
        if login(email, password):
            st.sidebar.success("Login successful!")
            # Set default user type
            st.session_state.user_type = "buyer"
            # Force a rerun to update the UI
            st.rerun()
        else:
            st.sidebar.error("Invalid email or password")
    
    # Register option
    st.sidebar.markdown("---")
    st.sidebar.markdown("Don't have an account? [Register](https://bidbazar-registration.com)")
    

def show_buyer_interface():
    st.markdown('<p class="section-header">Browse Auctions</p>', unsafe_allow_html=True)
    
    # Filters in columns
    col1, col2 = st.columns(2)
    
    with col1:
        # Product type filter
        product_types = get_product_types()
        selected_type = st.selectbox(
            "Product Type", 
            options=["All"] + product_types,
            key="filter_product_type"
        )
        
        # Product filter (based on selected type)
        if selected_type and selected_type != "All":
            products = get_products_by_type(selected_type)
            selected_product = st.selectbox(
                "Product", 
                options=["All"] + products,
                key="filter_product"
            )
        else:
            selected_product = "All"
    
    with col2:
        # Price range filter
        min_price = st.number_input("Minimum Price ($)", min_value=0, value=0, key="filter_min_price")
        max_price = st.number_input("Maximum Price ($)", min_value=0, value=10000, key="filter_max_price")
    
    # Apply filters button
    if st.button("Apply Filters"):
        # Prepare filters
        filters = {}
        if selected_type and selected_type != "All":
            filters['product_type'] = selected_type
        
        if selected_product and selected_product != "All":
            filters['product'] = selected_product
        
        if min_price > 0:
            filters['price_min'] = min_price
        
        if max_price > 0:
            filters['price_max'] = max_price
        
        # Get auctions based on filters
        auctions = get_available_auctions(filters)
        st.session_state.filtered_auctions = auctions
    
    # Display auctions
    if 'filtered_auctions' not in st.session_state:
        # Get all auctions if no filter has been applied yet
        st.session_state.filtered_auctions = get_available_auctions()
    
    # Display auctions in a grid view
    if st.session_state.filtered_auctions:
        st.markdown('<div class="product-grid">', unsafe_allow_html=True)
        
        # Use columns to create a grid
        cols = st.columns(3)
        
        for i, auction in enumerate(st.session_state.filtered_auctions):
            with cols[i % 3]:
                # Calculate time remaining
                end_time = auction['AuctionEndTime']
                time_remaining = end_time - datetime.datetime.now()
                days_remaining = time_remaining.days
                hours_remaining = time_remaining.seconds // 3600
                
                st.markdown(
                    f"""
                    <div class="product-card">
                        <div class="product-info">
                            <div class="product-title">{auction['Product']} ({auction['ProductType']})</div>
                            <p>Seller: {auction['SellerName']}</p>
                            <p>Starting Price: <span class="product-price">${auction['AuctionBasePrice']:.2f}</span></p>
                            <p>Current Highest Bid: <span class="product-price">${auction['CurrentHighestBid'] if auction['CurrentHighestBid'] else auction['AuctionBasePrice']:.2f}</span></p>
                            <p>Total Bids: {auction['BidCount']}</p>
                            <p>Time Remaining: {days_remaining} days, {hours_remaining} hours</p>
                        </div>
                    </div>
                    """, 
                    unsafe_allow_html=True
                )
                
                # Bid button (only if logged in)
                if st.session_state.logged_in:
                    if st.button(f"Bid Now", key=f"bid_btn_{auction['AuctionID']}"):
                        st.session_state.selected_auction = auction
                        st.session_state.show_bid_form = True
    else:
        st.info("No auctions found matching your criteria.")
    
    # Show bid form if an auction is selected
    if 'show_bid_form' in st.session_state and st.session_state.show_bid_form:
        show_bid_form(st.session_state.selected_auction)

def show_bid_form(auction):
    # Display the form to place a bid
    st.markdown('<p class="section-header">Place Your Bid</p>', unsafe_allow_html=True)
    
    # Display auction details
    st.markdown(
        f"""
        <div class="card">
            <h3>{auction['Product']} ({auction['ProductType']})</h3>
            <p>Current Highest Bid: <strong>${auction['CurrentHighestBid'] if auction['CurrentHighestBid'] else auction['AuctionBasePrice']:.2f}</strong></p>
            <p>Auction ends: {auction['AuctionEndTime'].strftime('%B %d, %Y at %I:%M %p')}</p>
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    # Product attributes
    attributes = get_product_attributes(auction['ProductID'])
    if attributes:
        st.markdown('<p class="section-header">Product Specifications</p>', unsafe_allow_html=True)
        
        # Display attributes in a nice format
        attr_cols = st.columns(2)
        for i, attr in enumerate(attributes):
            with attr_cols[i % 2]:
                st.write(f"**{attr['AttributeName']}:** {attr['AttributeValue']}")
    
    # Bid input
    current_highest = auction['CurrentHighestBid'] if auction['CurrentHighestBid'] else auction['AuctionBasePrice']
    min_bid = current_highest + 1  # Minimum bid is $1 more than current highest
    
    bid_amount = st.number_input(
        "Your Bid Amount ($)", 
        min_value=float(min_bid), 
        value=float(min_bid), 
        step=1.0,
        key="bid_amount"
    )
    
    # Auto-bid option
    use_auto_bid = st.checkbox("Use Auto-Bidding", key="use_auto_bid")
    
    if use_auto_bid:
        col1, col2 = st.columns(2)
        
        with col1:
            max_bid = st.number_input(
                "Maximum Bid Amount ($)", 
                min_value=float(bid_amount), 
                value=float(bid_amount * 1.2),  # Default to 20% higher
                step=1.0,
                key="max_bid"
            )
        
        with col2:
            step_rate = st.number_input(
                "Bid Increment ($)", 
                min_value=1.0, 
                value=5.0, 
                step=1.0,
                key="step_rate"
            )
        
        st.info("Auto-bidding will automatically place bids for you up to your maximum amount, increasing by your specified increment when you're outbid.")
    
    # Place bid button
    if st.button("Place Bid", key="place_bid_btn"):
        if not st.session_state.logged_in:
            st.error("Please log in to place a bid.")
        else:
            # Prevent bidding on own auctions
            if auction['SellerID'] == st.session_state.user_id:
                st.error("You cannot bid on your own auction.")
            else:
                # Place the bid
                result = place_bid(
                    auction_id=auction['AuctionID'],
                    product_id=auction['ProductID'],
                    user_id=st.session_state.user_id,
                    bid_amount=bid_amount,
                    is_auto_bid=use_auto_bid,
                    max_bid=max_bid if use_auto_bid else None,
                    step_rate=step_rate if use_auto_bid else None
                )
                
                if result['success']:
                    st.success(result['message'])
                    # Refresh auctions
                    st.session_state.filtered_auctions = get_available_auctions()
                    # Close bid form
                    st.session_state.show_bid_form = False
                    # Force a rerun to update the UI
                    time.sleep(1)
                    st.rerun()
                else:
                    st.error(result['message'])
    
    # Cancel button
    if st.button("Cancel", key="cancel_bid_btn"):
        st.session_state.show_bid_form = False
        st.rerun()

def show_seller_interface():
    # Create tabs for different seller functions
    seller_tabs = st.tabs(["My Auctions", "Create New Auction", "Sales Dashboard"])
    
    # Tab 1: My Auctions
    with seller_tabs[0]:
        st.markdown('<p class="section-header">My Active Auctions</p>', unsafe_allow_html=True)
        
        if not st.session_state.logged_in:
            st.warning("Please log in to view your auctions.")
        else:
            # Get user's auctions
            auctions = get_user_auctions(st.session_state.user_id)
            
            if not auctions:
                st.info("You haven't created any auctions yet.")
            else:
                # Convert to DataFrame for display
                auctions_df = pd.DataFrame(auctions)
                
                # Format date columns
                if 'AuctionStartTime' in auctions_df.columns:
                    auctions_df['AuctionStartTime'] = auctions_df['AuctionStartTime'].apply(
                        lambda x: x.strftime('%Y-%m-%d %H:%M') if x else '')
                
                if 'AuctionEndTime' in auctions_df.columns:
                    auctions_df['AuctionEndTime'] = auctions_df['AuctionEndTime'].apply(
                        lambda x: x.strftime('%Y-%m-%d %H:%M') if x else '')
                
                # Display active auctions
                active_auctions = auctions_df[auctions_df['AuctionStatus'] == 'Open']
                if not active_auctions.empty:
                    st.markdown('<div class="dataframe-container">', unsafe_allow_html=True)
                    st.dataframe(
                        active_auctions[['AuctionID', 'ProductType', 'Product', 'AuctionStartTime', 
                                      'AuctionEndTime', 'AuctionBasePrice', 'CurrentHighestBid', 'BidCount']],
                        use_container_width=True
                    )
                    st.markdown('</div>', unsafe_allow_html=True)
                else:
                    st.info("You don't have any active auctions.")
                
                # Display completed auctions
                st.markdown('<p class="section-header">My Completed Auctions</p>', unsafe_allow_html=True)
                completed_auctions = auctions_df[auctions_df['AuctionStatus'] == 'Completed']
                
                if not completed_auctions.empty:
                    st.markdown('<div class="dataframe-container">', unsafe_allow_html=True)
                    st.dataframe(
                        completed_auctions[['AuctionID', 'ProductType', 'Product', 'AuctionStartTime', 
                                         'AuctionEndTime', 'AuctionBasePrice', 'CurrentHighestBid', 'BidCount']],
                        use_container_width=True
                    )
                    st.markdown('</div>', unsafe_allow_html=True)
                else:
                    st.info("You don't have any completed auctions.")
    
    # Tab 2: Create New Auction
    with seller_tabs[1]:
        st.markdown('<p class="section-header">Create New Auction</p>', unsafe_allow_html=True)
        
        if not st.session_state.logged_in:
            st.warning("Please log in to create an auction.")
        else:
            # Form to create a new auction
            with st.form(key="create_auction_form"):
                st.markdown("### Product Information")
                
                # Basic product details
                product_types = get_product_types()
                product_type = st.selectbox("Product Type", options=product_types)
                product_name = st.text_input("Product Name")
                
                # Dynamic attributes based on product type
                st.markdown("### Product Attributes")
                
                # Define some common attributes based on product type
                attributes = {}
                
                if product_type == "Electronics":
                    attributes['brand'] = st.text_input("Brand")
                    attributes['model'] = st.text_input("Model")
                    attributes['condition'] = st.selectbox("Condition", ["New", "Like New", "Good", "Fair", "Poor"])
                    attributes['color'] = st.text_input("Color")
                    
                    if "Smartphone" in product_name or "Phone" in product_name or "Mobile" in product_name:
                        attributes['storage'] = st.text_input("Storage (GB)")
                        attributes['ram'] = st.text_input("RAM (GB)")
                        attributes['screen_size'] = st.text_input("Screen Size (inches)")
                    
                    if "Laptop" in product_name or "Computer" in product_name:
                        attributes['processor'] = st.text_input("Processor")
                        attributes['ram'] = st.text_input("RAM (GB)")
                        attributes['storage'] = st.text_input("Storage (GB)")
                        attributes['screen_size'] = st.text_input("Screen Size (inches)")
                
                elif product_type == "Home Appliances":
                    attributes['brand'] = st.text_input("Brand")
                    attributes['model'] = st.text_input("Model")
                    attributes['condition'] = st.selectbox("Condition", ["New", "Like New", "Good", "Fair", "Poor"])
                    attributes['color'] = st.text_input("Color")
                    attributes['energy_rating'] = st.text_input("Energy Rating")
                
                elif product_type == "Vehicle":
                    attributes['make'] = st.text_input("Make")
                    attributes['model'] = st.text_input("Model")
                    attributes['year'] = st.text_input("Year")
                    attributes['mileage'] = st.text_input("Mileage")
                    attributes['color'] = st.text_input("Color")
                    attributes['fuel_type'] = st.selectbox("Fuel Type", ["Petrol", "Diesel", "Electric", "Hybrid"])
                    attributes['transmission'] = st.selectbox("Transmission", ["Automatic", "Manual"])
                
                else:
                    # Generic attributes for other product types
                    attributes['brand'] = st.text_input("Brand")
                    attributes['model'] = st.text_input("Model")
                    attributes['condition'] = st.selectbox("Condition", ["New", "Like New", "Good", "Fair", "Poor"])
                    attributes['color'] = st.text_input("Color")
                
                # Custom attributes
                st.markdown("### Additional Attributes (Optional)")
                custom_attr1_name = st.text_input("Custom Attribute 1 Name")
                custom_attr1_value = st.text_input("Custom Attribute 1 Value")
                
                custom_attr2_name = st.text_input("Custom Attribute 2 Name")
                custom_attr2_value = st.text_input("Custom Attribute 2 Value")
                
                if custom_attr1_name and custom_attr1_value:
                    attributes[custom_attr1_name] = custom_attr1_value
                
                if custom_attr2_name and custom_attr2_value:
                    attributes[custom_attr2_name] = custom_attr2_value
                
                # Auction details
                st.markdown("### Auction Details")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    auction_type = st.selectbox("Auction Type", ["English", "Dutch", "Standard"])
                    base_price = st.number_input("Starting Price ($)", min_value=1.0, value=100.0, step=1.0)
                    
                with col2:
                    snipping_flag = st.checkbox("Enable Sniping Protection", value=True)
                    negotiation_enabled = st.checkbox("Allow Negotiation", value=True)
                
                # Auction dates
                start_date = st.date_input("Auction Start Date", value=datetime.date.today())
                start_time = st.time_input("Auction Start Time", value=datetime.time(hour=9, minute=0))
                
                end_date = st.date_input("Auction End Date", value=datetime.date.today() + datetime.timedelta(days=7))
                end_time = st.time_input("Auction End Time", value=datetime.time(hour=18, minute=0))
                
                # Combine date and time
                start_datetime = datetime.datetime.combine(start_date, start_time)
                end_datetime = datetime.datetime.combine(end_date, end_time)
                
                # Pickup details
                st.markdown("### Pickup Details")
                pickup_address = st.text_input("Pickup Address")
                pickup_date = st.date_input("Pickup Date", value=end_date + datetime.timedelta(days=1))
                pickup_time = st.time_input("Pickup Time", value=datetime.time(hour=12, minute=0))
                
                # Combine pickup date and time
                pickup_datetime = datetime.datetime.combine(pickup_date, pickup_time)
                
                # Submit button
                submit_button = st.form_submit_button(label="Create Auction")
                
                if submit_button:
                    if not product_name:
                        st.error("Please enter a product name.")
                    elif not pickup_address:
                        st.error("Please enter a pickup address.")
                    elif start_datetime >= end_datetime:
                        st.error("Auction end time must be after start time.")
                    else:
                        # Prepare auction details
                        auction_details = {
                            'start_time': start_datetime,
                            'end_time': end_datetime,
                            'auction_type': auction_type,
                            'base_price': base_price,
                            'snipping_flag': snipping_flag,
                            'negotiation_enabled': negotiation_enabled,
                            'pickup_address': pickup_address,
                            'pickup_datetime': pickup_datetime
                        }
                        
                        # Create the auction
                        result = create_new_auction(
                            user_id=st.session_state.user_id,
                            product_type=product_type,
                            product_name=product_name,
                            attributes=attributes,
                            auction_details=auction_details
                        )
                        
                        if result['success']:
                            st.success(result['message'])
                            time.sleep(1)
                            st.rerun()
                        else:
                            st.error(result['message'])
    
    # Tab 3: Sales Dashboard
    with seller_tabs[2]:
        st.markdown('<p class="section-header">Sales Dashboard</p>', unsafe_allow_html=True)
        
        if not st.session_state.logged_in:
            st.warning("Please log in to view your sales dashboard.")
        else:
            # Run the SQL queries to get sales data
            
            query1 = """
            SELECT 
                PC.ProductType,
                COUNT(I.InvoiceID) AS TotalInvoices,
                SUM(I.SellerAmount) AS TotalSales
            FROM Invoice I
            JOIN ProductDetails PD ON I.ProductID = PD.ProductID
            JOIN ProductConfiguration PC ON PD.ConfigurationID = PC.ConfigurationID
            WHERE I.SellerID = %s
            GROUP BY PC.ProductType
            """
            result1 = run_custom_query(query1, (st.session_state.user_id,))
            
            query9 = """
            SELECT 
                COALESCE(SUM(I.SellerAmount), 0) AS TotalRevenue 
            FROM Invoice I
            WHERE I.SellerID = %s AND I.InvoiceStatus = 'Paid'
            """
            result9 = run_custom_query(query9, (st.session_state.user_id,))
            
            # Create a summary dashboard
            if result1['success'] and result9['success']:
                # Display total revenue
                total_revenue = result9['result'][0]['TotalRevenue'] if result9['result'] else 0
                
                # Revenue card
                st.markdown(
                    f"""
                    <div class="card" style="text-align: center; padding: 30px;">
                        <h2>Total Revenue</h2>
                        <h1 style="color: var(--primary-color); font-size: 48px;">${total_revenue:.2f}</h1>
                    </div>
                    """, 
                    unsafe_allow_html=True
                )
                
                # Sales by product type
                if result1['result']:
                    st.markdown('<p class="section-header">Sales by Product Type</p>', unsafe_allow_html=True)
                    
                    # Convert to DataFrame
                    sales_by_type = pd.DataFrame(result1['result'])
                    
                    # Display as a chart
                    if not sales_by_type.empty:
                        col1, col2 = st.columns(2)
                        
                        with col1:
                            # Bar chart for sales
                            st.bar_chart(sales_by_type.set_index('ProductType')['TotalSales'])
                        
                        with col2:
                            # Pie chart for invoices
                            st.markdown('<div class="dataframe-container">', unsafe_allow_html=True)
                            st.dataframe(sales_by_type, use_container_width=True)
                            st.markdown('</div>', unsafe_allow_html=True)
                    else:
                        st.info("No sales data available.")
                else:
                    st.info("No sales data available.")
            else:
                st.error("Error fetching sales data.")

def show_analytics_tab():
    st.markdown('<p class="section-header">Database Analytics</p>', unsafe_allow_html=True)
    
    preset_queries = [
        "1. Total Sales and Invoice Count by Product Type",
        "2. Highest Bid per Closed Auction with Auction Creator",
        "3. Bid Statistics per Product",
        "4. All Losing Bids (Sorted by Amount)",
        "5. User Bidding Statistics",
        "6. Product Bid Counts on Latest Auctions",
        "7. Paid Buyers",
        "8. Products Sold by Category",
        "9. Total Revenue per Seller",
        "10. Average Bid Amount per Auction"
    ]
    
    selected_query = st.selectbox("Select a Preset Query", preset_queries)
    
    query_mapping = {
        "1. Total Sales and Invoice Count by Product Type": """
            SELECT 
                PC.ProductType,
                COUNT(I.InvoiceID) AS TotalInvoices,
                SUM(I.SellerAmount) AS TotalSales
            FROM Invoice I
            JOIN ProductDetails PD ON I.ProductID = PD.ProductID
            JOIN ProductConfiguration PC ON PD.ConfigurationID = PC.ConfigurationID
            GROUP BY PC.ProductType;
        """,
        "2. Highest Bid per Closed Auction with Auction Creator": """
            SELECT 
                A.AuctionID,
                A.AuctionStatus,
                U.Name AS AuctionCreator,
                B.MaxBid,
                A.AuctionBasePrice
            FROM Auction A
            JOIN User U ON A.UserID = U.UserID
            JOIN (
                SELECT AuctionID, MAX(BidAmount) AS MaxBid
                FROM Bid
                GROUP BY AuctionID
            ) B ON A.AuctionID = B.AuctionID
            WHERE A.AuctionStatus = 'Closed';
        """,
        "3. Bid Statistics per Product": """
            SELECT 
                PD.ProductID,
                PC.Product AS ProductName,
                PD.LatestAuctionStatus,
                COUNT(B.BidID) AS NumBids,
                AVG(B.BidAmount) AS AvgBid
            FROM ProductDetails PD
            JOIN ProductConfiguration PC ON PD.ConfigurationID = PC.ConfigurationID
            LEFT JOIN Bid B ON PD.ProductID = B.ProductID
            GROUP BY PD.ProductID, PC.Product, PD.LatestAuctionStatus;
        """,
        "4. All Losing Bids (Sorted by Amount)": """
            SELECT 
                b.BidID,
                u.Name AS BidderName,
                pc.Product AS ProductName,
                b.BidAmount,
                b.isWinningBid,
                b.WinTimestamp
            FROM Bid b
            JOIN User u ON b.UserID = u.UserID
            JOIN ProductDetails pd ON b.ProductID = pd.ProductID
            JOIN ProductConfiguration pc ON pd.ConfigurationID = pc.ConfigurationID
            WHERE b.isWinningBid = FALSE
            ORDER BY b.BidAmount DESC;
        """,
        "5. User Bidding Statistics": """
            SELECT
                U.UserID,
                U.Name,
                U.Email,
                COUNT(B.BidID) AS TotalBids,
                MAX(B.BidAmount) AS MaxBid
            FROM User U
            LEFT JOIN Bid B ON U.UserID = B.UserID
            GROUP BY U.UserID, U.Name, U.Email
            ORDER BY TotalBids DESC, MaxBid DESC;
        """,
        "6. Product Bid Counts on Latest Auctions": """
            SELECT
                PD.ProductID,
                PC.Product,
                A.AuctionStatus AS LatestAuctionStatus,
                COUNT(B.BidID) AS TotalBids
            FROM ProductDetails PD
            INNER JOIN ProductConfiguration PC ON PD.ConfigurationID = PC.ConfigurationID
            INNER JOIN Auction A ON PD.ProductID = A.ProductID
            LEFT JOIN Bid B ON A.AuctionID = B.AuctionID
            WHERE A.AuctionID IN (
                SELECT MAX(AuctionID)
                FROM Auction
                GROUP BY ProductID
            )
            GROUP BY PD.ProductID, PC.Product, A.AuctionStatus;
        """,
        "7. Paid Buyers": """
            SELECT
                U.UserID,
                U.Name,
                U.Email,
                I.InvoiceID,
                I.InvoiceStatus
            FROM User U
            INNER JOIN Invoice I ON U.UserID = I.BuyerID
            WHERE I.InvoiceStatus = 'Paid';
        """,
        "8. Products Sold by Category": """
            SELECT
                PC.ProductType,
                COUNT(*) AS TotalSales
            FROM ProductConfiguration PC
            INNER JOIN ProductDetails PD ON PC.ConfigurationID = PD.ConfigurationID
            WHERE PD.Status = 'Sold'
            GROUP BY PC.ProductType
            ORDER BY TotalSales DESC;
        """,
        "9. Total Revenue per Seller": """
            SELECT 
                U.UserID, 
                U.Name, 
                COALESCE(SUM(I.SellerAmount), 0) AS TotalRevenue 
            FROM User U
            LEFT JOIN Invoice I ON U.UserID = I.SellerID
            WHERE I.InvoiceStatus = 'Paid'
            GROUP BY U.UserID;
        """,
        "10. Average Bid Amount per Auction": """
            SELECT 
                A.AuctionID, 
                AVG(B.BidAmount) AS AvgBidAmount
            FROM Auction A
            INNER JOIN Bid B ON A.AuctionID = B.AuctionID
            GROUP BY A.AuctionID;
        """
    }
    
    query = query_mapping.get(selected_query, "")
    
    st.code(query, language="sql")
    
    if st.button("Run Query"):
        result = run_custom_query(query)
        
        if result['success']:
            if result['result']:
                df = pd.DataFrame(result['result'])
                st.markdown('<div class="dataframe-container">', unsafe_allow_html=True)
                st.dataframe(df, use_container_width=True)
                st.markdown('</div>', unsafe_allow_html=True)
                
                csv = df.to_csv(index=False)
                b64 = base64.b64encode(csv.encode()).decode()
                href = f'<a href="data:file/csv;base64,{b64}" download="query_results.csv" class="btn btn-primary">Download CSV</a>'
                st.markdown(href, unsafe_allow_html=True)
            else:
                st.info("The query returned no results.")
        else:
            st.error(result['message'])
    
    st.markdown('<p class="section-header">Custom SQL Query</p>', unsafe_allow_html=True)
    
    custom_query = st.text_area("Enter your custom SQL query", height=150)
    
    if st.button("Run Custom Query"):
        if custom_query:
            result = run_custom_query(custom_query)
            
            if result['success']:
                if result['result']:
                    df = pd.DataFrame(result['result'])
                    
                    st.markdown('<div class="dataframe-container">', unsafe_allow_html=True)
                    st.dataframe(df, use_container_width=True)
                    st.markdown('</div>', unsafe_allow_html=True)
                    
                    # Download button
                    csv = df.to_csv(index=False)
                    b64 = base64.b64encode(csv.encode()).decode()
                    href = f'<a href="data:file/csv;base64,{b64}" download="custom_query_results.csv" class="btn btn-primary">Download CSV</a>'
                    st.markdown(href, unsafe_allow_html=True)
                else:
                    st.info("The query returned no results.")
            else:
                st.error(result['message'])
        else:
            st.warning("Please enter a SQL query.")

def show_account_tab():
    # account tab with user information and bidding history
    if not st.session_state.logged_in:
        st.warning("Please log in to view your account information.")
        return
    
    st.markdown('<p class="section-header">My Account</p>', unsafe_allow_html=True)
    
    # User information
    connection = create_connection()
    if connection:
        query = "SELECT * FROM User WHERE UserID = %s"
        result = execute_query(connection, query, (st.session_state.user_id,))
        connection.close()
        
        if result:
            user = result[0]
            
            # Display user info
            st.markdown(
                f"""
                <div class="card">
                    <h3>Account Information</h3>
                    <p><strong>Name:</strong> {user['Name']}</p>
                    <p><strong>Email:</strong> {user['Email']}</p>
                    <p><strong>Phone:</strong> {user['Phone']}</p>
                    <p><strong>Address:</strong> {user['Address']}</p>
                </div>
                """, 
                unsafe_allow_html=True
            )
    
    # Bidding history
    st.markdown('<p class="section-header">My Bidding History</p>', unsafe_allow_html=True)
    
    bids = get_user_bids(st.session_state.user_id)
    
    if not bids:
        st.info("You haven't placed any bids yet.")
    else:

        bids_df = pd.DataFrame(bids)
        
        if 'BidTimestamp' in bids_df.columns:
            bids_df['BidTimestamp'] = bids_df['BidTimestamp'].apply(
                lambda x: x.strftime('%Y-%m-%d %H:%M') if x else '')
        
        # Display active bids (auctions still open)
        active_bids = bids_df[bids_df['AuctionStatus'] == 'Open']
        
        if not active_bids.empty:
            st.markdown("<h3>Active Bids</h3>", unsafe_allow_html=True)
            st.markdown('<div class="dataframe-container">', unsafe_allow_html=True)
            st.dataframe(
                active_bids[['BidID', 'ProductType', 'Product', 'BidTimestamp', 'BidAmount']],
                use_container_width=True
            )
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Display completed bids
        completed_bids = bids_df[bids_df['AuctionStatus'] != 'Open']
        
        if not completed_bids.empty:
            st.markdown("<h3>Completed Bids</h3>", unsafe_allow_html=True)
            st.markdown('<div class="dataframe-container">', unsafe_allow_html=True)
            st.dataframe(
                completed_bids[['BidID', 'ProductType', 'Product', 'BidTimestamp', 'BidAmount', 'isWinningBid']],
                use_container_width=True
            )
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Show won items
            won_bids = completed_bids[completed_bids['isWinningBid'] == True]
            
            if not won_bids.empty:
                st.markdown("<h3>Items Won</h3>", unsafe_allow_html=True)
                st.markdown('<div class="dataframe-container">', unsafe_allow_html=True)
                st.dataframe(
                    won_bids[['BidID', 'ProductType', 'Product', 'BidTimestamp', 'BidAmount']],
                    use_container_width=True
                )
                st.markdown('</div>', unsafe_allow_html=True)

def show_admin_panel():

    st.markdown('<div class="admin-header"><h2>Admin Panel</h2></div>', unsafe_allow_html=True)
    
    # Create tabs for different admin functions
    admin_tabs = st.tabs(["User Management", "Auction Management", "System Stats", "Database Operations"])
    
    # Tab 1: User Management
    with admin_tabs[0]:
        st.markdown('<p class="section-header">User Management</p>', unsafe_allow_html=True)
        
        # Get all users
        connection = create_connection()
        if connection:
            query = "SELECT UserID, Name, Email, Phone, Address, isBlocked FROM User ORDER BY UserID"
            users = execute_query(connection, query)
            connection.close()
            
            if users:
                # Convert to DataFrame
                users_df = pd.DataFrame(users)
                
                # Display users
                st.markdown('<div class="dataframe-container">', unsafe_allow_html=True)
                st.dataframe(users_df, use_container_width=True)
                st.markdown('</div>', unsafe_allow_html=True)
                
                # Block/Unblock user
                col1, col2 = st.columns(2)
                
                with col1:
                    user_id_to_edit = st.number_input("Enter User ID", min_value=1, step=1)
                
                with col2:
                    action = st.selectbox("Action", ["Block User", "Unblock User"])
                
                if st.button("Apply Action"):
                    if action == "Block User":
                        query = "UPDATE User SET isBlocked = TRUE WHERE UserID = %s"
                    else:
                        query = "UPDATE User SET isBlocked = FALSE WHERE UserID = %s"
                    
                    connection = create_connection()
                    if connection:
                        execute_query(connection, query, (user_id_to_edit,))
                        connection.commit()
                        connection.close()
                        st.success(f"User {user_id_to_edit} has been {action.split()[0].lower()}ed.")
                        time.sleep(1)
                        st.rerun()
            else:
                st.info("No users found.")
    
    # Tab 2: Auction Management
    with admin_tabs[1]:
        st.markdown('<p class="section-header">Auction Management</p>', unsafe_allow_html=True)
        
        # Get all auctions
        connection = create_connection()
        if connection:
            query = """
            SELECT 
                A.AuctionID, 
                A.ProductID, 
                PC.ProductType, 
                PC.Product, 
                U.Name AS SellerName,
                A.AuctionStartTime, 
                A.AuctionEndTime, 
                A.AuctionStatus, 
                A.AuctionBasePrice
            FROM Auction A
            JOIN ProductDetails PD ON A.ProductID = PD.ProductID
            JOIN ProductConfiguration PC ON PD.ConfigurationID = PC.ConfigurationID
            JOIN User U ON A.UserID = U.UserID
            ORDER BY A.AuctionStartTime DESC
            """
            auctions = execute_query(connection, query)
            connection.close()
            
            if auctions:
                # Convert to DataFrame
                auctions_df = pd.DataFrame(auctions)
                
                # Format date columns
                if 'AuctionStartTime' in auctions_df.columns:
                    auctions_df['AuctionStartTime'] = auctions_df['AuctionStartTime'].apply(
                        lambda x: x.strftime('%Y-%m-%d %H:%M') if x else '')
                
                if 'AuctionEndTime' in auctions_df.columns:
                    auctions_df['AuctionEndTime'] = auctions_df['AuctionEndTime'].apply(
                        lambda x: x.strftime('%Y-%m-%d %H:%M') if x else '')
                
                # Display auctions
                st.markdown('<div class="dataframe-container">', unsafe_allow_html=True)
                st.dataframe(auctions_df, use_container_width=True)
                st.markdown('</div>', unsafe_allow_html=True)
            
                col1, col2 = st.columns(2)
                
                with col1:
                    auction_id_to_edit = st.number_input("Enter Auction ID", min_value=1, step=1)
                
                with col2:
                    new_status = st.selectbox("New Status", ["Open", "Closed", "Cancelled"])
                
                if st.button("Update Auction Status"):
                    query = "UPDATE Auction SET AuctionStatus = %s WHERE AuctionID = %s"
                    
                    connection = create_connection()
                    if connection:
                        execute_query(connection, query, (new_status, auction_id_to_edit))
                        
                        query = """
                        UPDATE ProductDetails PD
                        SET LatestAuctionStatus = %s
                        WHERE ProductID = (
                            SELECT ProductID FROM Auction WHERE AuctionID = %s
                        )
                        """
                        execute_query(connection, query, (new_status, auction_id_to_edit))
                        
                        connection.commit()
                        connection.close()
                        st.success(f"Auction {auction_id_to_edit} status updated to {new_status}.")
                        time.sleep(1)
                        st.rerun()
            else:
                st.info("No auctions found.")
    
    # Tab 3: System Stats
    with admin_tabs[2]:
        st.markdown('<p class="section-header">System Statistics</p>', unsafe_allow_html=True)
        
        # Create columns for stats
        col1, col2 = st.columns(2)
        
        connection = create_connection()
        if connection:
            # Get total users
            query = "SELECT COUNT(*) AS TotalUsers FROM User"
            result = execute_query(connection, query)
            total_users = result[0]['TotalUsers'] if result else 0
            
            # Get total products
            query = "SELECT COUNT(*) AS TotalProducts FROM ProductDetails"
            result = execute_query(connection, query)
            total_products = result[0]['TotalProducts'] if result else 0
            
            # Get total auctions
            query = "SELECT COUNT(*) AS TotalAuctions FROM Auction"
            result = execute_query(connection, query)
            total_auctions = result[0]['TotalAuctions'] if result else 0
            
            # Get total bids
            query = "SELECT COUNT(*) AS TotalBids FROM Bid"
            result = execute_query(connection, query)
            total_bids = result[0]['TotalBids'] if result else 0
            
            # Get total sales
            query = "SELECT COUNT(*) AS TotalSales FROM ProductDetails WHERE Status = 'Sold'"
            result = execute_query(connection, query)
            total_sales = result[0]['TotalSales'] if result else 0
            
            # Get total revenue
            query = "SELECT SUM(SellerAmount) AS TotalRevenue FROM Invoice WHERE InvoiceStatus = 'Paid'"
            result = execute_query(connection, query)
            total_revenue = result[0]['TotalRevenue'] if result and result[0]['TotalRevenue'] else 0
            
            connection.close()

            with col1:
                st.markdown(
                    f"""
                    <div class="card" style="text-align: center; padding: 30px; margin-bottom: 20px;">
                        <h3>Total Users</h3>
                        <h2 style="color: var(--primary-color);">{total_users}</h2>
                    </div>
                    <div class="card" style="text-align: center; padding: 30px; margin-bottom: 20px;">
                        <h3>Total Products</h3>
                        <h2 style="color: var(--primary-color);">{total_products}</h2>
                    </div>
                    <div class="card" style="text-align: center; padding: 30px;">
                        <h3>Total Auctions</h3>
                        <h2 style="color: var(--primary-color);">{total_auctions}</h2>
                    </div>
                    """, 
                    unsafe_allow_html=True
                )
            
            with col2:
                st.markdown(
                    f"""
                    <div class="card" style="text-align: center; padding: 30px; margin-bottom: 20px;">
                        <h3>Total Bids</h3>
                        <h2 style="color: var(--primary-color);">{total_bids}</h2>
                    </div>
                    <div class="card" style="text-align: center; padding: 30px; margin-bottom: 20px;">
                        <h3>Total Sales</h3>
                        <h2 style="color: var(--primary-color);">{total_sales}</h2>
                    </div>
                    <div class="card" style="text-align: center; padding: 30px;">
                        <h3>Total Revenue</h3>
                        <h2 style="color: var(--primary-color);">${total_revenue:.2f}</h2>
                    </div>
                    """, 
                    unsafe_allow_html=True
                )
    
    # Tab 4: Database Operations
    with admin_tabs[3]:
        st.markdown('<p class="section-header">Database Operations</p>', unsafe_allow_html=True)
        
        # Execute custom SQL
        st.markdown("<h3>Execute SQL Commands</h3>", unsafe_allow_html=True)
        sql_command = st.text_area("Enter SQL Command", height=150)
        
        if st.button("Execute SQL"):
            if sql_command:
                # Check if it's a SELECT query
                is_select = sql_command.strip().upper().startswith("SELECT")
                
                connection = create_connection()
                if connection:
                    try:
                        if is_select:
                            result = execute_query(connection, sql_command)
                            
                            if result:
                                # Convert to DataFrame
                                df = pd.DataFrame(result)
                                
                                # Display the results
                                st.markdown('<div class="dataframe-container">', unsafe_allow_html=True)
                                st.dataframe(df, use_container_width=True)
                                st.markdown('</div>', unsafe_allow_html=True)
                            else:
                                st.info("The query returned no results.")
                        else:
                            # For non-SELECT queries
                            cursor = connection.cursor()
                            cursor.execute(sql_command)
                            connection.commit()
                            st.success(f"SQL command executed successfully. {cursor.rowcount} row(s) affected.")
                            cursor.close()
                        
                        connection.close()
                    except Error as e:
                        connection.rollback()
                        connection.close()
                        st.error(f"Error executing SQL: {str(e)}")
            else:
                st.warning("Please enter a SQL command.")
        
        st.markdown("<h3>Database Backup</h3>", unsafe_allow_html=True)
        if st.button("Generate Database Backup"):
            # This is a simplified example - in a real app, you'd use a more robust backup method
            connection = create_connection()
            if connection:
                try:
                    # Get all table names
                    query = "SHOW TABLES"
                    tables = execute_query(connection, query)
                    
                    backup_data = {}
                    
                    for table in tables:
                        table_name = list(table.values())[0]
                        query = f"SELECT * FROM {table_name}"
                        data = execute_query(connection, query)
                        backup_data[table_name] = data
                    
                    # Convert to JSON
                    backup_json = json.dumps(backup_data, default=str, indent=4)
                    
                    # Create a download link
                    b64 = base64.b64encode(backup_json.encode()).decode()
                    now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                    href = f'<a href="data:file/json;base64,{b64}" download="bidbazar_backup_{now}.json" class="btn btn-primary">Download Backup File</a>'
                    st.markdown(href, unsafe_allow_html=True)
                    
                    connection.close()
                except Error as e:
                    connection.close()
                    st.error(f"Error generating backup: {str(e)}")

def main():
    show_header()

    if st.session_state.logged_in:
  
        with st.sidebar:
            # Check if user is admin (considerin UserID 1 as admin)
            is_admin = (st.session_state.user_id == 1)
            
            if is_admin:
                selected = option_menu(
                    "Navigation", 
                    ["Home", "Account", "Analytics", "Admin"],
                    icons=["house", "person", "graph-up", "shield-lock"], 
                    menu_icon="cast", 
                    default_index=0
                )
            else:
                selected = option_menu(
                    "Navigation", 
                    ["Home", "Account", "Analytics"],
                    icons=["house", "person", "graph-up"], 
                    menu_icon="cast", 
                    default_index=0
                )
        
        if selected == "Home":
            if st.session_state.user_type == "buyer":
                show_buyer_interface()
            else:  # seller
                show_seller_interface()
        
        elif selected == "Account":
            # Show account information
            show_account_tab()
        
        elif selected == "Analytics":
            # Show analytics tab
            show_analytics_tab()
            
        elif selected == "Admin" and st.session_state.user_id == 1:  # Only for admin
            # Show admin panel
            show_admin_panel()
    
    else:
        # Show welcome page for non-logged in users
        st.markdown(
            """
            <div style="text-align: center; padding: 50px 20px;">
                <h1 style="color: var(--primary-color);">Welcome to BidBazar!</h1>
                <p style="font-size: 20px; margin-bottom: 30px;">Your one-stop platform for online auctions</p>
                <div style="background-color: white; border-radius: 10px; padding: 20px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); max-width: 600px; margin: 0 auto;">
                    <h2>Get Started</h2>
                    <p>Please log in to start bidding or selling on BidBazar.</p>
                    <p>Use the login form in the sidebar to access your account.</p>
                </div>
            </div>
            """, 
            unsafe_allow_html=True
        )
        
        # Show some featured auctions
        st.markdown('<p class="section-header">Featured Auctions</p>', unsafe_allow_html=True)
        
        # Get a few available auctions to display
        featured_auctions = get_available_auctions()
        if featured_auctions:
            # Only show a few
            featured_auctions = featured_auctions[:6]
            
            # Display auctions in a grid view
            st.markdown('<div class="product-grid">', unsafe_allow_html=True)
            
            # Use columns to create a grid
            cols = st.columns(3)
            
            for i, auction in enumerate(featured_auctions):
                with cols[i % 3]:
                    # Calculate time remaining
                    end_time = auction['AuctionEndTime']
                    time_remaining = end_time - datetime.datetime.now()
                    days_remaining = time_remaining.days
                    hours_remaining = time_remaining.seconds // 3600
                    
                    # Product card
                    st.markdown(
                        f"""
                        <div class="product-card">
                            <div class="product-info">
                                <div class="product-title">{auction['Product']} ({auction['ProductType']})</div>
                                <p>Seller: {auction['SellerName']}</p>
                                <p>Starting Price: <span class="product-price">${auction['AuctionBasePrice']:.2f}</span></p>
                                <p>Current Highest Bid: <span class="product-price">${auction['CurrentHighestBid'] if auction['CurrentHighestBid'] else auction['AuctionBasePrice']:.2f}</span></p>
                                <p>Time Remaining: {days_remaining} days, {hours_remaining} hours</p>
                                <p>Login to place bids</p>
                            </div>
                        </div>
                        """, 
                        unsafe_allow_html=True
                    )
if __name__ == "__main__":
    main()
