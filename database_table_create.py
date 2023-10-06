import pyodbc

cs = r'DRIVER={ODBC Driver 17 for SQL Server};SERVER=MIS;DATABASE=qastore;Trusted_Connection=yes'

querystrc = """CREATE TABLE student (
    PersonID int,
    Lastname varchar(255),
    Firstname varchar(255),
    Address varchar(255),
    City varchar(255)
    );"""

def dbQuery(createtable):
    conn = pyodbc.connect(cs)
    cur = conn.cursor()
    cur.execute(createtable)
    
    conn.commit()
    conn.close()

dbQuery(querystrc)