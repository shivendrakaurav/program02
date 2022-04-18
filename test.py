import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="shivendrasingh",
#   database="customer"
# )

# mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE customers (Cust_Id INT AUTO_INCREMENT PRIMARY KEY, Cust_Name VARCHAR(255), Cust_Phone_No INT UNIQUE KEY, Cust_address VARCHAR(255), Cust_Purchase_date DATE)")
class MysqlClass:

    # def __init__(self):
    #     #  conn = mysql.connector.connect(host="Host",user="RRR",password="123",database="RRR")
    #     #  self.mycursor = conn.cursor()
    #     print(id(self))

    # def insert(id,name,age,rollno):
    #     self.mycursor("insert into table values(101,)")
    #     return "one entry inserted"
    def void(self):
        print("sivendru")

my = MysqlClass()
my.void()



