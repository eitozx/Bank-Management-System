import os
import dotenv
from mysql import connector
from mysql.connector import errors

class InvalidCredential(Exception):
    pass


class Manage:

    def __init__(self):
        dotenv.load_dotenv(".env")

        try:
            self.connector = connector.connect(
                user = os.getenv("USER", "root"),
                password = os.getenv("PASSWORD"),
                host = os.getenv("HOST", "localhost")
            )
        except errors.ProgrammingError:
            raise InvalidCredential("Please fill '.env' file with correct credentials")

        self.dictcursor = self.connector.cursor(dictionary = True)
        self.cursor = self.connector.cursor()
        self.__database_exe__()
        self.__table_exe__()

    def __database_exe__(self):
        self.cursor.execute(
            f"CREATE DATABASE IF NOT EXISTS {os.getenv('DATABASE', 'banksystem')}"
        )
        self.cursor.execute(f"USE {os.getenv('DATABASE', 'banksystem')}")        

    def __table_exe__(self):
        self.cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS User(
                UserID VARCHAR(15) PRIMARY KEY,
                Password VARCHAR(25) NOT NULL,
                Amount INTEGER DEFAULT 0,
                Name VARCHAR(35) NOT NULL,
                DOB DATE NOT NULL,
                Phone BIGINT,
                Email VARCHAR(50),
                FatherName VARCHAR(35),
                MotherName VARCHAR(35),
                AadharID BIGINT
            )
        """)

    def admin(self, user : str, password : str):
        if user == os.getenv("USER", "root") and password == os.getenv("PASSWORD"):
            return True
        else:
            return False

    def deleteUser(self, UserID : str):
        self.cursor.execute(f"""
            DELETE FROM User
            WHERE UserID = "{UserID}"
        """)
        self.connector.commit()

    def exit(self):
        self.connector.close()
        self.cursor.close()
        return exit(0)

    def getUser(self, UserID : str, Password : str):
        self.dictcursor.execute(f"""
            SELECT * FROM User
            WHERE UserID = "{UserID}" AND Password = "{Password}"
        """)
        for data in self.dictcursor:
            if data:
                return data
            else:
                return None

    def read_data(self, data : str = "*", ext : str = ""):
        self.dictcursor.execute(f"SELECT {data} FROM User {ext}")
        for i in self.dictcursor:
            yield i


    def sign_in(self, UserID : str, Password : str):
        return self.getUser(UserID, Password)

    def sign_up(self, UserID : str, Password : str, Amount : int, Name : str,
        Birth : str, Phone : str, Email : str, FatherName : str,
        MotherName : str, AadharID : int):
        try:
            self.cursor.execute(f"""
                INSERT INTO User
                VALUES (
                    "{UserID}", "{Password}", {Amount},
                    "{Name}", "{Birth}", {Phone}, "{Email}",
                    "{FatherName}", "{MotherName}", {AadharID}
                )
            """)
            self.connector.commit()
            print("\nAccount Created Successfully!")
        except errors.IntegrityError:
            print(f"\nUserID: '{UserID}' already exists. Please retry with another UserID")

    def updateUser(self, UserID : str, field : str, value : str):
        self.cursor.execute(f"""
            UPDATE User
            SET {field} = "{value}"
            WHERE UserID = "{UserID}"
        """)
        self.connector.commit()
