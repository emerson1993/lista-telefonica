CREATE DATABASE ListaTelefonicaDB;
USE ListaTelefonicaDB;
CREATE TABLE IF NOT EXISTS db_tkinterphonelist.tbl_ContactList (
IdContact INT(11) NOT NULL AUTO_INCREMENT,
ContactName VARCHAR(100) NOT NULL,
PhoneNumber VARCHAR(12) NOT NULL,
PRIMARY KEY (IdContact));
SELECT DATABASE();
SELECT*FROM tbl_ContactList;