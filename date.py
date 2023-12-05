import mysql.connector

import datetime

date = datetime.datetime.now().strftime('%Y-%m-%d')
print(date)
conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Illusiondb')
cursor = conn.cursor()
cursor.execute("SELECT * FROM regtb1 WHERE id=1 AND '2022-12-09' between sdate and edate" )
data = cursor.fetchone()
if data:
    print("exit")

else:
    print("No-exit")

