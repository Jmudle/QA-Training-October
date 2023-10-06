import pyodbc

cs = r'DRIVER={ODBC Driver 17 for SQL Server};SERVER=MIS;DATABASE=qastore;Trusted_Connection=yes'

queryadd = """INSERT INTO student
VALUES (00002, 'Davidson', 'Oscar', '14 River Way', 'Sheffield'),
(00003, 'Peterson', 'Ragnar', '35 Sea Bank', 'Manchester');"""

queryupdate = """UPDATE student
SET Firstname = 'Steven'
WHERE PersonID = 00003;"""

#def dbQuery(add):
    #conn = pyodbc.connect(cs)
    #cur = conn.cursor()
    #cur.execute(add)

    #conn.commit()

    #conn.close()

#dbQuery(queryadd)

def dbQuery(update):
    conn = pyodbc.connect(cs)
    cur = conn.cursor()
    cur.execute(update)

    conn.commit()

    conn.close()

dbQuery(queryupdate)
    