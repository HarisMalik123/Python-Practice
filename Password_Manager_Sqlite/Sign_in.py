
import bcrypt
import re
import string
import random
from Login import hashpassword
import sqlite3
def is_valid_password(password):
    
    pattern = (
        r'^(?=.*[a-z])'    
        r'(?=.*[A-Z])'      
        r'(?=.*\d)'         
        r'(?=.*[@$!%*#?&])'
        r'[A-Za-z\d@$!%*#?&]{8,}'
    )
    

    if re.fullmatch(pattern, password):
        return True
    else:
        return False
def validate_email(email):
    pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    ## ^ means Start of string should be upper lowercase or digits atleast one then @ must be there then atleast upper lower digit . or - must be there 
    ## then again same thing bu
    if re.match(pattern=pattern,string=email):
        return True
    else:
        return False
    
def generate_pass():
    
    length=12 ## for More Secure Password
    characters=string.ascii_letters+string.digits+string.punctuation
    password=''.join(random.choice(characters) for i in range(length))
    return password
def signin():
    username = input("Enter Your Username: ")
    choice = input("Do You Want to Generate Random Password (Y/N): ")

    email = ""
    password = ""

    if choice.lower() == 'y':
        password = generate_pass()
        print(f"Your Password is {password}")
    else:
        while True:
            password = input("Enter Your Password: ")
            if not is_valid_password(password):
                print("Password does not meet the criteria.")
            else:
                break

        while True:
            password_confirm = input("Confirm Your Password: ")
            if password != password_confirm:
                print("Passwords do not match. Please try again.")
            else:
                break

    # Hash the password before storing it
    password = hashpassword(password)

    while True:
        email = input("Enter Your Email ID: ")
        if not validate_email(email):
            print("Invalid Email. Please enter a valid email address.")
        else:
            break

    
    try:
        con = sqlite3.connect('password.db')
        curr = con.cursor()
        curr.execute('''INSERT INTO users (username, password_hash, email) VALUES (?, ?, ?)''', (username, password, email))
        con.commit()
        print("User registered successfully.")
    except sqlite3.Error as e:
        print("Error occurred while inserting into database:", e)
    finally:
        con.close()