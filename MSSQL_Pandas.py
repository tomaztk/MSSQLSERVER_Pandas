'''
Author: Tomaz Kastrun
Date: 12.07.2018

get data from sql server to pandas
get data from pandas data frame to sql server database

'''

## From SQL to DataFrame Pandas

import pandas as pd
import pyodbc

sql_conn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER=SQLSERVER2017;DATABASE=Adventureworks;Trusted_Connection=yes') 
query = "SELECT [BusinessEntityID],[FirstName],[LastName],[PostalCode],[City] FROM [Sales].[vSalesPerson]"
df = pd.read_sql(query, sql_conn)

df.head(3)


## From DataFrame Pandas to SQL

'''
Have table prepared ON Microsoft SQL Server

USE AdventureWorks;
GO

DROP TABLE IF EXISTS vSalesPerson_test

CREATE TABLE vSalesPerson_test
(
 [BusinessEntityID] INT
,[FirstName] VARCHAR(50)
,[LastName] VARCHAR(100)
)


'''
connStr = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER=SQLSERVER2017;DATABASE=Adventureworks;Trusted_Connection=yes')
cursor = connStr.cursor()

for index,row in df.iterrows():
    cursor.execute("INSERT INTO dbo.vSalesPerson_test([BusinessEntityID],[FirstName],[LastName]) values (?, ?,?)", row['BusinessEntityID'], row['FirstName'] , row['LastName']) 
    connStr.commit()
cursor.close()
connStr.close()