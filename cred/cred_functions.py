
from MysqlDatabase import MysqlDatabasename
from search_functions import  MysqlClass_for_search


class MysqlClass(MysqlDatabasename):

    def __init__(self):
        super().__init__()
        self.search_object = MysqlClass_for_search()

    def delete(self):
        cust_id = int(input("Enter the id of customer >"))

        self.mycursor.execute(f"DELETE FROM customers WHERE cust_id = {cust_id}")
        self.mydb.commit()
       
        print(self.mycursor.rowcount, "record(s) deleted")
        

        if self.mycursor.rowcount == 0:
            raise Exception(f"Fail to remove customer having id = {cust_id}")
        else:
             print(self.mycursor.rowcount, "record(s) deleted")


    def insert(self):
        
        inserting_values_list = tuple(input("Enter customers values in format:<customer id  > <customer name > <customer phone > <customer date of purchase>").split(" "))
        sql = "INSERT INTO customers (cust_id, cust_name, cust_phone_no, cust_purchase_date) VALUES (%s, %s,%s, %s)"
        val = inserting_values_list
        self.mycursor.execute(sql, val)
        self.mydb.commit()

        print(self.mycursor.rowcount, "record inserted.")

    def update(self):
        updating_values_list = list(input("Enter customers update values in format:<customer id  primary key> <name of column to update >  <value of updated column>").split(" "))
        updating_values_list[0] = int(updating_values_list[0])
        self.mycursor.execute(f"UPDATE customers SET {updating_values_list[1]} = '{updating_values_list[2]}' WHERE cust_id = {updating_values_list[0]}")
        self.mydb.commit()

        if self.mycursor.rowcount==1:
            print(self.mycursor.rowcount, "record(s) updated")
        else:
            raise Exception(f"Fail to update customer having id = {updating_values_list[0]}")


    def search(self,search_type):
        if search_type == "endswith":
            self.search_object.endswith()
        elif search_type == "startswith":
            self.search_object.startswith()
        elif search_type == "contain":
            self.search_object.contain()
        elif search_type =="id":
            self.search_object.id()
        elif search_type == "date_after":
           self.search_object.date_after()
        elif search_type == "date_before":
            self.search_object.date_before()
        elif search_type == "date_between":
            self.search_object.date_between()
        else:
            print(f"unknown command {search_type}")

        