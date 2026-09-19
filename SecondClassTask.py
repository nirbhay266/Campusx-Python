## Problem 1: Write a program that will give you in hand monthly salary after deduction on CTC - HRA(10%), DA(5%), PF(3%) and taxes deduction as below:
## Salary(Lakhs) : Tax(%)

## Below 5 : 0%
## 5-10 : 10%
## 10-20 : 20%
## aboove 20 : 30%
## Write code here


salary=1500000
hra=salary*10/100
da=salary*5/100
pf=salary*3/100

if salary<=500000:
  print("Not Taxable")
elif salary>=500000 and salary<=1000000:
  tax=(salary*10)/100
  after_tax_d=salary-hra-da-pf-tax
  print(f"Your all CTC {salary} After tax dedutions your salary is",after_tax_d)
elif salary>=1000000 and salary<=2000000:
  tax=(salary*20)/100
  after_tax_d=salary-hra-da-pf-tax
  print(f"Your all CTC {salary} After tax dedutions your salary is",after_tax_d)
elif salary>2000000:
  tax=(salary*30)/100
  after_tax_d=salary-hra-da-pf-tax
  print(f"Your all CTC {salary} After tax dedutions your salary is",after_tax_d)

print(f"Here is your salary slab:->\n Total Salary->{salary} \n HRA:->{hra} \n DA->{da} \n PF->{pf},\n Tax->{tax}");


## Problem 2: Write a program that take a user input of three angles and will find out whether it can form
## a triangle or not.

# a=int(input("Enter first angle: "))
# b=int(input("Enter second angle: "))
# c=int(input("Enter third angle: "))

# if a>0 and b>0 and c>0 and a+b+c==180:
# #(a+b>c) and (b+c>a) and (a+c>b):
# #a+b+c==180:
#   print("Yes, it can form a triangle")
# else:
#     print("No, it can't form a triangle")

# # Problem 3: Write a program that will take user input of cost price and selling price and 
# # determines whether its a loss or a profit.

# cost_price=int(input("Enter cost price: "))
# selling_price=int(input("Enter selling price: "))

# if selling_price>cost_price:
#   profit=selling_price-cost_price
#   print(f"your profite is {profit}")
# elif selling_price<cost_price:
#     loss=cost_price-selling_price
#     print(f"your loss is {loss}")
# else:
#     print("No profit no loss")


## Problem 4: Write a menu-driven program -
## cm to ft
## km to miles
## USD to INR
## # exit
# print(''' Please select your option:
#     1.cm to ft
#     2.km to miles
#     3.USD to INR
#     4.exit
#   ''')
# option=int(input("Enter your option: "))
# if option==1:
#   CM=int(input("Enter your number: "))
#   feet=CM*12
#   print(f"Your number in Feet is: {feet}")
# elif option==2:
#     KM=int(input("Enter your number in KM: "))
#     miles=KM*0.621371
#     print(f"Your number in Miles is: {miles}")
# elif option==3:
#     USD=int(input("Enter your number in USD: "))
#     INR=USD*96
#     print(f"Your number in INR is: {INR}")
# elif option==4:
#   exit()
# else:
#   print("Invalid option ")


## Problem 5 - Exercise 12: Display Fibonacci series up to 10 terms.
## Note: The Fibonacci Sequence is a series of numbers. The next number is found by adding up the two 
## numbers before it. The first two numbers are 0 and 1. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. 
## The next number in this series above is 13+21 = 34

# Write code here
# a=0
# b=1
# for i in range(10):
#   print(a,end=" ")
#   c=a+b
#   a=b
#   b=c

## Problem 6 - Find the factorial of a given number.
## Write a program to use the loop to find the factorial of a given number.

## The factorial (symbol: !) means to multiply all whole numbers from the chosen number down to 1.

## For example: calculate the factorial of 5

## 5! = 5 × 4 × 3 × 2 × 1 = 120

  # fact=int(input("Enter your number to find factorial: "))
  # factorial=1
  # for i in range(fact,0,-1):
  #   factorial=factorial*i
  #   print(i,end=" ")
  # print(f"Factorial of {fact} is: {factorial}")


## Problem 7 - Reverse a given integer number.
## Example:
## Input:
## 76542
## Output:
## 24567
n=76542
# rev=0
# while n>0:
#   digit=n%10
#   rev=rev*10+digit
#   n=n//10
# print(f"\nReversed number is: {rev}")



## Problem 8: Take a user input as integer N. Find out the sum from 1 to N. If any number if divisible by 5, then skip that number. And if the sum is greater than 300, don't need to calculate the sum further more. Print the final result. And don't use for loop to solve this problem.
## Example 1:
## Input:
## 30
## Output:
## 276

## Write code here
# n=int(input("Enter the number: "))
# i=1
# sum=0
# while i<=n:
#   if i%5==0:
#     i=i+1
#     continue
#   sum=i+sum;
#   if sum>300:
#     break
#   i=i+1
# print(sum)

##   Problem 9: Write a program that keeps on accepting a number from the user until the user enters Zero.
## Display the sum and average of all the numbers.

# Write code here
# # Write code here
# n=int(input("Enter the number: "))
# sum=0
# count=0
# while n!=0:
#  try:
#       user_input=input("Enter the number: ")
#       if user_input.strip()=="":
#         print("Please enter number")
#         continue
#       n=int(input("Enter the number: "))
#       if n==0:
#         break

#       sum=sum+n
#       count=count+1
#  except ValueError:
#       print("Please enter number")
    
# print("Sum is: ",sum)
# print("Average is: ",sum/count)

##########################################################################################################################################

## Problem 10: Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). 
## The numbers obtained should be printed in a comma-separated sequence on a single line.


# for i in range(2000,3201):
#   if i%7==0 and i%5!=0:
#     #print(i,end=",")

#########################################################################################################################################

## Problem 11: Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
## The numbers obtained should be printed in a space-separated sequence on a single line.

for i in range(1000,3001):
  valid=True
  digits=list(map(int,str(i)))
  for j in digits:
    if j%2!=0:
      valid=False
  if valid:
    print(i,end=",")


## Problem 12: A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
## The trace of robot movement is shown as the following:

## UP 5
## DOWN 3
## LEFT 3
## RIGHT 2
## !
## The numbers after the direction are steps.

## ! means robot stop there.

## Please write a program to compute the distance from current position after a sequence of movement and original point.

## If the distance is a float, then just print the nearest integer.

## Example:

## Input:

## UP 5
## DOWN 3
## LEFT 3
## RIGHT 2
## !
## Output:
#
## 2
## Write code here

# x=0
# y=0
# while True:
#   s=input("Please enter movment (e.g, UP 5,DOWN 2)")

#   if s=='!':
#     break
#   part=s.split()
#   if len(part)!=2:
#     print("Invalid formate please enter again like DOWN 3 UP 6")
#   direction=part[0].upper()
#   step=int(part[1])

#   if direction=="UP":
#     y=y+step
#   if direction=="DOWN":
#     y=y-step
#   if direction=="RIGHT":
#     x=x+step
#   if direction=="LEFT":
#     x=x-step
#   else:
#     print("Invalide Input")
#   # Distace calculation
#   distance=(x**2+y**2)**0.5
# print("Final Distance",round(distance))

## Problem 13: Write a program to print whether a given number is a prime number or not

# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# number = int(input("Enter a number: "))
# if is_prime(number):
#     print(f"{number} is a prime number.")
# else:
#     print(f"{number} is not a prime number.")

####  Check Armstrong number

# n= int(input("Enter a number: "))
# a=n
# rev=0
# while n>0:
#   digit=n%10
#   rev=rev*10+digit
#   n=n//10
# print("Reversed number:", rev)

# if rev==a:
#   print(f"{a} is a palindrome number.")
# else:
#   print(f"{a} is not a palindrome number.")

#### 13 Check Armstrong number

# n= int(input("Enter a number: "))
# a=n
# sum=0
# while n>0:
#   digit=n%10
#   sum=sum+digit**3
#   n=n//10
# print("Sum of digits:", sum)

# if sum==a:
#   print(f"{a} is a Armstrong number.")
# else:
#   print(f"{a} is not a Armstrong number.")

time_hour=input("Enter time (HH:MM ): ")
h,m=map(int,time_hour.split(":"))
#HD=h*30
#MV=m*0.5
hours_angle=h*30+m*0.5
minutes_angle=m*6
angle=abs(hours_angle-minutes_angle)
final_angle=min(angle,360-angle)
print(f"Angle between hour and minute hand is: {final_angle} degrees")


