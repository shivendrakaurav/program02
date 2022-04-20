from cred import*
class MysqlClass(MysqlDatabasename):
    def __init__(self):
        print(f"cusror:{self.mycursor}")
    def delete(self):
        cust_id = int(input("Enter the id of customer >"))

        self.mycursor.execute(f"DELETE FROM customers WHERE cust_id = {cust_id}")
        mydb.commit()
        #if mycursor.rowcount>0:
        #    print(mycursor.rowcount, "record(s) deleted")
        #else:
        #    print(f"No data availale with cust_id :{cust_id}, therefore no data is deleted ")

        if mycursor.rowcount != 0:
            raise Exception(f"Fail to remove customer having id = {cust_id}")


    def insert(self):
        
        inserting_values_list = tuple(input("Enter customers values in format:<customer id  primary key> <customer name > <customer phone no unique key> <customer date of purchase>").split(" "))
        sql = "INSERT INTO customers (cust_id, cust_name, cust_phone_no, cust_purchase_date) VALUES (%s, %s,%s, %s)"
        val = inserting_values_list
        mycursor.execute(sql, val)
        mydb.commit()

        print(mycursor.rowcount, "record inserted.")

    def update(self):
        updating_values_list = list(input("Enter customers update values in format:<customer id  primary key> <name of column to update >  <value of updated column>").split(" "))
        updating_values_list[0] = int(updating_values_list[0])
        mycursor.execute(f"UPDATE customers SET {updating_values_list[1]} = '{updating_values_list[2]}' WHERE cust_id = {updating_values_list[0]}")
        mydb.commit()

        if mycursor.rowcount>0:
            print(mycursor.rowcount, "record(s) updated")
        else:
            print(f"No data availale with cust_id :{updating_values_list[0]} or column name '{updating_values_list[1]}' therefore cannot be updated")




    # def search(self,search_type):
    #     if search_type == "endswith":
    #         endswith()
    #     if search_type == "startswith":
    #         startswith()
    #     if search_type == "contain":
    #         contain()
    #     if search_type =="id":
    #         id()
    #     if search_type == "date_after":
    #         date_after()
    #     if search_type == "date_before":
    #         date_before()
    #     if search_type == "date_between":
    #         date_between()

        