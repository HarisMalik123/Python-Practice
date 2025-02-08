
import bcrypt

import pandas as pd
from tabulate import tabulate
import sqlite3
con=sqlite3.connect('password.db')
cur=con.cursor()
def hashpassword(password):
    salt=bcrypt.gensalt()
    hash_password=bcrypt.hashpw(password.encode('utf-8'),salt)
    return hash_password.decode('utf-8')
def fetch(userid):
    
    cur.execute('''select website, password_text from password where user_id = ? 
                ''',(userid,))
    passwords=cur.fetchall()
    if passwords:
        df=pd.DataFrame(passwords,columns=['Websites','Passwords'])
        print(tabulate(df,headers='keys',tablefmt='pretty'))
    else:
        print("No Data of this user")
def insert(userid,password,website):
    
    cur.execute(''' Insert into password (user_id,website,password_text)
                values(?,?,?)
                ''',(userid,website,password))
    con.commit()
def update(user_id):
    website = input("Enter the Name of Particular website whose password you want to update: ")
    cur.execute('''SELECT website FROM password WHERE user_id = ? AND website = ?''', (user_id, website))
    website_row = cur.fetchone()
    if website_row:
        password = input("Enter Updating password: ")
        cur.execute('''UPDATE password SET password_text = ? WHERE user_id = ? AND website = ?''', (password, user_id, website))
        con.commit()
        print("Password updated successfully!")
    else:
        print("Website with this name does not exist.")
    
def Login():
    
    user=input("Enter Username")
    password=input("Enter Password")
    
    cur.execute('''SELECT password_hash FROM users where username = ?
                   ''',(user,))
    stored_pass=cur.fetchone()
    print(stored_pass)
    if stored_pass:
        
        if bcrypt.checkpw(password.encode('utf-8'),stored_pass[0].encode('utf-8')):
            cur.execute('''select user_id from users where username = ? and password_hash = ?
                           ''',(user,stored_pass[0]))
            userid=cur.fetchone()
            user_id=userid[0]
            while 1:
                choice=input("Enter v for viewing your password and I for inserting password and U for updating Password  E for exit ").lower()
            
                if choice=='y':
                    fetch(user_id)
                if choice=='i':
                    while 1:
                        website=input("Enter Website")
                        password=input(f"Enter Password for Website {website}")
                        insert(user_id,password,website)
                        if input("Enter Y for inserting more and N for exit ").lower() == 'n':
                            break
                    print("Data Inserted Succesfully")
                if choice == 'u':
                    update(user_id)
                if choice == 'e':
                    break
                        
            
            
        else:
            print("Password Did Not Matched ")
            return False
            
    else:
        print("User Did Not Exist")
        return False
    
    
    
    
    
    