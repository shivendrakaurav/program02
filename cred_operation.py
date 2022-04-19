import mysql.connector

def delete():
    cust_id = int(input("Enter the id of customer >"))

    mycursor.execute(f"DELETE FROM customers WHERE cust_id = {cust_id}")
    mydb.commit()
    if mycursor.rowcount>0:
        print(mycursor.rowcount, "record(s) deleted")
    else:
        print(f"No data availale with cust_id :{cust_id}, therefore no data is deleted ")


def insert():
    
    inserting_values_list = tuple(input("Enter customers values in format:<customer id  primary key> <customer name > <customer phone no unique key> <customer date of purchase>").split(" "))
    sql = "INSERT INTO customers (cust_id, cust_name, cust_phone_no, cust_purchase_date) VALUES (%s, %s,%s, %s)"
    val = inserting_values_list
    mycursor.execute(sql, val)
    mydb.commit()

    print(mycursor.rowcount, "record inserted.")

def update():
    updating_values_list = list(input("Enter customers update values in format:<customer id  primary key> <name of column to update >  <value of updated column>").split(" "))
    updating_values_list[0] = int(updating_values_list[0])
    mycursor.execute(f"UPDATE customers SET {updating_values_list[1]} = '{updating_values_list[2]}' WHERE cust_id = {updating_values_list[0]}")
    mydb.commit()

    if mycursor.rowcount>0:
        print(mycursor.rowcount, "record(s) updated")
    else:
        print(f"No data availale with cust_id :{updating_values_list[0]} or column name '{updating_values_list[1]}' therefore cannot be updated")



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
    list_input = list(input("Enter search details in this format: <column name> <idr>").split(" "))
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




def search(search_type):
    if search_type == "endswith":
        endswith()
    if search_type == "startswith":
        startswith()
    if search_type == "contain":
        contain()
    if search_type =="id":
        id()
    if search_type == "date_after":
        date_after()
    if search_type == "date_before":
        date_before()
    if search_type == "date_between":
        date_between()

    




def main():
    while True: 
        operation_to_perform = input("Enter one of the operation between <SEARCH> <UPDATE> <INSERT > <DELETE> >")

        if operation_to_perform.upper() == "SEARCH" :
            search_type = input("Enter the type of search: <startswith> <endswith> <contain> <id>  <date_after>  <date_before> <date_between>")
            search(search_type.lower())
            
        if  operation_to_perform.upper() == "DELETE":
            delete()
            
        if  operation_to_perform.upper() == "INSERT":
            insert()

        if  operation_to_perform.upper() == "UPDATE":
            update()
    

        
        if input("Type 'Y' to continue the operation else 'N' >") == "N":
            break



mydb = mysql.connector.connect(
host="localhost",
user="root",
password="shivendrasingh",
database="customer"
)
mycursor = mydb.cursor()


if __name__ == "__main__":
    try:
        main()


    except Exception as e1:
        print("Generic error: {0}".format(e1))