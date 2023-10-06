import pyodbc

connectionString = r'DRIVER={ODBC Driver 17 for SQL Server};SERVER=MIS;DATABASE=qastore;Trusted_Connection=yes'



def dbQuery(query):
    conn = pyodbc.connect(connectionString)
    cur = conn.cursor()
    result = cur.execute(query).fetchall()
    conn.close()
    return result

#result = dbQuery("SELECT * FROM salesperson ORDER BY salary DESC")#
result = dbQuery("SELECT * FROM company WHERE county = 'London'")

for row in result:
    print(row)