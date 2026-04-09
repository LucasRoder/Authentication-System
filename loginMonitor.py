class Account: # creates account objcets
    def __init__(self, password, secret_answer):
        self.password = password
        self.secret_answer = secret_answer
        self.locked = False

class LoginMonitor:

    def __init__(self): # adds to dictonary for storage
        self.accounts = {
            "admin": Account("admin123", "admin")
        }

    def whitespace_checker(self, password)-> bool:
        for char in password:
            if char.isspace():
                return False

        return True

    def length_checker(self, password)-> bool:
        return len(password) >= 8

    def strength_checker(self, password) -> str:
        # checks for number upper case letter lower case letter and specail char
        strength = 0
        num = False
        upper = False
        lower = False
        special = False

        for letter in password:
            if letter.isdigit():
                num = True
            if letter.isupper():
                upper = True
            if letter.islower():
                lower = True
            if not letter.isalnum():
                special = True

        if num:
            strength += 1
        if upper:
            strength += 1
        if lower:
            strength += 1
        if special:
            strength += 1

        if strength >= 3:
            return "strong password"
        elif strength == 2:
            return "medium password"
        else:
            return "weak password"

    def get_valid_password(self, username)-> str:
        password = input(f"Please enter a password for {username} that is at least 8 characters and contains no spaces: ")

        while not self.whitespace_checker(password) or not self.length_checker(password):
          # continusly asks for password until no white space and at least 8 char
            if not self.whitespace_checker(password) and not self.length_checker(password):
                print(f"Your password length is {len(password)} and it contains spaces.")
            elif not self.whitespace_checker(password):
                print("Your password contains spaces.")
            elif not self.length_checker(password):
                print(f"Your password length is {len(password)}.")

            password = input(f"Please enter a password for {username} that is at least 8 characters and contains no spaces: ")

        print("Password strength:", self.strength_checker(password))

        password_confirm = input(f"Confirm password for {username}: ")
        # confirms password for username  by making user retype
        while password != password_confirm:
            print("Passwords do not match.")
            password_confirm = input(f"Confirm password for {username}: ")

        return password

    def make_account(self):
        print("\nCreating new account")

        username = input("Enter username: ")

        while username in self.accounts: # ensures username unique so dictonary dosnet break
            print("Username already exists.")
            username = input("Enter username: ")

        password = self.get_valid_password(username)

        secret = input("Please enter the name of your first pet so you can recover your account if locked out: ")

        self.accounts[username] = Account(password, secret)

        print("Account created successfully.")

    def login(self):
        print("\nLogging in")
        attempts = 3 # 3 password attempts
        username = input("Username: ")

        while username not in self.accounts:
            print("Username not found.")
            username = input("Username: ")


        if self.accounts[username].locked:
            # if locked make type in answer to secret question
            print("Account is locked.")
            secret = input(
                "Please enter the name of your first pet to unlock your account: "
            )

            if self.accounts[username].secret_answer == secret:
                self.accounts[username].locked = False
                print("Identity confirmed. Account unlocked.")
            else:
                print("Incorrect secret answer.")
                return

        password = input("Password: ")

        while self.accounts[username].password != password:
            # lowers attempts if incorect answer
            attempts -= 1

            if attempts == 0: # after 3 failures locks accpunt
                print("Too many failed attempts. Account locked.")
                self.accounts[username].locked = True
                return

            print(f"Password incorrect. You have {attempts} attempt(s) remaining.")
            password = input("Password: ")

        print("Login successful.")

    def change_password(self):
        username = input("Username: ")

        while username not in self.accounts:
            print("Username not found.")
            username = input("Username: ")

        # must answer security question to change password
        secret = input("Please enter the name of your first pet to confirm your identity: ")
        if self.accounts[username].secret_answer != secret:
            print("Incorrect secret answer.")
            return
        print("Identity confirmed.")
        new_password = self.get_valid_password(username)
        #if correct password calls valid password function to get new password

        self.accounts[username].password = new_password
        self.accounts[username].locked = False
        print("Password changed successfully.")

    def display_menu(self):
        # menu
        print("\n************************")
        print("*** Login Monitor ***")
        print("************************")
        print("1. Login")
        print("2. Create new account")
        print("3. Change password")
        print("4. Exit")

    def run(self):
        # keeps program runing till user exit
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == "1":
                self.login()
            elif choice == "2":
                self.make_account()
            elif choice == "3":
                self.change_password()
            elif choice == "4":
                print("Goodbye.")
                break
            else:
                print("Invalid option. Please enter 1, 2, 3, or 4.")

def main():
    monitor = LoginMonitor()
    monitor.run() # runs program

if __name__ == "__main__":
    main()





