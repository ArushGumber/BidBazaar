import mysql
import mysql.connector
from mysql.connector import Error
import os
import sys
from config import DB_CONFIG

# SQL scripts to create tables
create_tables_sql = """
-- Table: User
CREATE TABLE IF NOT EXISTS User (
    UserID INTEGER PRIMARY KEY,
    Name VARCHAR(255),
    Email VARCHAR(255),
    Phone VARCHAR(20),
    Password VARCHAR(255),
    Address VARCHAR(255),
    isBlocked BOOLEAN
);

-- Table: ProductConfiguration
CREATE TABLE IF NOT EXISTS ProductConfiguration (
    ConfigurationID INTEGER PRIMARY KEY,
    Created TIMESTAMP,
    ProductType VARCHAR(255),
    Product VARCHAR(255)
);

-- Table: ProductDetails
CREATE TABLE IF NOT EXISTS ProductDetails (
    ProductID INTEGER PRIMARY KEY,
    ConfigurationID INTEGER,
    LatestAuctionStatus VARCHAR(255),
    WinningBidID INTEGER,
    BuyerID INTEGER,
    Status VARCHAR(255),
    FOREIGN KEY (ConfigurationID) REFERENCES ProductConfiguration(ConfigurationID)
);

-- Table: ProductInventory
CREATE TABLE IF NOT EXISTS ProductInventory (
    ProductID INTEGER PRIMARY KEY,
    PickupAddress VARCHAR(255),
    PickupDateTime TIMESTAMP,
    AmountForSeller DECIMAL(10,2),
    DeliveryAddress VARCHAR(255),
    DeliveryDate TIMESTAMP,
    Status VARCHAR(255),
    SellerReceiptID INTEGER,
    BuyerReceiptID INTEGER,
    FOREIGN KEY (ProductID) REFERENCES ProductDetails(ProductID)
);

-- Table: Auction
CREATE TABLE IF NOT EXISTS Auction (
    AuctionID INTEGER PRIMARY KEY,
    ProductID INTEGER,
    UserID INTEGER,
    AuctionStartTime TIMESTAMP,
    AuctionEndTime TIMESTAMP,
    AuctionStatus VARCHAR(255),
    AuctionType VARCHAR(255),
    SnippingFlag BOOLEAN,
    AuctionBasePrice DECIMAL(10,2),
    NegotiationEnabled BOOLEAN,
    FOREIGN KEY (ProductID) REFERENCES ProductDetails(ProductID),
    FOREIGN KEY (UserID) REFERENCES User(UserID)
);

-- Table: Bid
CREATE TABLE IF NOT EXISTS Bid (
    BidID INTEGER PRIMARY KEY,
    AuctionID INTEGER,
    ProductID INTEGER,
    UserID INTEGER,
    BidTimestamp TIMESTAMP,
    BidAmount DECIMAL(10,2),
    isWinningBid BOOLEAN,
    WinTimestamp TIMESTAMP,
    isAutoBid BOOLEAN,
    FOREIGN KEY (AuctionID) REFERENCES Auction(AuctionID),
    FOREIGN KEY (ProductID) REFERENCES ProductDetails(ProductID),
    FOREIGN KEY (UserID) REFERENCES User(UserID)
);

-- Table: AutoBid
CREATE TABLE IF NOT EXISTS AutoBid (
    BidID INTEGER PRIMARY KEY,
    StartingBid DECIMAL(10,2),
    MaxBid DECIMAL(10,2),
    StepRate DECIMAL(10,2),
    FOREIGN KEY (BidID) REFERENCES Bid(BidID)
);

-- Table: Invoice
CREATE TABLE IF NOT EXISTS Invoice (
    InvoiceID INTEGER PRIMARY KEY,
    BuyerID INTEGER,                
    SellerID INTEGER,              
    ReceiptID INTEGER,             
    ProductID INTEGER,
    CreatedTimestamp TIMESTAMP,
    SellerAmount DECIMAL(10,2),
    ServiceRate DECIMAL(10,2),
    FinalSellerPayout DECIMAL(10,2),
    BuyerPayout DECIMAL(10,2),
    InvoiceStatus VARCHAR(255),
    FOREIGN KEY (BuyerID) REFERENCES User(UserID),
    FOREIGN KEY (SellerID) REFERENCES User(UserID),
    FOREIGN KEY (ProductID) REFERENCES ProductDetails(ProductID)
);

-- Table: ProductAttributes
CREATE TABLE IF NOT EXISTS ProductAttributes (
    ProductID INTEGER,
    AttributeName VARCHAR(255),
    AttributeValue VARCHAR(255),
    PRIMARY KEY (ProductID, AttributeName),
    FOREIGN KEY (ProductID) REFERENCES ProductDetails(ProductID)
);
"""

# Function to create the database
def create_database():
    connection = None
    try:
        # Connect to MySQL server without specifying a database
        connection = mysql.connector.connect(
            host=DB_CONFIG['host'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password']
        )

        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create the database if it doesn't exist
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_CONFIG['database']}")
            print(f"Database '{DB_CONFIG['database']}' created or already exists")
            
            # Connect to the bidbazar database
            cursor.execute(f"USE {DB_CONFIG['database']}")
            
            # Execute the SQL to create tables
            for statement in create_tables_sql.split(';'):
                if statement.strip():
                    cursor.execute(statement + ';')
            
            connection.commit()
            print("Tables created successfully")
            
            # Insert initial admin user if it doesn't exist
            cursor.execute("SELECT COUNT(*) FROM User WHERE UserID = 1")
            count = cursor.fetchone()[0]
            
            if count == 0:
                cursor.execute("""
                INSERT INTO User (UserID, Name, Email, Phone, Password, Address, isBlocked) 
                VALUES (1, 'Admin User', 'admin@bidbazar.com', '1234567890', 'admin123', 'Admin Address', FALSE)
                """)
                connection.commit()
                print("Admin user created")
            
            cursor.close()
    
    except Error as e:
        print(f"Error: {e}")
    
    finally:
        if connection and connection.is_connected():
            connection.close()
            print("MySQL connection closed")

# Main function
def main():
    print("Initializing BidBazar database...")
    create_database()
    print("Database initialization completed")

if __name__ == "__main__":
    main()