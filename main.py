import time
import pwinput
import BankSystem
from mysql.connector import errors

Bank = BankSystem.Manage()

def _compare(text : str):
    return text.replace("-","").replace(" ","").lower()

def viewinfo(user : dict):
    print(f"""
    Here's your info {user["Name"]}
    =================================

    Name: {user["Name"]}
    UserID: {user["UserID"]}
    Password: {user["Password"]}
    Amount: {user["Amount"]}
    DOB: {user["DOB"]}
    Phone: {user["Phone"]}
    Email: {user["Email"]}
    FatherName: {user["FatherName"]}
    MotherName: {user["MotherName"]}
    AadharID: {user["AadharID"]}
    """)

def signin():
    print("\n")
    UserID = input("Enter your user ID: ")
    Password = pwinput.pwinput("Enter your password: ")
    user = Bank.sign_in(UserID, Password)
    time.sleep(1)
    while user:
        choice = _compare(input(f"""

        Welcome {user["Name"]}!
        ===========================
        What would you like to do?

        1. View-Info
        2. Update-Info
        3. Delete-Account
        4. Log-Out

        Choose Option: """))
        if choice in ["1", "viewinfo"]:
            time.sleep(1)
            viewinfo(user)
            time.sleep(2)

        elif choice in ["2", "updateinfo"]:
            time.sleep(1)
            viewinfo(user)
            choice = input("Which field you like to edit?: ")
            value = input("Enter new value: ")

            if choice == "userid":
                try:
                    Bank.updateUser(UserID, choice, value)
                    user = Bank.getUser(value, Password)
                    print(f"Account Updated Successfully!")
                except errors.IntegrityError:
                    print(f"UserID: '{value}' already exists. Please retry with another UserID")

            elif choice == "password":
                Bank.updateUser(UserID, choice, value)
                user = Bank.getUser(UserID, value)
                print(f"Account Updated Successfully!")

            else:
                try:
                    Bank.updateUser(UserID, choice, value)
                    user = Bank.getUser(UserID, Password)
                    print(f"Account Updated Successfully!")
                except:
                    print("Please enter values in correct format")
            time.sleep(2)

        elif choice in ["3", "delete", "deleteaccount"]:
            time.sleep(1)
            Bank.deleteUser(user["UserID"])
            print("Account Deleted Successfully!")
            time.sleep(2)
            break

        elif choice in ["4", "logout", "exit"]:
            print("Logging out...")
            time.sleep(1)
            break
    else:
        print("Invalid Credentials, Please try again.")
        time.sleep(1)

def admin():
    print("\n")
    UserID = input("Enter DB User ID: ")
    Password = pwinput.pwinput("Enter DB Password: ")
    user = Bank.admin(UserID, Password)
    time.sleep(1)
    
    while user:
        choice = _compare(input(f"""

        Welcome Admin User
        ======================
        What would you like to do?

        1. View All Data
        2. Delete All Data
        3. Log-Out
        
        Choose Option: """))
        if choice in ["1", "viewall", "viewalldata"]:
            time.sleep(1)
            for i in Bank.read_data():
                print(i)
            else:
                print('Data Not Found')
            time.sleep(2)

        elif choice in ["2", "deleteall","deletealldata"]:
            time.sleep(1)
            Bank.cursor.execute("""
            DELETE FROM User
            """)
            Bank.connector.commit()
            print("\n All Data Deleted Successfully!")
            time.sleep(2)
            
        elif choice in ["3", "logout", "exit"]:
            print("Logging out...")
            time.sleep(1)
            break
    else:
        print("Invalid Credentials, Please try again.")
        time.sleep(1)

def welcome():
    choice = _compare(input(f"""
    Welcome to BankSystem
    ==========================

    1. Log-in
    2. Sign-Up
    3. Admin-Panel
    4. Exit

    Choose Option: """))
    if choice in ["1", "login"]:
        signin()

    elif choice in ["2", "signup"]:
        time.sleep(1)
        print("""
          BankSystem: Sign-Up
         =======================
        Enter the required data
        """)
        try:
            Name = input("Name: ")
            Birth = input("Birth [Format: YYYY-MM-DD]: ")
            Phone = input("Phone: ")
            Email = input("Email: ")
            FatherName = input("FatherName: ")
            MotherName = input("MotherName: ")
            AadharID = input("AadharID: ")
            UserID = input("User ID: ")
            Password = input("Password: ")
            Amount = input("Amount: ")

            Bank.sign_up(UserID, Password, Amount, Name, Birth,
                Phone, Email, FatherName, MotherName, AadharID)
            time.sleep(2)

        except:
            time.sleep(1)
            print("Please enter values in correct format")

    elif choice in ["3", "admin", "adminpanel"]:
        admin()

    elif choice in ["4", "exit"]:
        Bank.exit()
    else:
        print("Please Enter Valid Input")

while True:
    welcome()
