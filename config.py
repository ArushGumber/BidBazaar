# BidBazar Configuration File

# Database configuration
DB_CONFIG = {
    'host': 'localhost',
    'database': 'BidBazar',
    'user': 'root',
    'password': '_'  
}

# Application settings
APP_SETTINGS = {
    'app_name': 'BidBazar',
    'app_logo': '🛒',
    'theme_primary_color': '#1e88e5',
    'theme_secondary_color': '#4caf50',
    'default_currency': 'USD',
    'min_bid_increment': 1.0,
    'default_auction_duration_days': 7,
    'enable_email_notifications': False,
    'enable_sms_notifications': False
}

# Feature toggles
FEATURES = {
    'auto_bidding': True,
    'negotiation': True,
    'sniping_protection': True,
    'analytics': True,
    'admin_panel': True
}

# Product types and attributes
PRODUCT_TYPES = {
    'Electronics': ['brand', 'model', 'condition', 'color'],
    'Home Appliances': ['brand', 'model', 'condition', 'energy_rating'],
    'Vehicle': ['make', 'model', 'year', 'mileage', 'fuel_type', 'transmission'],
    'Fashion': ['brand', 'size', 'color', 'material', 'condition'],
    'Books': ['author', 'publisher', 'genre', 'condition', 'language'],
    'Sports & Outdoors': ['brand', 'type', 'condition', 'material'],
    'Collectibles': ['era', 'condition', 'rarity', 'origin']
}

# Auction types
AUCTION_TYPES = ['English', 'Dutch', 'Standard']

# Status options
STATUS_OPTIONS = {
    'auction': ['Open', 'Closed', 'Cancelled'],
    'product': ['Available', 'Sold', 'Not Available'],
    'inventory': ['Pending', 'Shipped', 'Delivered', 'Cancelled']
}

# Demo data settings
DEMO_MODE = True
DEMO_ADMIN_USER = {
    'id': 1,
    'name': 'Admin User',
    'email': 'admin@bidbazar.com',
    'password': 'admin123'
}