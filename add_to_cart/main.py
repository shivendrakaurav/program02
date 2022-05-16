from add_to_cart_class import Egoclient
import sys
from add_to_cart_class import validate_args


if __name__ == "__main__":
    
    # try:       
        validate_args(sys.argv)
        a = Egoclient()

        if sys.argv[1] == "add_to_cart":
            credentials = input("Enter phone number and  : <phone no > <password>").split(" ")

            if len(credentials) !=2:
                raise Exception("Enter credentials are not given in above format")

            else :
                print(a.add_to_cart(credentials[0], credentials[1]))

    # except Exception as e1:
    #     print(f"Generic error : {e1}")