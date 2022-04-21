import mysql.connector
class MysqlDatabasename:
    def __init__(self):
        self.mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="shivendrasingh",
        database="customer"
        )

        self.mycursor = self.mydb.cursor()
