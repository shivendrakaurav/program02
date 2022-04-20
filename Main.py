from cred import *

if __name__ == "__main__":
    while True:
        try:
            operation_to_perform = input("Enter one of the operation between <SEARCH> <UPDATE> <INSERT > <DELETE> <EXIT> >")

            calling = MysqlClass()

            if operation_to_perform.upper() == "SEARCH" :
                search_type = input("Enter the type of search: <startswith> <endswith> <contain> <id>  <date_after>  <date_before> <date_between>")
                search(search_type.lower())
                
            elif  operation_to_perform.upper() == "DELETE":
                delete()
                
            elif  operation_to_perform.upper() == "INSERT":
                insert()

            elif  operation_to_perform.upper() == "UPDATE":
                update()
            elif operation_to_perform.upper() == "EXIT":
                break
            else:
                print(f'Unknown command, {operation_to_perform}')
                
        except Exception as e1:
            print("Generic error: {0}".format(e1))