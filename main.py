
import mysql.connector as msql

db = msql.connect(
    host="localhost",
    user="lewis",
    password="Redstreet@50",
    db="sampledb"
)
cursor = db.cursor()
#cursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
cursor.execute("SELECT * FROM customers")
myresult = cursor.fetchall()
cursor.close()
for x in myresult:
    print(x)