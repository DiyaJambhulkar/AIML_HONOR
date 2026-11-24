


import pandas as pd
import pymysql

connection = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='Diya@2007',
    database='employee'
)
query = "SELECT * FROM employee"
result = pd.read_sql(query, connection)
print(result)
average_salary = result['salary'].mean()
print(average_salary)
pd.write_sql("INSERT INTO employee (name, salary) VALUES ('John Doe', 50000)", connection, index=False)