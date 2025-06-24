-- 1. Total Sales and Invoice Count by Product Type

	SELECT 
    PC.ProductType,
    COUNT(I.InvoiceID) AS TotalInvoices,
    SUM(I.SellerAmount) AS TotalSales
FROM Invoice I
JOIN ProductDetails PD ON I.ProductID = PD.ProductID
JOIN ProductConfiguration PC ON PD.ConfigurationID = PC.ConfigurationID
GROUP BY PC.ProductType;


-- 2. Highest Bid per Closed Auction with Auction Creator

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

-- 3. Bid Statistics per Product

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

-- 4. this query is getting all bids where the bidder lost. it shows bid id, bidder name, product name, bid amount, win status, and timestamp. bids are sorted from highest amount to lowest.

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

-- 5. this query is showing each user's total bids and highest bid amount. it includes users even if they haven't bid (because of left join). sorted by most active bidders and biggest bids.

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

-- 6. this query shows product id, product name, latest auction status, and how many bids were placed on its most recent auction. grouped by product.


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

-- 7.  this query gets all users who have bought something (buyer in invoice) and shows their name, email, and invoice status — only shows "Paid" invoices.


SELECT
    U.UserID,
    U.Name,
    U.Email,
    I.InvoiceID,
    I.InvoiceStatus
FROM User U
INNER JOIN Invoice I ON U.UserID = I.BuyerID
WHERE I.InvoiceStatus = 'Paid';

-- 8. this query groups sold products by their product type (like electronics, fashion) and shows how many total sales (sold products) each type has. sorted by most sold category first.


SELECT
    PC.ProductType,
    COUNT(*) AS TotalSales
FROM ProductConfiguration PC
INNER JOIN ProductDetails PD ON PC.ConfigurationID = PD.ConfigurationID
WHERE PD.Status = 'Sold'
GROUP BY PC.ProductType
ORDER BY TotalSales DESC;

-- 9.
-- QUERY: finding total revenue for each User who has sold in auction, and recieved the money (bill is paid)
SELECT 
    U.UserID, 
    U.Name, 
    COALESCE(SUM(I.SellerAmount), 0) AS TotalRevenue 
FROM User U
LEFT JOIN Invoice I ON U.UserID = I.SellerID
WHERE I.InvoiceStatus = 'Paid'
GROUP BY U.UserID;

-- 10.
-- Query: calculates the average bid amount for each auction.
SELECT 
    A.AuctionID, 
    AVG(B.BidAmount) AS AvgBidAmount
FROM Auction A
INNER JOIN Bid B ON A.AuctionID = B.AuctionID
GROUP BY A.AuctionID;


-- Wrong gpt query
-- wrong chat gpt query 1 
-- gpt made this error by trying to join ProductConfiguration to a table Product which doesn't exist in our schema. I fixed it by just using the Product column from ProductConfiguration itself.

SELECT 
    Category,
    ProductID,
    ProductName,
    TotalSales,
    RANK() OVER (PARTITION BY Category ORDER BY TotalSales DESC) AS SalesRank
FROM (
    SELECT 
        PC.ProductType AS Category,
        PD.ProductID,
        P.Product AS ProductName,
        SUM(I.FinalSellerPayout) AS TotalSales
    FROM ProductDetails PD
    INNER JOIN ProductConfiguration PC ON PD.ConfigurationID = PC.ConfigurationID
    INNER JOIN Product P ON PC.Product = P.Product
    INNER JOIN Invoice I ON PD.ProductID = I.ProductID
    WHERE PD.Status = 'Sold'
    GROUP BY PC.ProductType, PD.ProductID, P.Product
) AS SalesData
ORDER BY Category, SalesRank;

-- fixed version of query 1
-- this query ranks products (based on their sales total) within their product categories. it calculates total revenue from invoices where product was sold, and assigns a rank inside each product type. so for each category you’ll see which products sold the most.


SELECT 
    Category,
    ProductID,
    ProductName,
    TotalSales,
    RANK() OVER (PARTITION BY Category ORDER BY TotalSales DESC) AS SalesRank
FROM (
    SELECT 
        PC.ProductType AS Category,
        PD.ProductID,
        PC.Product AS ProductName,
        SUM(I.FinalSellerPayout) AS TotalSales
    FROM ProductDetails PD
    INNER JOIN ProductConfiguration PC ON PD.ConfigurationID = PC.ConfigurationID
    INNER JOIN Invoice I ON PD.ProductID = I.ProductID
    WHERE PD.Status = 'Sold'
    GROUP BY PC.ProductType, PD.ProductID, PC.Product
) AS SalesData
ORDER BY Category, SalesRank;

-- wrong gpt query 2
-- gpt made this error by adding SUM(...) OVER (...) window function for total wins even though we were already grouping by user. this caused redundancy and possible confusion in output — I fixed it by removing the extra OVER line since we already count total wins using COUNT(DISTINCT ...).

SELECT 
    U.UserID,
    U.Name,
    U.Email,
    COUNT(DISTINCT A.AuctionID) AS TotalAuctionsParticipated,
    COUNT(DISTINCT CASE WHEN B.isWinningBid = TRUE THEN A.AuctionID ELSE NULL END) AS AuctionsWon,
    AVG(B.BidAmount) AS AverageBidAmount,
    MAX(B.BidAmount) AS MaxBidAmount,
    MIN(B.BidAmount) AS MinBidAmount,
    SUM(CASE WHEN B.isWinningBid = TRUE THEN 1 ELSE 0 END) OVER (PARTITION BY U.UserID) AS TotalWins
FROM User U
INNER JOIN Bid B ON U.UserID = B.UserID
INNER JOIN Auction A ON B.AuctionID = A.AuctionID
GROUP BY U.UserID, U.Name, U.Email
ORDER BY TotalAuctionsParticipated DESC, TotalWins DESC, AverageBidAmount DESC;

-- corrected version of query 2
-- this query shows per-user auction stats — how many auctions they participated in, how many they won, their average, max, and min bid. sorted by most active and most successful users.

SELECT 
    U.UserID,
    U.Name,
    U.Email,
    COUNT(DISTINCT A.AuctionID) AS TotalAuctionsParticipated,
    COUNT(DISTINCT CASE WHEN B.isWinningBid = TRUE THEN A.AuctionID ELSE NULL END) AS AuctionsWon,
    AVG(B.BidAmount) AS AverageBidAmount,
    MAX(B.BidAmount) AS MaxBidAmount,
    MIN(B.BidAmount) AS MinBidAmount
FROM User U
INNER JOIN Bid B ON U.UserID = B.UserID
INNER JOIN Auction A ON B.AuctionID = A.AuctionID
GROUP BY U.UserID, U.Name, U.Email
ORDER BY TotalAuctionsParticipated DESC, AuctionsWon DESC, AverageBidAmount DESC;
