# Using Microsoft SQL SQLSERVER with Python Pandas

Using **Python Pandas** dataframe to read and insert data to **Microsoft SQL Server**.

<img src="img/mssqlserver.png" align="left" width="400" />
<img src="img/pandas.png"  width="240" />

<br />


## Cloning the repository
You can follow the steps below to clone the repository.
```
git clone  https://github.com/tomaztk/MSSQLSERVER_Pandas.git
```


## Quickstart from Microsoft SQL Server

1.  Clone the repository
2.  Get connection to your SQL Server 2017+
3.  Start using MSSQL Server with Python Pandas

<!-- end list -->

``` sql
-- sample table
SELECT TOP 10 
   name
  ,object_id
FROM sys.tables


EXECUTE sp_execute_external_script @language = N'Python'
      ,@script = N'
      import pandas as pd
      OutputDataSet = pd.DataFrame(InputDataSet);
      '
      , @input_data_1 = N'SELECT TOP 10 name,object_id FROM sys.tables'
WITH RESULT SETS((
        [Name] VARCHAR(150) NOT NULL
       ,[object_ID] CHAR(20) NOT NULL
         ));

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
