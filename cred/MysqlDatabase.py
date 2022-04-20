import mysql.connector
from cred import *

class MysqlDatabasename:
    def __init__(self):
        print(f"in inheritance")
        self.mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="shivendrasingh",
        database="customer"
        )
        self.mycursor = mydb.cursor()
