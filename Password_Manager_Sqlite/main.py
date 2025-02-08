from create import Create
import pyfiglet
from Sign_in import signin
from Login import Login
ascii_banner = pyfiglet.figlet_format("Save Passwords")
print(ascii_banner)
Create()

print("Enter Your Choice ")
print("1) Sign_in")
print("2) Login")
print("3) for exit")





    
while 1:
        try:
            choice = input()
            choice = int(choice)
            if choice == 1:
                signin()
            elif choice == 2:
                Login()
            elif choice == 3:
                break
   
        except ValueError:
            print("Please enter a valid number")
            break
        except:
            
            print("An unexpected error occurred")
            break

