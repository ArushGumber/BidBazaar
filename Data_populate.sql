-- ------------------------------
-- -- 1. Insert 20 additional Users (IDs 11 to 30)
-- ------------------------------
-- INSERT INTO User (UserID, Name, Email, Phone, Password, Address, isBlocked) VALUES
-- (11, 'Rahul Iyer', 'rahul.iyer@example.com', '9100000011', 'pass11', 'Bangalore, India', FALSE),
-- (12, 'Meera Nair', 'meera.nair@example.com', '9100000012', 'pass12', 'Kochi, India', FALSE),
-- (13, 'Siddharth Rao', 'siddharth.rao@example.com', '9100000013', 'pass13', 'Hyderabad, India', FALSE),
-- (14, 'Aisha Khan', 'aisha.khan@example.com', '9100000014', 'pass14', 'Jaipur, India', TRUE),
-- (15, 'Vikram Patel', 'vikram.patel@example.com', '9100000015', 'pass15', 'Surat, India', FALSE),
-- (16, 'Priya Reddy', 'priya.reddy@example.com', '9100000016', 'pass16', 'Vijayawada, India', FALSE),
-- (17, 'Ananya Roy', 'ananya.roy@example.com', '9100000017', 'pass17', 'Kolkata, India', FALSE),
-- (18, 'Kabita Das', 'kabita.das@example.com', '9100000018', 'pass18', 'Guwahati, India', FALSE),
-- (19, 'Rohan Khanna', 'rohan.khanna@example.com', '9100000019', 'pass19', 'Delhi, India', FALSE),
-- (20, 'Neha Gupta', 'neha.gupta@example.com', '9100000020', 'pass20', 'Mumbai, India', FALSE),
-- (21, 'Arnav Malhotra', 'arnav.malhotra@example.com', '9100000021', 'pass21', 'Chennai, India', FALSE),
-- (22, 'Sonia Mehra', 'sonia.mehra@example.com', '9100000022', 'pass22', 'Pune, India', FALSE),
-- (23, 'Manish Chawla', 'manish.chawla@example.com', '9100000023', 'pass23', 'Jaipur, India', FALSE),
-- (24, 'Kavya Sharma', 'kavya.sharma@example.com', '9100000024', 'pass24', 'Lucknow, India', FALSE),
-- (25, 'Harshad Joshi', 'harshad.joshi@example.com', '9100000025', 'pass25', 'Indore, India', FALSE),
-- (26, 'Ishaan Verma', 'ishaan.verma@example.com', '9100000026', 'pass26', 'Bhopal, India', FALSE),
-- (27, 'Pooja Aggarwal', 'pooja.aggarwal@example.com', '9100000027', 'pass27', 'Amritsar, India', FALSE),
-- (28, 'Vineet Kapoor', 'vineet.kapoor@example.com', '9100000028', 'pass28', 'Gurgaon, India', FALSE),
-- (29, 'Aditi Singh', 'aditi.singh@example.com', '9100000029', 'pass29', 'Noida, India', FALSE),
-- (30, 'Rakesh Patel', 'rakesh.patel@example.com', '9100000030', 'pass30', 'Vadodara, India', FALSE);

-- ------------------------------
-- -- 2. Insert 20 additional ProductConfiguration rows (IDs 11 to 30)
-- ------------------------------
-- INSERT INTO ProductConfiguration (ConfigurationID, Created, ProductType, Product) VALUES
-- (11, '2025-02-01 08:00:00', 'Electronics', 'Smartwatch'),
-- (12, '2025-02-01 08:30:00', 'Fashion', 'Handbag'),
-- (13, '2025-02-02 09:00:00', 'Books', 'Cookbook'),
-- (14, '2025-02-02 09:30:00', 'Home Appliances', 'Vacuum Cleaner'),
-- (15, '2025-02-03 10:00:00', 'Automotive', 'Car Stereo'),
-- (16, '2025-02-03 10:30:00', 'Electronics', 'Drone'),
-- (17, '2025-02-04 11:00:00', 'Fashion', 'Sunglasses'),
-- (18, '2025-02-04 11:30:00', 'Books', 'Biography'),
-- (19, '2025-02-05 12:00:00', 'Home Appliances', 'Air Purifier'),
-- (20, '2025-02-05 12:30:00', 'Automotive', 'GPS Tracker'),
-- (21, '2025-02-06 13:00:00', 'Electronics', 'Camera'),
-- (22, '2025-02-06 13:30:00', 'Fashion', 'Perfume'),
-- (23, '2025-02-07 14:00:00', 'Books', 'Graphic Novel'),
-- (24, '2025-02-07 14:30:00', 'Home Appliances', 'Microwave'),
-- (25, '2025-02-08 15:00:00', 'Automotive', 'Tire Inflator'),
-- (26, '2025-02-08 15:30:00', 'Electronics', 'Bluetooth Speaker'),
-- (27, '2025-02-09 16:00:00', 'Fashion', 'Jacket'),
-- (28, '2025-02-09 16:30:00', 'Books', 'Mystery Novel'),
-- (29, '2025-02-10 17:00:00', 'Home Appliances', 'Coffee Maker'),
-- (30, '2025-02-10 17:30:00', 'Automotive', 'Car Charger');

-- ------------------------------
-- -- 3. Insert 20 additional ProductDetails rows (ProductIDs 111 to 130)
-- ------------------------------
-- INSERT INTO ProductDetails (ProductID, ConfigurationID, LatestAuctionStatus, WinningBidID, BuyerID, Status) VALUES
-- (111, 11, 'Open',   NULL, NULL, 'Available'),
-- (112, 12, 'Open',   NULL, NULL, 'Available'),
-- (113, 13, 'Closed', 215, 12, 'Sold'),
-- (114, 14, 'Open',   NULL, NULL, 'Available'),
-- (115, 15, 'Open',   NULL, NULL, 'Available'),
-- (116, 16, 'Open',   NULL, NULL, 'Available'),
-- (117, 17, 'Closed', 218, 14, 'Sold'),
-- (118, 18, 'Open',   NULL, NULL, 'Available'),
-- (119, 19, 'Open',   NULL, NULL, 'Available'),
-- (120, 20, 'Closed', 220, 15, 'Sold'),
-- (121, 21, 'Open',   NULL, NULL, 'Available'),
-- (122, 22, 'Open',   NULL, NULL, 'Available'),
-- (123, 23, 'Closed', 223, 16, 'Sold'),
-- (124, 24, 'Open',   NULL, NULL, 'Available'),
-- (125, 25, 'Open',   NULL, NULL, 'Available'),
-- (126, 26, 'Open',   NULL, NULL, 'Available'),
-- (127, 27, 'Closed', 227, 17, 'Sold'),
-- (128, 28, 'Open',   NULL, NULL, 'Available'),
-- (129, 29, 'Open',   NULL, NULL, 'Available'),
-- (130, 30, 'Closed', 230, 18, 'Sold');

-- ------------------------------
-- -- 4. Insert 20 additional ProductInventory rows (for ProductIDs 111 to 130)
-- ------------------------------
-- INSERT INTO ProductInventory (ProductID, PickupAddress, PickupDateTime, AmountForSeller, DeliveryAddress, DeliveryDate, Status, SellerReceiptID, BuyerReceiptID) VALUES
-- (111, 'Bangalore, India',     '2025-02-02 08:15:00', 220.00, 'Kochi, India',      '2025-02-05 10:30:00', 'Pending', 1101, NULL),
-- (112, 'Kochi, India',         '2025-02-02 09:00:00', 180.00, 'Hyderabad, India',   '2025-02-06 11:00:00', 'Pending', NULL, NULL),
-- (113, 'Hyderabad, India',      '2025-02-03 09:15:00', 310.00, 'Bangalore, India',   '2025-02-07 12:00:00', 'Shipped', 1102, 2102),
-- (114, 'Jaipur, India',         '2025-02-03 09:45:00', 130.00, 'Surat, India',       '2025-02-08 13:00:00', 'Pending', NULL, NULL),
-- (115, 'Surat, India',          '2025-02-04 10:00:00', 190.00, 'Kochi, India',       '2025-02-09 14:00:00', 'Pending', NULL, NULL),
-- (116, 'Vijayawada, India',     '2025-02-04 10:30:00', 260.00, 'Chennai, India',     '2025-02-10 15:00:00', 'Pending', NULL, NULL),
-- (117, 'Kolkata, India',        '2025-02-05 11:00:00', 280.00, 'Bangalore, India',   '2025-02-11 15:30:00', 'Shipped', 1103, 2103),
-- (118, 'Guwahati, India',       '2025-02-05 11:30:00', 200.00, 'Kochi, India',       '2025-02-12 16:00:00', 'Pending', NULL, NULL),
-- (119, 'Delhi, India',          '2025-02-06 12:00:00', 330.00, 'Hyderabad, India',   '2025-02-13 16:30:00', 'Pending', NULL, NULL),
-- (120, 'Mumbai, India',         '2025-02-06 12:30:00', 410.00, 'Jaipur, India',      '2025-02-14 17:00:00', 'Shipped', 1104, 2104),
-- (121, 'Chennai, India',        '2025-02-07 13:00:00', 240.00, 'Surat, India',       '2025-02-15 17:30:00', 'Pending', NULL, NULL),
-- (122, 'Pune, India',           '2025-02-07 13:30:00', 190.00, 'Vijayawada, India',  '2025-02-16 18:00:00', 'Pending', NULL, NULL),
-- (123, 'Jaipur, India',         '2025-02-08 14:00:00', 320.00, 'Kolkata, India',     '2025-02-17 18:30:00', 'Shipped', 1105, 2105),
-- (124, 'Lucknow, India',        '2025-02-08 14:30:00', 140.00, 'Guwahati, India',    '2025-02-18 19:00:00', 'Pending', NULL, NULL),
-- (125, 'Indore, India',         '2025-02-09 15:00:00', 210.00, 'Delhi, India',       '2025-02-19 19:30:00', 'Pending', NULL, NULL),
-- (126, 'Bhopal, India',         '2025-02-09 15:30:00', 230.00, 'Mumbai, India',      '2025-02-20 20:00:00', 'Pending', NULL, NULL),
-- (127, 'Amritsar, India',       '2025-02-10 16:00:00', 290.00, 'Chennai, India',     '2025-02-21 20:30:00', 'Shipped', 1106, 2106),
-- (128, 'Gurgaon, India',        '2025-02-10 16:30:00', 210.00, 'Pune, India',        '2025-02-22 21:00:00', 'Pending', NULL, NULL),
-- (129, 'Noida, India',          '2025-02-11 17:00:00', 340.00, 'Jaipur, India',      '2025-02-23 21:30:00', 'Pending', NULL, NULL),
-- (130, 'Vadodara, India',       '2025-02-11 17:30:00', 420.00, 'Chandigarh, India',  '2025-02-24 22:00:00', 'Shipped', 1107, 2107);

-- ------------------------------
-- -- 5. Insert 20 additional Auction rows (AuctionIDs 11 to 30)
-- ------------------------------
-- INSERT INTO Auction (AuctionID, ProductID, UserID, AuctionStartTime, AuctionEndTime, AuctionStatus, AuctionType, SnippingFlag, AuctionBasePrice, NegotiationEnabled) VALUES
-- (11, 111, 11, '2025-02-02 08:00:00', '2025-02-02 11:00:00', 'Closed', 'Standard', FALSE, 220.00, TRUE),
-- (12, 112, 12, '2025-02-02 08:30:00', '2025-02-02 11:30:00', 'Open',   'Standard', FALSE, 180.00, FALSE),
-- (13, 113, 13, '2025-02-03 09:00:00', '2025-02-03 12:00:00', 'Closed', 'Standard', FALSE, 225.00, TRUE),
-- (14, 114, 14, '2025-02-03 09:30:00', '2025-02-03 12:30:00', 'Open',   'Standard', FALSE, 130.00, FALSE),
-- (15, 115, 15, '2025-02-04 10:00:00', '2025-02-04 13:00:00', 'Closed', 'Standard', FALSE, 190.00, TRUE),
-- (16, 116, 16, '2025-02-04 10:30:00', '2025-02-04 13:30:00', 'Open',   'Standard', FALSE, 260.00, FALSE),
-- (17, 117, 17, '2025-02-05 11:00:00', '2025-02-05 14:00:00', 'Closed', 'Standard', FALSE, 280.00, TRUE),
-- (18, 118, 18, '2025-02-05 11:30:00', '2025-02-05 14:30:00', 'Open',   'Standard', FALSE, 200.00, FALSE),
-- (19, 119, 19, '2025-02-06 12:00:00', '2025-02-06 15:00:00', 'Closed', 'Standard', FALSE, 330.00, TRUE),
-- (20, 120, 20, '2025-02-06 12:30:00', '2025-02-06 15:30:00', 'Open',   'Standard', FALSE, 410.00, FALSE),
-- (21, 121, 21, '2025-02-07 13:00:00', '2025-02-07 16:00:00', 'Closed', 'Standard', FALSE, 240.00, TRUE),
-- (22, 122, 22, '2025-02-07 13:30:00', '2025-02-07 16:30:00', 'Open',   'Standard', FALSE, 190.00, FALSE),
-- (23, 123, 23, '2025-02-08 14:00:00', '2025-02-08 17:00:00', 'Closed', 'Standard', FALSE, 320.00, TRUE),
-- (24, 124, 24, '2025-02-08 14:30:00', '2025-02-08 17:30:00', 'Open',   'Standard', FALSE, 140.00, FALSE),
-- (25, 125, 25, '2025-02-09 15:00:00', '2025-02-09 18:00:00', 'Closed', 'Standard', FALSE, 210.00, TRUE),
-- (26, 126, 26, '2025-02-09 15:30:00', '2025-02-09 18:30:00', 'Open',   'Standard', FALSE, 230.00, FALSE),
-- (27, 127, 27, '2025-02-10 16:00:00', '2025-02-10 19:00:00', 'Closed', 'Standard', FALSE, 290.00, TRUE),
-- (28, 128, 28, '2025-02-10 16:30:00', '2025-02-10 19:30:00', 'Open',   'Standard', FALSE, 210.00, FALSE),
-- (29, 129, 29, '2025-02-11 17:00:00', '2025-02-11 20:00:00', 'Closed', 'Standard', FALSE, 340.00, TRUE),
-- (30, 130, 30, '2025-02-11 17:30:00', '2025-02-11 20:30:00', 'Open',   'Standard', FALSE, 420.00, FALSE);

-- ------------------------------
-- -- 6. Insert 20 additional Bid rows (BidIDs 210 to 229)
-- ------------------------------
-- INSERT INTO Bid (BidID, AuctionID, ProductID, UserID, BidTimestamp, BidAmount, isWinningBid, WinTimestamp, isAutoBid) VALUES
-- (210, 11, 111, 12, '2025-02-02 08:15:00', 230.00, TRUE,  '2025-02-02 11:00:00', TRUE),
-- (211, 12, 112, 13, '2025-02-02 08:45:00', 190.00, FALSE, NULL, FALSE),
-- (212, 13, 113, 14, '2025-02-03 09:15:00', 235.00, TRUE,  '2025-02-03 12:00:00', TRUE),
-- (213, 14, 114, 15, '2025-02-03 09:45:00', 135.00, FALSE, NULL, FALSE),
-- (214, 15, 115, 16, '2025-02-04 10:15:00', 195.00, TRUE,  '2025-02-04 13:00:00', TRUE),
-- (215, 16, 116, 17, '2025-02-04 10:45:00', 265.00, FALSE, NULL, FALSE),
-- (216, 17, 117, 18, '2025-02-05 11:15:00', 285.00, TRUE,  '2025-02-05 14:00:00', TRUE),
-- (217, 18, 118, 19, '2025-02-05 11:45:00', 205.00, FALSE, NULL, FALSE),
-- (218, 19, 119, 20, '2025-02-06 12:15:00', 335.00, TRUE,  '2025-02-06 15:00:00', TRUE),
-- (219, 20, 120, 21, '2025-02-06 12:45:00', 415.00, FALSE, NULL, FALSE),
-- (220, 21, 121, 22, '2025-02-07 13:15:00', 245.00, TRUE,  '2025-02-07 16:00:00', TRUE),
-- (221, 22, 122, 23, '2025-02-07 13:45:00', 195.00, FALSE, NULL, FALSE),
-- (222, 23, 123, 24, '2025-02-08 14:15:00', 325.00, TRUE,  '2025-02-08 17:00:00', TRUE),
-- (223, 24, 124, 25, '2025-02-08 14:45:00', 145.00, FALSE, NULL, FALSE),
-- (224, 25, 125, 26, '2025-02-09 15:15:00', 215.00, TRUE,  '2025-02-09 18:00:00', TRUE),
-- (225, 26, 126, 27, '2025-02-09 15:45:00', 235.00, FALSE, NULL, FALSE),
-- (226, 27, 127, 28, '2025-02-10 16:15:00', 295.00, TRUE,  '2025-02-10 19:00:00', TRUE),
-- (227, 28, 128, 29, '2025-02-10 16:45:00', 215.00, FALSE, NULL, FALSE),
-- (228, 29, 129, 30, '2025-02-11 17:15:00', 345.00, TRUE,  '2025-02-11 20:00:00', TRUE),
-- (229, 30, 130, 11, '2025-02-11 17:45:00', 425.00, FALSE, NULL, FALSE);

-- ------------------------------
-- -- 7. Insert AutoBid rows for selected new bids (10 rows)
-- ------------------------------
-- INSERT INTO AutoBid (BidID, StartingBid, MaxBid, StepRate) VALUES
-- (210, 220.00, 250.00, 5.00),
-- (212, 230.00, 260.00, 5.00),
-- (214, 185.00, 215.00, 5.00),
-- (216, 275.00, 305.00, 5.00),
-- (218, 325.00, 355.00, 5.00),
-- (220, 405.00, 435.00, 5.00),
-- (222, 235.00, 265.00, 5.00),
-- (224, 205.00, 235.00, 5.00),
-- (226, 285.00, 315.00, 5.00),
-- (228, 335.00, 365.00, 5.00);

-- ------------------------------
-- -- 8. Insert 20 additional Invoice rows (InvoiceIDs 1007 to 1026)
-- ------------------------------
-- INSERT INTO Invoice (InvoiceID, BuyerID, SellerID, ReceiptID, ProductID, CreatedTimestamp, SellerAmount, ServiceRate, FinalSellerPayout, BuyerPayout, InvoiceStatus) VALUES
-- (1007, 11, 12, 1007, 113, '2025-02-04 10:00:00', 235.00, 15.00, 220.00, 240.00, 'Paid'),
-- (1008, 13, 14, 1008, 117, '2025-02-05 11:00:00', 285.00, 20.00, 265.00, 300.00, 'Paid'),
-- (1009, 15, 16, 1009, 115, '2025-02-04 11:00:00', 190.00, 10.00, 180.00, 200.00, 'Paid'),
-- (1010, 17, 18, 1010, 123, '2025-02-08 14:15:00', 325.00, 18.00, 310.00, 340.00, 'Paid'),
-- (1011, 19, 20, 1011, 119, '2025-02-06 12:15:00', 330.00, 22.00, 308.00, 350.00, 'Paid'),
-- (1012, 21, 22, 1012, 121, '2025-02-07 13:15:00', 240.00, 12.00, 228.00, 250.00, 'Paid'),
-- (1013, 23, 24, 1013, 123, '2025-02-08 14:30:00', 320.00, 15.00, 305.00, 335.00, 'Paid'),
-- (1014, 25, 26, 1014, 125, '2025-02-09 15:00:00', 210.00, 10.00, 200.00, 220.00, 'Paid'),
-- (1015, 27, 28, 1015, 127, '2025-02-10 16:00:00', 290.00, 20.00, 270.00, 300.00, 'Paid'),
-- (1016, 29, 30, 1016, 129, '2025-02-11 17:00:00', 340.00, 25.00, 315.00, 360.00, 'Paid'),
-- (1017, 11, 12, 1017, 113, '2025-02-04 10:30:00', 235.00, 15.00, 220.00, 240.00, 'Paid'),
-- (1018, 13, 14, 1018, 117, '2025-02-05 11:30:00', 285.00, 20.00, 265.00, 300.00, 'Paid'),
-- (1019, 15, 16, 1019, 115, '2025-02-04 11:30:00', 190.00, 10.00, 180.00, 200.00, 'Paid'),
-- (1020, 17, 18, 1020, 123, '2025-02-08 14:45:00', 325.00, 18.00, 310.00, 340.00, 'Paid'),
-- (1021, 19, 20, 1021, 119, '2025-02-06 12:45:00', 330.00, 22.00, 308.00, 350.00, 'Paid'),
-- (1022, 21, 22, 1022, 121, '2025-02-07 13:45:00', 240.00, 12.00, 228.00, 250.00, 'Paid'),
-- (1023, 23, 24, 1023, 123, '2025-02-08 15:00:00', 320.00, 15.00, 305.00, 335.00, 'Paid'),
-- (1024, 25, 26, 1024, 125, '2025-02-09 15:30:00', 210.00, 10.00, 200.00, 220.00, 'Paid'),
-- (1025, 27, 28, 1025, 127, '2025-02-10 16:30:00', 290.00, 20.00, 270.00, 300.00, 'Paid'),
-- (1026, 29, 30, 1026, 129, '2025-02-11 17:30:00', 340.00, 25.00, 315.00, 360.00, 'Paid');

-- ------------------------------
-- -- 9. Insert 20 additional ProductAttributes rows (for ProductIDs 111 to 130)
-- ------------------------------
-- INSERT INTO ProductAttributes (ProductID, AttributeName, AttributeValue) VALUES
-- (111, 'material', 'aluminum'),
-- (112, 'color', 'red'),
-- (113, 'size', 'M'),
-- (114, 'weight', '1.2kg'),
-- (115, 'battery', '3000mAh'),
-- (116, 'screen', '8-inch'),
-- (117, 'durability', 'high'),
-- (118, 'style', 'modern'),
-- (119, 'design', 'sleek'),
-- (120, 'capacity', '256GB'),
-- (121, 'resolution', '1080p'),
-- (122, 'speed', 'fast'),
-- (123, 'power', '90W'),
-- (124, 'temperature', '350°F'),
-- (125, 'voltage', '220V'),
-- (126, 'frequency', '60Hz'),
-- (127, 'length', '15cm'),
-- (128, 'width', '7cm'),
-- (129, 'height', '2cm'),
-- (130, 'depth', '0.5cm');





INSERT INTO User (UserID, Name, Email, Phone, Password, Address, isBlocked) VALUES
(1, 'Alice Johnson', 'alice.johnson@example.com', '1234567890', 'password1', '123 Maple St, Cityville', FALSE),
(2, 'Bob Smith', 'bob.smith@example.com', '1234567891', 'password2', '456 Oak Ave, Townsville', FALSE),
(3, 'Carol Williams', 'carol.williams@example.com', '1234567892', 'password3', '789 Pine Rd, Villageville', FALSE),
(4, 'David Brown', 'david.brown@example.com', '1234567893', 'password4', '321 Birch St, Hamletville', FALSE),
(5, 'Evelyn Davis', 'evelyn.davis@example.com', '1234567894', 'password5', '654 Cedar Ave, Metropolis', FALSE),
(6, 'Frank Miller', 'frank.miller@example.com', '1234567895', 'password6', '987 Spruce Rd, Smalltown', FALSE),
(7, 'Grace Wilson', 'grace.wilson@example.com', '1234567896', 'password7', '159 Elm St, Bigcity', FALSE),
(8, 'Henry Moore', 'henry.moore@example.com', '1234567897', 'password8', '753 Willow Ave, Uptown', FALSE),
(9, 'Isabella Taylor', 'isabella.taylor@example.com', '1234567898', 'password9', '357 Fir Rd, Downtown', FALSE),
(10, 'Jack Anderson', 'jack.anderson@example.com', '1234567899', 'password10', '951 Palm St, Suburbia', FALSE),
(11, 'Katherine Thomas', 'katherine.thomas@example.com', '1234567800', 'password11', '258 Aspen Ave, Riverside', FALSE),
(12, 'Liam Jackson', 'liam.jackson@example.com', '1234567801', 'password12', '369 Redwood Rd, Lakeside', FALSE),
(13, 'Mia White', 'mia.white@example.com', '1234567802', 'password13', '147 Dogwood St, Hilltop', FALSE),
(14, 'Noah Harris', 'noah.harris@example.com', '1234567803', 'password14', '258 Magnolia Ave, Bayview', FALSE),
(15, 'Olivia Martin', 'olivia.martin@example.com', '1234567804', 'password15', '369 Cherry Rd, Forestville', FALSE),
(16, 'Paul Lee', 'paul.lee@example.com', '1234567805', 'password16', '159 Peach St, Valleyview', FALSE),
(17, 'Quinn Perez', 'quinn.perez@example.com', '1234567806', 'password17', '753 Plum Ave, Cliffside', FALSE),
(18, 'Rachel Clark', 'rachel.clark@example.com', '1234567807', 'password18', '357 Lime Rd, Seaside', FALSE),
(19, 'Samuel Lewis', 'samuel.lewis@example.com', '1234567808', 'password19', '951 Lemon St, Brookside', FALSE),
(20, 'Tina Walker', 'tina.walker@example.com', '1234567809', 'password20', '147 Orange Ave, Crestview', FALSE);

INSERT INTO ProductConfiguration (ConfigurationID, Created, ProductType, Product) VALUES
-- Electronics (ConfigurationIDs 1-5)
(1, '2025-03-01 10:00:00', 'Electronics', 'Smartphone'),
(2, '2025-03-01 10:05:00', 'Electronics', 'Laptop'),
(3, '2025-03-01 10:10:00', 'Electronics', 'Tablet'),
(4, '2025-03-01 10:15:00', 'Electronics', 'Smartwatch'),
(5, '2025-03-01 10:20:00', 'Electronics', 'Camera'),

-- Home Appliances (ConfigurationIDs 6-10)
(6, '2025-03-01 11:00:00', 'Home Appliances', 'Refrigerator'),
(7, '2025-03-01 11:05:00', 'Home Appliances', 'Microwave Oven'),
(8, '2025-03-01 11:10:00', 'Home Appliances', 'Washing Machine'),
(9, '2025-03-01 11:15:00', 'Home Appliances', 'Air Conditioner'),
(10, '2025-03-01 11:20:00', 'Home Appliances', 'Dishwasher'),

-- Vehicle (ConfigurationIDs 11-15)
(11, '2025-03-01 12:00:00', 'Vehicle', 'Car'),
(12, '2025-03-01 12:05:00', 'Vehicle', 'Motorcycle'),
(13, '2025-03-01 12:10:00', 'Vehicle', 'Truck'),
(14, '2025-03-01 12:15:00', 'Vehicle', 'Bus'),
(15, '2025-03-01 12:20:00', 'Vehicle', 'SUV');

INSERT INTO ProductDetails (ProductID, ConfigurationID, LatestAuctionStatus, WinningBidID, BuyerID, Status) VALUES
-- Electronics (ProductIDs 201-205)
(201, 1, 'Completed', 501, 1001, 'Sold'),
(202, 2, 'Active', NULL, NULL, 'Available'),
(203, 3, 'Completed', 502, 1002, 'Sold'),
(204, 4, 'Cancelled', NULL, NULL, 'Not Available'),
(205, 5, 'Active', NULL, NULL, 'Available'),

-- Home Appliances (ProductIDs 206-210)
(206, 6, 'Completed', 503, 1003, 'Sold'),
(207, 7, 'Active', NULL, NULL, 'Available'),
(208, 8, 'Active', NULL, NULL, 'Available'),
(209, 9, 'Completed', 504, 1004, 'Sold'),
(210, 10, 'Cancelled', NULL, NULL, 'Not Available'),

-- Vehicle (ProductIDs 211-215)
(211, 11, 'Active', NULL, NULL, 'Available'),
(212, 12, 'Completed', 505, 1005, 'Sold'),
(213, 13, 'Cancelled', NULL, NULL, 'Not Available'),
(214, 14, 'Active', NULL, NULL, 'Available'),
(215, 15, 'Completed', 506, 1006, 'Sold');

-- ATTRIBUTES
INSERT INTO ProductAttributes (ProductID, AttributeName, AttributeValue) VALUES
-- Electronics (ProductIDs 201-205)
-- Product 201: Smartphone
(201, 'RAM', '4GB'),
(201, 'Storage', '64GB'),

-- Product 202: Laptop
(202, 'Processor', 'Intel i5'),
(202, 'RAM', '8GB'),

-- Product 203: Tablet
(203, 'Screen Size', '10 inches'),
(203, 'Battery', '5000mAh'),

-- Product 204: Smartwatch
(204, 'Strap', 'Leather'),
(204, 'Display', '1.5 inches'),

-- Product 205: Camera
(205, 'Resolution', '20MP'),
(205, 'Lens Type', 'Wide Angle'),

-- Home Appliances (ProductIDs 206-210)
-- Product 206: Refrigerator
(206, 'Capacity', '350L'),
(206, 'Energy Rating', '4 Star'),

-- Product 207: Microwave Oven
(207, 'Power', '900W'),
(207, 'Capacity', '20L'),

-- Product 208: Washing Machine
(208, 'Load Capacity', '7kg'),
(208, 'Type', 'Front Load'),

-- Product 209: Air Conditioner
(209, 'BTU', '12000'),
(209, 'Energy Star', 'Yes'),

-- Product 210: Dishwasher
(210, 'Wash Programs', '6'),
(210, 'Capacity', '12 Place'),

-- Vehicle (ProductIDs 211-215)
-- Product 211: Car
(211, 'Engine Type', 'Petrol'),
(211, 'Fuel Efficiency', '15 km/l'),

-- Product 212: Motorcycle
(212, 'Engine Capacity', '150cc'),
(212, 'Type', 'Sports'),

-- Product 213: Truck
(213, 'Payload', '5 Tons'),
(213, 'Axles', '2'),

-- Product 214: Bus
(214, 'Seating Capacity', '50'),
(214, 'Length', '12m'),

-- Product 215: SUV
(215, 'Drivetrain', '4WD'),
(215, 'Ground Clearance', '220mm');


INSERT INTO Invoice (InvoiceID, BuyerID, SellerID, ReceiptID, ProductID, CreatedTimestamp, SellerAmount, ServiceRate, FinalSellerPayout, BuyerPayout, InvoiceStatus) VALUES
-- Invoice for ProductID 201
(1001, 2, 10, 1001, 201, '2025-03-02 10:00:00', 500.00, 20.00, 480.00, 520.00, 'Paid'),
-- Invoice for ProductID 203
(1002, 3, 11, 1002, 203, '2025-03-02 11:00:00', 750.00, 25.00, 725.00, 775.00, 'Paid'),
-- Invoice for ProductID 206
(1003, 4, 12, 1003, 206, '2025-03-02 12:00:00', 600.00, 30.00, 570.00, 630.00, 'Paid'),
-- Invoice for ProductID 209
(1004, 5, 13, 1004, 209, '2025-03-02 13:00:00', 650.00, 35.00, 615.00, 680.00, 'Paid'),
-- Invoice for ProductID 212
(1005, 6, 14, 1005, 212, '2025-03-02 14:00:00', 800.00, 40.00, 760.00, 840.00, 'Paid'),
-- Invoice for ProductID 215
(1006, 7, 15, 1006, 215, '2025-03-02 15:00:00', 900.00, 45.00, 855.00, 945.00, 'Paid');


INSERT INTO ProductInventory (ProductID, PickupAddress, PickupDateTime, AmountForSeller, DeliveryAddress, DeliveryDate, Status, SellerReceiptID, BuyerReceiptID) VALUES
-- Product 201 (Sold)
(201, '123 Main St, City A', '2025-03-03 10:00:00', 500.00, '456 Elm St, City B', '2025-03-04 12:00:00', 'Delivered', 2001, 3001),
-- Product 202 (Available)
(202, '789 Oak St, City C', '2025-03-03 11:00:00', 700.00, '321 Pine St, City D', '2025-03-05 13:00:00', 'Pending', NULL, NULL),
-- Product 203 (Sold)
(203, '654 Maple Ave, City E', '2025-03-03 12:00:00', 550.00, '987 Birch Ave, City F', '2025-03-04 14:00:00', 'Delivered', 2002, 3002),
-- Product 204 (Not Available)
(204, '159 Cedar St, City G', '2025-03-03 13:00:00', 0.00, '753 Walnut St, City H', '2025-03-04 15:00:00', 'Cancelled', NULL, NULL),
-- Product 205 (Available)
(205, '357 Spruce Rd, City I', '2025-03-03 14:00:00', 600.00, '951 Willow Rd, City J', '2025-03-05 16:00:00', 'Pending', NULL, NULL),
-- Product 206 (Sold)
(206, '246 Hickory St, City K', '2025-03-03 15:00:00', 650.00, '135 Sycamore St, City L', '2025-03-04 17:00:00', 'Delivered', 2003, 3003),
-- Product 207 (Available)
(207, '864 Aspen St, City M', '2025-03-03 16:00:00', 720.00, '753 Poplar St, City N', '2025-03-05 18:00:00', 'Pending', NULL, NULL),
-- Product 208 (Available)
(208, '159 Fir St, City O', '2025-03-03 17:00:00', 730.00, '357 Redwood St, City P', '2025-03-05 19:00:00', 'Pending', NULL, NULL),
-- Product 209 (Sold)
(209, '951 Chestnut St, City Q', '2025-03-03 18:00:00', 680.00, '246 Dogwood St, City R', '2025-03-04 20:00:00', 'Delivered', 2004, 3004),
-- Product 210 (Not Available)
(210, '753 Cypress St, City S', '2025-03-03 19:00:00', 0.00, '159 Magnolia St, City T', '2025-03-04 21:00:00', 'Cancelled', NULL, NULL),
-- Product 211 (Available)
(211, '357 Juniper St, City U', '2025-03-03 20:00:00', 800.00, '951 Palm St, City V', '2025-03-05 22:00:00', 'Pending', NULL, NULL),
-- Product 212 (Sold)
(212, '864 Alder St, City W', '2025-03-03 21:00:00', 850.00, '753 Bamboo St, City X', '2025-03-04 23:00:00', 'Delivered', 2005, 3005),
-- Product 213 (Not Available)
(213, '159 Olive St, City Y', '2025-03-03 22:00:00', 0.00, '357 Pineapple St, City Z', '2025-03-04 23:30:00', 'Cancelled', NULL, NULL),
-- Product 214 (Available)
(214, '951 Lemon St, City AA', '2025-03-03 23:00:00', 900.00, '246 Lime St, City BB', '2025-03-05 23:45:00', 'Pending', NULL, NULL),
-- Product 215 (Sold)
(215, '753 Mango St, City CC', '2025-03-04 00:00:00', 950.00, '159 Papaya St, City DD', '2025-03-05 00:30:00', 'Delivered', 2006, 3006);


INSERT INTO Auction (AuctionID, ProductID, UserID, AuctionStartTime, AuctionEndTime, AuctionStatus, AuctionType, SnippingFlag, AuctionBasePrice, NegotiationEnabled) VALUES
-- For ProductID 201 (Sold: Inventory=500.00, Invoice=500.00)
(301, 201, 10, '2025-03-03 09:00:00', '2025-03-03 12:00:00', 'Closed', 'English', FALSE, 500.00, FALSE),
-- For ProductID 202 (Available: Inventory=700.00)
(302, 202, 11, '2025-03-03 10:00:00', '2025-03-03 13:00:00', 'Open', 'English', FALSE, 700.00, TRUE),
-- For ProductID 203 (Sold: Inventory=550.00, Invoice=550.00)
(303, 203, 12, '2025-03-03 11:00:00', '2025-03-03 14:00:00', 'Closed', 'English', FALSE, 550.00, TRUE),
-- For ProductID 204 (Not Available: Inventory=0.00)
(304, 204, 13, '2025-03-03 12:00:00', '2025-03-03 15:00:00', 'Cancelled', 'English', FALSE, 0.00, FALSE),
-- For ProductID 205 (Available: Inventory=600.00)
(305, 205, 14, '2025-03-03 13:00:00', '2025-03-03 16:00:00', 'Open', 'English', FALSE, 600.00, TRUE),
-- For ProductID 206 (Sold: Inventory=650.00, Invoice=650.00)
(306, 206, 15, '2025-03-03 14:00:00', '2025-03-03 17:00:00', 'Closed', 'English', FALSE, 650.00, TRUE),
-- For ProductID 207 (Available: Inventory=720.00)
(307, 207, 16, '2025-03-03 15:00:00', '2025-03-03 18:00:00', 'Open', 'English', FALSE, 720.00, TRUE),
-- For ProductID 208 (Available: Inventory=730.00)
(308, 208, 17, '2025-03-03 16:00:00', '2025-03-03 19:00:00', 'Open', 'English', FALSE, 730.00, TRUE),
-- For ProductID 209 (Sold: Inventory=680.00, Invoice=680.00)
(309, 209, 18, '2025-03-03 17:00:00', '2025-03-03 20:00:00', 'Closed', 'English', FALSE, 680.00, TRUE),
-- For ProductID 210 (Not Available: Inventory=0.00)
(310, 210, 19, '2025-03-03 18:00:00', '2025-03-03 21:00:00', 'Cancelled', 'English', FALSE, 0.00, FALSE),
-- For ProductID 211 (Available: Inventory=800.00)
(311, 211, 20, '2025-03-03 19:00:00', '2025-03-03 22:00:00', 'Open', 'English', FALSE, 800.00, TRUE),
-- For ProductID 212 (Sold: Inventory=850.00, Invoice=850.00)
(312, 212, 2,  '2025-03-03 20:00:00', '2025-03-03 23:00:00', 'Closed', 'English', FALSE, 850.00, TRUE),
-- For ProductID 213 (Not Available: Inventory=0.00)
(313, 213, 3,  '2025-03-03 21:00:00', '2025-03-04 00:00:00', 'Cancelled', 'English', FALSE, 0.00, FALSE),
-- For ProductID 214 (Available: Inventory=900.00)
(314, 214, 4,  '2025-03-03 22:00:00', '2025-03-04 01:00:00', 'Open', 'English', FALSE, 900.00, TRUE),
-- For ProductID 215 (Sold: Inventory=950.00, Invoice=950.00)
(315, 215, 5,  '2025-03-03 23:00:00', '2025-03-04 02:00:00', 'Closed', 'English', FALSE, 950.00, TRUE);



-- Insert multiple bids for each auction/product.
-- Auction table details (AuctionIDs 301 to 315) have been defined earlier.
-- Note: Timestamps, amounts, and UserIDs are chosen so that the winning bid for sold products matches the invoice's BuyerID.
INSERT INTO Bid (BidID, AuctionID, ProductID, UserID, BidTimestamp, BidAmount, isWinningBid, WinTimestamp, isAutoBid) VALUES
-- For Product 201 (AuctionID 301, Seller=10, Invoice Buyer=2)
(401, 301, 201, 4, '2025-03-03 09:15:00', 480.00, FALSE, NULL, FALSE),
(402, 301, 201, 2, '2025-03-03 09:30:00', 500.00, TRUE, '2025-03-03 11:00:00', TRUE),
(403, 301, 201, 8, '2025-03-03 09:45:00', 490.00, FALSE, NULL, FALSE),

-- For Product 202 (AuctionID 302, Seller=11, Available so no winner)
(404, 302, 202, 3, '2025-03-03 10:15:00', 680.00, FALSE, NULL, FALSE),
(405, 302, 202, 5, '2025-03-03 10:30:00', 700.00, FALSE, NULL, TRUE),
(406, 302, 202, 6, '2025-03-03 10:45:00', 690.00, FALSE, NULL, FALSE),

-- For Product 203 (AuctionID 303, Seller=12, Invoice Buyer=3)
(407, 303, 203, 7, '2025-03-03 11:15:00', 530.00, FALSE, NULL, FALSE),
(408, 303, 203, 3, '2025-03-03 11:30:00', 550.00, TRUE, '2025-03-03 12:00:00', TRUE),
(409, 303, 203, 8, '2025-03-03 11:45:00', 540.00, FALSE, NULL, FALSE),

-- For Product 204 (AuctionID 304, Seller=13, Cancelled so no sale)
(410, 304, 204, 2, '2025-03-03 12:15:00', 100.00, FALSE, NULL, FALSE),
(411, 304, 204, 4, '2025-03-03 12:30:00', 110.00, FALSE, NULL, TRUE),
(412, 304, 204, 6, '2025-03-03 12:45:00', 105.00, FALSE, NULL, FALSE),

-- For Product 205 (AuctionID 305, Seller=14, Available)
(413, 305, 205, 7, '2025-03-03 13:15:00', 580.00, FALSE, NULL, FALSE),
(414, 305, 205, 8, '2025-03-03 13:30:00', 600.00, FALSE, NULL, TRUE),
(415, 305, 205, 9, '2025-03-03 13:45:00', 590.00, FALSE, NULL, FALSE),

-- For Product 206 (AuctionID 306, Seller=15, Invoice Buyer=4)
(416, 306, 206, 2, '2025-03-03 14:15:00', 630.00, FALSE, NULL, FALSE),
(417, 306, 206, 4, '2025-03-03 14:30:00', 650.00, TRUE, '2025-03-03 17:00:00', TRUE),
(418, 306, 206, 5, '2025-03-03 14:45:00', 640.00, FALSE, NULL, FALSE),

-- For Product 207 (AuctionID 307, Seller=16, Available)
(419, 307, 207, 3, '2025-03-03 15:15:00', 710.00, FALSE, NULL, FALSE),
(420, 307, 207, 4, '2025-03-03 15:30:00', 720.00, FALSE, NULL, TRUE),
(421, 307, 207, 8, '2025-03-03 15:45:00', 715.00, FALSE, NULL, FALSE),

-- For Product 208 (AuctionID 308, Seller=17, Available)
(422, 308, 208, 2, '2025-03-03 16:15:00', 720.00, FALSE, NULL, FALSE),
(423, 308, 208, 9, '2025-03-03 16:30:00', 730.00, FALSE, NULL, TRUE),
(424, 308, 208, 10, '2025-03-03 16:45:00', 725.00, FALSE, NULL, FALSE),

-- For Product 209 (AuctionID 309, Seller=18, Invoice Buyer=5)
(425, 309, 209, 7, '2025-03-03 17:15:00', 660.00, FALSE, NULL, FALSE),
(426, 309, 209, 5, '2025-03-03 17:30:00', 680.00, TRUE, '2025-03-03 20:00:00', TRUE),
(427, 309, 209, 8, '2025-03-03 17:45:00', 670.00, FALSE, NULL, FALSE),

-- For Product 210 (AuctionID 310, Seller=19, Cancelled)
(428, 310, 210, 2, '2025-03-03 18:15:00', 0.00, FALSE, NULL, FALSE),
(429, 310, 210, 4, '2025-03-03 18:30:00', 0.00, FALSE, NULL, TRUE),
(430, 310, 210, 8, '2025-03-03 18:45:00', 0.00, FALSE, NULL, FALSE),

-- For Product 211 (AuctionID 311, Seller=20, Available)
(431, 311, 211, 3, '2025-03-03 19:15:00', 780.00, FALSE, NULL, FALSE),
(432, 311, 211, 5, '2025-03-03 19:30:00', 800.00, FALSE, NULL, TRUE),
(433, 311, 211, 6, '2025-03-03 19:45:00', 790.00, FALSE, NULL, FALSE),

-- For Product 212 (AuctionID 312, Seller=2, Invoice Buyer=6)
(434, 312, 212, 7, '2025-03-03 20:15:00', 830.00, FALSE, NULL, FALSE),
(435, 312, 212, 6, '2025-03-03 20:30:00', 850.00, TRUE, '2025-03-03 23:00:00', TRUE),
(436, 312, 212, 8, '2025-03-03 20:45:00', 840.00, FALSE, NULL, FALSE),

-- For Product 213 (AuctionID 313, Seller=3, Cancelled)
(437, 313, 213, 2, '2025-03-03 21:15:00', 0.00, FALSE, NULL, FALSE),
(438, 313, 213, 4, '2025-03-03 21:30:00', 0.00, FALSE, NULL, TRUE),
(439, 313, 213, 8, '2025-03-03 21:45:00', 0.00, FALSE, NULL, FALSE),

-- For Product 214 (AuctionID 314, Seller=4, Available)
(440, 314, 214, 7, '2025-03-03 22:15:00', 880.00, FALSE, NULL, FALSE),
(441, 314, 214, 5, '2025-03-03 22:30:00', 900.00, FALSE, NULL, TRUE),
(442, 314, 214, 6, '2025-03-03 22:45:00', 890.00, FALSE, NULL, FALSE),

-- For Product 215 (AuctionID 315, Seller=5, Invoice Buyer=7)
(443, 315, 215, 2, '2025-03-03 23:15:00', 930.00, FALSE, NULL, FALSE),
(444, 315, 215, 7, '2025-03-03 23:30:00', 950.00, TRUE, '2025-03-04 02:00:00', TRUE),
(445, 315, 215, 8, '2025-03-03 23:45:00', 940.00, FALSE, NULL, FALSE);


INSERT INTO AutoBid (BidID, StartingBid, MaxBid, StepRate) VALUES
(402, 490.00, 520.00, 5.00),
(405, 680.00, 710.00, 5.00),
(408, 540.00, 560.00, 5.00),
(411, 100.00, 120.00, 5.00),
(414, 580.00, 610.00, 5.00),
(417, 640.00, 660.00, 5.00),
(420, 710.00, 730.00, 5.00),
(423, 720.00, 740.00, 5.00),
(426, 670.00, 700.00, 5.00),
(429, 0.00, 0.00, 0.00),
(432, 780.00, 810.00, 5.00),
(435, 830.00, 860.00, 5.00),
(438, 0.00, 0.00, 0.00),
(441, 880.00, 910.00, 5.00),
(444, 930.00, 970.00, 5.00);