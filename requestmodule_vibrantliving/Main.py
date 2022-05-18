from egoclient import Egoclient
import sys
from egoclient import validate_args


if __name__ == "__main__":
    
    # try:       
        validate_args(sys.argv)
        if sys.argv[1].lower() == "list_items":
            a = Egoclient()
            print(a.list_items())
        else:
            credentials = input("Enter credentials: <phone number> <password>").split(" ")
            if len(credentials) !=2:
                raise Exception("Entered credentials are not given in above format")
            a = Egoclient(credentials[0], credentials[1])
            

            if sys.argv[1].lower() =="cart_details" :
                print(a.cart_details()) 
            elif  sys.argv[1].lower() =="add_to_cart":
                print(a.add_to_cart()) 
            else:
                print(a.list_subscriptions()) 
    # except Exception as e1:
    #     print(f"Generic error : {e1}")