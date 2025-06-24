

DROP TABLE IF EXISTS ProductAttributes CASCADE;
DROP TABLE IF EXISTS Invoice CASCADE;
DROP TABLE IF EXISTS AutoBid CASCADE;
DROP TABLE IF EXISTS Bid CASCADE;
DROP TABLE IF EXISTS Auction CASCADE;
DROP TABLE IF EXISTS ProductInventory CASCADE;
DROP TABLE IF EXISTS ProductDetails CASCADE;
DROP TABLE IF EXISTS ProductConfiguration CASCADE;
DROP TABLE IF EXISTS User CASCADE;

CREATE TABLE User (
    UserID INTEGER PRIMARY KEY,
    Name VARCHAR(255),
    Email VARCHAR(255),
    Phone VARCHAR(20),
    Password VARCHAR(255),
    Address VARCHAR(255),
    isBlocked BOOLEAN
);
-- End of User table

-- Table: ProductConfiguration
-- This table holds common product configuration information.
CREATE TABLE ProductConfiguration (
    ConfigurationID INTEGER PRIMARY KEY,
    Created TIMESTAMP,
    ProductType VARCHAR(255),
    Product VARCHAR(255)
);
-- End of ProductConfiguration table

-- Table: ProductDetails
-- Contains instance specific data.
CREATE TABLE ProductDetails (
    ProductID INTEGER PRIMARY KEY,
    ConfigurationID INTEGER,
    LatestAuctionStatus VARCHAR(255),
    WinningBidID INTEGER,
    BuyerID INTEGER,
    Status VARCHAR(255),
    FOREIGN KEY (ConfigurationID) REFERENCES ProductConfiguration(ConfigurationID)
);
-- End of ProductDetails table

-- Table: ProductInventory
CREATE TABLE ProductInventory (
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
-- End of ProductInventory table

-- Table: Auction
CREATE TABLE Auction (
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
-- End of Auction table

-- Table: Bid
CREATE TABLE Bid (
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
-- End of Bid table

-- Table: AutoBid
-- Contains auto-bid configuration for bids that support automatic bidding.
CREATE TABLE AutoBid (
    BidID INTEGER PRIMARY KEY,
    StartingBid DECIMAL(10,2),
    MaxBid DECIMAL(10,2),
    StepRate DECIMAL(10,2),
    FOREIGN KEY (BidID) REFERENCES Bid(BidID)
);
-- End of AutoBid table

-- Table: Invoice
CREATE TABLE Invoice (
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
-- End of Invoice table

-- Table: ProductAttributes
-- New EAV table to store product-specific attributes.
-- This replaces JSON columns and prevents storing nulls for non-applicable attributes.
CREATE TABLE ProductAttributes (
    ProductID INTEGER,
    AttributeName VARCHAR(255),
    AttributeValue VARCHAR(255),
    PRIMARY KEY (ProductID, AttributeName),
    FOREIGN KEY (ProductID) REFERENCES ProductDetails(ProductID)
);
-- End of ProductAttributes table

