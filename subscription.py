from subscription_class import Egoclient

if __name__ == "__main__":
    try:
        a = Egoclient()
        a.login('vltest1@gmail.com','Test@1234')
        a.i
        print(a.post())

    except Exception as e1:
        print(f"Generic error as : {e1}")