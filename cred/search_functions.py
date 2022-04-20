import mysql.connector
from cred import *


mydb = mysql.connector.connect(
host="localhost",
user="root",
password="shivendrasingh",
database="customer"
)
mycursor = mydb.cursor()





def read_table(column_name, operator,patterns):

    mycursor.execute(f"SELECT * FROM customers WHERE {column_name} {operator} '{patterns}' ")
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)


def endswith():
    list_input = list(input("Enter search details in this format: <column name> <ending charachter>").split(" "))
    pattern = "%" + list_input[1]
    read_table(list_input[0] , "LIKE" , pattern)


def startswith():
    list_input = list(input("Enter search details in this format: <column name> <ending charachter>").split(" "))
    pattern =   list_input[1] +"%"
    read_table(list_input[0] , "LIKE" , pattern)

def contain():
    list_input = list(input("Enter search details in this format: <column name> <ending charachter>").split(" "))
    pattern =   "%"  +list_input[1] +"%"
    read_table(list_input[0] , "LIKE" , pattern)

def id():
    list_input = list(input("Enter search details in this format: <column name> <id>").split(" "))
    mycursor.execute(f"SELECT * FROM customers WHERE {list_input[0]} = {int(list_input[1])} ")
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

def date_after():
    list_input = list(input("Enter search details in this format: <column name> <date after which  data is to fetch>").split(" "))
    read_table(list_input[0] , ">" , list_input[1])

def date_before():
    list_input = list(input("Enter search details in this format: <column name> <date from which before data is to fetch>").split(" "))
    read_table(list_input[0] , "<" , list_input[1])

def date_between():
    list_input = list(input("Enter search details in this format: <column name> <starting date> <ending date>").split(" "))
    mycursor.execute(f"SELECT * FROM customers WHERE {list_input[0]} BETWEEN '{list_input[1]}' and '{list_input[2]}' ")
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)


