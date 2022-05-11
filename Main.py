from login_class import Egoclient
import sys
from login_class import validate_args


if __name__ == "__main__":
    
    try:
    
        validate_args(sys.argv)
        a = Egoclient()

        if sys.argv[1] == "subscription":
            credentials = input("Enter id and password: <id> <password>").split(" ")

            if len(credentials) !=2:
                raise Exception("Enter credentials are not given in above format")

            a.login(credentials[0], credentials[1])
            # print(credentials[0])


        elif sys.argv[1] == "list_items":
            print(a.list_items())

    except Exception as e1:
        # raise e1
        print(f"Generic error : {e1}")