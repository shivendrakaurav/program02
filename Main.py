from cred import MysqlClass
from work.cred.search_functions import SearchController

if __name__ == "__main__":
    while True:
        try:
            operation_to_perform = input("Enter one of the operation between <SEARCH> <UPDATE> <INSERT > <DELETE> <EXIT> >")

            calling = MysqlClass()

            if operation_to_perform.upper() == "SEARCH" :
                search_object = SearchController()
                search_type = input("Enter the type of search: <startswith> <endswith> <contain> <id>  <date_after>  <date_before> <date_between>")
                calling.search(search_type.lower())


                if search_type == "endswith":
                     search_object.search_object.endswith()

                elif search_type == "startswith":
                     search_object.search_object.startswith()
                elif search_type == "contain":
                     search_object.search_object.contain()
                elif search_type =="id":
                     search_object.search_object.id()
                elif search_type == "date_after":
                    search_object.search_object.date_after()
                elif search_type == "date_before":
                     search_object.search_object.date_before()
                elif search_type == "date_between":
                     search_object.search_object.date_between()
                else:
                    print(f"unknown command {search_type}")

                
            elif  operation_to_perform.upper() == "DELETE":
                calling.delete()
                
            elif  operation_to_perform.upper() == "INSERT":
                calling.insert()

            elif  operation_to_perform.upper() == "UPDATE":
                calling.update()

            elif operation_to_perform.upper() == "EXIT":
                break

            else:
                print(f'Unknown command, {operation_to_perform}')
                
        except Exception as e1:
            print("Generic error: {0}".format(e1))