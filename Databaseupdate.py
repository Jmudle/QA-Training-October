import pyodbc

cs = r'DRIVER={ODBC Driver 17 for SQL Server};SERVER=MIS;DATABASE=qastore;Trusted_Connection=yes'

queryStr = """INSERT INTO company
VALUES (5000, 'Mr Mann Menswear', '0784578320', 'London', 'LO1 1PT');"""

queryStr2 = """UPDATE company
SET company_name = 'Mrs Mann Womenswear'
WHERE company_no = 5000;"""

#def dbQuery(add):
    #conn = pyodbc.connect(cs)
    #cur = conn.cursor()
    #cur.execute(queryStr)

    #conn.commit()

    #conn.close()

def dbQuery(update):
    conn = pyodbc.connect(cs)
    cur = conn.cursor()
    cur.execute(queryStr2)

    conn.commit()

    conn.close