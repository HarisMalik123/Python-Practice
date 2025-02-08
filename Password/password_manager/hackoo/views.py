from django.shortcuts import render,redirect
from django.http import HttpResponse
import re
import pandas as pd
from io import BytesIO
from cryptography.fernet import Fernet
def index(request):
    return render(request,"hackoo/login.html")
def toggle(request):
    return render(request,"hackoo/signup.html",context={})
def login_submit(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        key_file_path = r'E:\Password\key.key'
        with open(key_file_path, "rb") as f:
            key = f.read()
        cipher = Fernet(key)
        csv_file = 'data.csv'
        with open(csv_file, "rb") as f:
            encrypted_data = f.read()

        decrypted_data = cipher.decrypt(encrypted_data)

        # Create a BytesIO object and write decrypted data to it
        decrypted_io = BytesIO()
        decrypted_io.write(decrypted_data)
        decrypted_io.seek(0)  # Reset the position to the beginning of the stream

        # Load decrypted data from the BytesIO object into a DataFrame
        df = pd.read_csv(decrypted_io)
        

        condition = ((df['UserName'] == username) & (df['Password'] == password)).any()
        print(condition)
        if condition:
            return HttpResponse("Welcome")
        else:
            return HttpResponse("Username was not found")

    else:
        return HttpResponse("Method is not allowed")
def signup_submit(request):
    if request.method == 'POST':
        username = str(request.POST.get('username'))
        password = str(request.POST.get('password'))
        age = request.POST.get('age')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        retypepass=str(request.POST.get('password_confirmation'))
        if len(password)<8 and re.search(r'[a-zA-Z0-9]',password)==False:
            return HttpResponse("Password Must Be Greater Than 8 character should have atleast one number character")
        if not password == retypepass:
            return HttpResponse("password Did Not matched ")
        else:
            key_file_path = r'E:\Password\key.key'
            with open(key_file_path,'rb') as f:
                key=f.read()
            cipher=Fernet(key)
            data = {'UserName': username, 'Password': password, 'age': age, 'email': email, 'Cell_phone_number': phone_number}
            df = pd.DataFrame([data])

            csvfile='data.csv'
            try:
                existing_df=pd.read_csv(csvfile)
                updated_df=pd.concat([existing_df,df],ignore_index=True)
                encrypted_data=cipher.encrypt(updated_df.to_csv(index=False).encode())
                updated_df.to_csv(csvfile,index=False)
                with open (csvfile,'wb') as f:
                    f.write(encrypted_data)
                    
            except FileNotFoundError:
                encrypted_data=cipher.encrypt(df.to_csv(index=False).encode())
                with open(csvfile,'wb') as f:
                    f.write(encrypted_data)
                
        
            return redirect('index')
    else:
        return HttpResponse("Method is not allowed")
    