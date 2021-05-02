# Using Microsoft SQL SQLSERVER with Python Pandas

Using Python Pandas dataframe to read and insert data to Microsoft SQL Server


## Cloning the repository
You can follow the steps below to clone the repository.
```
git clone -n https://github.com/tomaztk/MSSQLSERVER_Pandas.git
```


## Quickstart from Microsoft SQL Server

1.  Clone the repository
2.  Get connection to your SQL Server 2017+
3.  Start using MSSQL Server with Python Pandas

<!-- end list -->

``` sql

```


## Quickstart from Python IDE

1. Clone the repository
2. Open Python IDE
3. Enjoy


<!-- end list -->

``` python
import pandas as pd
import pyodbc

sql_conn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER=SQLSERVER2017;DATABASE=master;Trusted_Connection=yes') 
query = "SELECT * FROM sys.tables"
df = pd.read_sql(query, sql_conn)

df.head(3)
```
