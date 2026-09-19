import math
import random
import datetime
email=input("Enter your email: ")
password=input("Enter your password: ")

if email=="nirbhay@gmail.com" and password=="123":
    print("Login Successful")
elif email=="nirbhay@gmail.com" and password!="123":
    print("Incorrect Password")
    password=input("Enter your password again: ")
    if password=="123":
        print("Login Successful")
    else:
        print("Login Failed beta tum chutiye ho ka ")
else:
    print("Incorrect Email");

print(math.sqrt(16))
print(random.randint(1,100))
print(datetime.datetime.now())
   