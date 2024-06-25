CREATE TABLE table_m3 (
    invoice_id TEXT, 
    branch CHAR(1) CHECK (branch IN ('A', 'B', 'C')),
    city VARCHAR(50),
    customer_type VARCHAR(10) CHECK (customer_type IN ('Member', 'Normal')),
    gender VARCHAR(10) CHECK (gender IN ('Male', 'Female')),
    product_line VARCHAR(50) CHECK (product_line IN ('Electronic accessories', 'Fashion accessories', 'Food and beverages', 'Health and beauty', 'Home and lifestyle', 'Sports and travel')),
    unit_price NUMERIC(10, 2),
    quantity INTEGER,
    tax NUMERIC(10, 2),
    total NUMERIC(10, 2),
    date DATE,
    time TIME,
    payment VARCHAR(15) CHECK (payment IN ('Cash', 'Credit card', 'Ewallet')),
    cogs NUMERIC(10, 2), 
    gross_margin_percentage NUMERIC(5, 2),
    gross_income NUMERIC(10, 2),
    rating FLOAT
);
-- generate for the created dataset and link to PyBook
COPY table_m3
FROM 'C:\Program Files\PostgreSQL\16\P2M3_Daffa_Darwin_data_raw.csv'
DELIMITER','
CSV HEADER;

-- generate the table that has been created above
SELECT * FROM table_m3 

-- for delete the mistakes of column creation
DROP TABLE table_m3