# Apache-Airflow-Project
This project, an engineering platform developed during a bootcamp focused on Data Structures, will be updated in real time. Updates are scheduled for every Friday at 6:30 AM.

# SQL Parts
In this section, the query language is created to fetch the data that will be linked to Python-- which the query looks like below:

```
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
```

# Directed Acyclic Graph
This section contains the Directed Acyclic Graph, which outlines the data cleaning process scheduled at specific times.

# Great Expectations
While the dataset has been established, the purpose of this section is to verify if the dataset contains valid data that supports the overall dataset. 

# Kibana & Elasticsearch
Kibana and Elasticsearch are similar to Tableau, but these tools are integrated with Docker for visualization deployment.

# Docker 
Since this project is using Airflow, this platform provides a place to create, deploy, and run applications in containers. These containers are like mini virtual machines, but more lightweight. They contain everything an application needs to run, making it easy to move applications between different environments while ensuring they will still work as expected. In this case, where the Directed Acyclic Graph and Great Expectations are placed in Docker. 
