import site

from cryptography.fernet import Fernet


class PasswordManager:


    def __init__(self):
        self.key = None
        self.password_file = None
        self.password_dict = {}

    def create_key(self, path):
        self.key = Fernet.generate_key()
        with open (path, "wb") as f:
            f.write(self.key)

    def load_key(self,path):
        with open (path, "rb") as f:
            self.key = f.read()


    def create_password_file(self, path, initial_values=None):
        self.password_file = path

        if initial_values is not None:
            for key, value in initial_values.items():
                self.add_password(key, value)

    def load_password_file(self,path):
        self.password_file = path


        with open(path, 'r')as f:
            for line in f:
                site, encrypted = line.split(":")
                sef.password_dict[site] = Fernet(self.key).decrypt(encrypted.encode()).decoded

    def add_password(self, site, password):
        self.password_dict[site] = password

        if self.password_file is not None:
            with open(self.password_file, "a+") as f:
                encrypted = Fernet(self.key).encrypt(password.encode())
                f.write(site + ":" + encrypted.decode() + "\n")

    def get_password(self, site):
        return self.password_dict[site]


def main():
    password ={
        "email": "1234567",
        "password": "myfbpassword",
        "youtube": "helloworld123",
        "something": "myfavoritepassword_123"
    }

    pm = PasswordManager()

    print("""What do you want to do ?
    (1) Create a new key 
    (2) Load an existing key
    (3) Create new password_file
    (4) Load existing password file
    (5) Add a new password
    (6) Get a password
    (q) Quit 
    """)

    done = False
    while not done:

        Choice = input("enter your choice: ")
        if Choice == "1":
            path = input("enter path: ")
            pm.create_key(path)
        elif Choice == "2":
            path = input("enter path: ")
            pm.load_key(path)
        elif Choice == "3":
            path = input("enter path: ")
            pm.create_password_file(path, password)
        elif Choice == "4":
            path = input("enter path: ")
            pm.load_password_file(path)
        elif Choice == "5":
            site = input("enter site: ")
            password = input("enter password: ")
            pm.add_password(site, password)
        elif Choice == "6":
            site = input("what site do you want to use: ")
            print(f"Password for {site} is {pm.get_password(site)}")
        elif Choice == "q":
            done = True
            print("Thank you for using this program")
        else:
            print("invalid choice")

if __name__ == "__main__":
  main()