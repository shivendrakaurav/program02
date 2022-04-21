from MysqlDatabase import MysqlDatabasename

class SearchController(MysqlDatabasename):

    def __init__(self):
        super().__init__()

    def read_table(self,column_name, operator,patterns):

        self.mycursor.execute(f"SELECT * FROM customers WHERE {column_name} {operator} '{patterns}' ")
        myresult = self.mycursor.fetchall()

        for x in myresult:
            print(x)


    def endswith(self):
        list_input = list(input("Enter search details in this format: <column name> <ending charachter>").split(" "))
        pattern = "%" + list_input[1]
        self.read_table(list_input[0] , "LIKE" , pattern)


    def startswith(self):
        list_input = list(input("Enter search details in this format: <column name> <ending charachter>").split(" "))
        pattern =   list_input[1] +"%"
        self.read_table(list_input[0] , "LIKE" , pattern)

    def contain(self):
        list_input = list(input("Enter search details in this format: <column name> <ending charachter>").split(" "))
        pattern =   "%"  +list_input[1] +"%"
        self.read_table(list_input[0] , "LIKE" , pattern)

    def id(self):
        list_input = list(input("Enter search details in this format: <column name> <id>").split(" "))
        self.mycursor.execute(f"SELECT * FROM customers WHERE {list_input[0]} = {int(list_input[1])} ")
        myresult = self.mycursor.fetchall()

        for x in myresult:
            print(x)

    def date_after(self):
        list_input = list(input("Enter search details in this format: <column name> <date after which  data is to fetch>").split(" "))
        self.read_table(list_input[0] , ">" , list_input[1])

    def date_before(self):
        list_input = list(input("Enter search details in this format: <column name> <date from which before data is to fetch>").split(" "))
        self.read_table(list_input[0] , "<" , list_input[1])

    def date_between(self):
        list_input = list(input("Enter search details in this format: <column name> <starting date> <ending date>").split(" "))
        self.mycursor.execute(f"SELECT * FROM customers WHERE {list_input[0]} BETWEEN '{list_input[1]}' and '{list_input[2]}' ")
        myresult = self.mycursor.fetchall()

        for x in myresult:
            print(x)


