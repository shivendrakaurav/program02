import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="shivendrasingh",
  database="football"
)

mycursor = mydb.cursor()

sql = "DELETE FROM players WHERE Age = 23"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")