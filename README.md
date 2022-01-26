# Bank Management System
MySQL Based Bank Management System \
*For school project*

## Key Features
- It uses its Own Library ([BankSystem](/BankSystem)).
- Creates its OWN Database & Table (if doesn't exist).
- It has basic CRUD (Create, Read, Update, Delete) operations.

## External Libraries
- [mysql-connector-python :](https://pypi.org/project/mysql-connector-python/) to deal with MySQL server.
- [python-dotenv :](https://pypi.org/project/python-dotenv/) to deal with .env file.
- [pwinput :](https://pypi.org/project/pwinput/) to "mask" password.


# How to use
Following are the steps if you want to run this banksystem on your pc.

## Clone repository
Clone this repository by following command
```cmd
git clone https://github.com/EitoZX/Bank-Management-System.git
```
**OR** **[CLICK HERE to Download this repository](https://github.com/EitoZX/Bank-Management-System/archive/refs/heads/master.zip)**

## Fill `.env` file with correct credentials
For reference, you can check [.env.example file](/.env.example). \
Then create a file named `.env` & fill it with correct credentials.

## Install required libraries
To install required libraries, follow the command:
```cmd
pip install -r requirements.txt
```
in working directory. \
**OR** install libraries mentioned in [requirements.txt](requirements.txt) manually by following command:
```cmd
pip install <library/package_name>
```

## Run!
Just run [main.py](main.py) to use "Bank Management System".


# Bibliography
MySQL [Docs](https://dev.mysql.com/doc/connector-python/en/) & [Examples](https://dev.mysql.com/doc/connector-python/en/connector-python-examples.html)