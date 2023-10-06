import pyodbc

cs = r'DRIVER={ODBC Driver 17 for SQL Server};SERVER=MIS;DATABASE=qastore;Trusted_Connection=yes'

with open('studentinfo.csv', 'r') as file1:
    result = file1.readlines()

for line in result:
    query = line.split(',')
    sqlStr = f"""INSERT INTO student
    VALUES ('{int(query[0])}', '{query[1]}', '{query[2]}', '{query[3]}', '{query[4]}')"""
    conn = pyodbc.connect(cs)
    cur = conn.cursor()
    cur.execute(sqlStr)
    conn.commit()
    conn.close()

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

#def dbQuery(update):
   # conn = pyodbc.connect(cs)
    #cur = conn.cursor()
    #cur.execute(update)

    #conn.commit()

    #conn.close()

#dbQuery(queryupdate)
    