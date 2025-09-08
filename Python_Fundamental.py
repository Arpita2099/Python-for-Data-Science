# While starting the code in the python just remember one thing that python is a case sensative language. So, keep in mind while using the syntax and function in the python.
# Now I am going to print something using the python. For instance,
print("Hey Everyone!, Welcome to python cosing language.")

#We acn also print anything in python using single inverted comma. For instance,
print('Okay, this is the code in python to print output using single inverted comma.')

# Also using the triple inverted comma we can print the output in the python. For instance, 
print('''
This is my first code in python using triple inverted comma.
Here, I can write myultiple sentence using this in the python at once.
And, it will give the output togethers.
''')
# Therefore, this is the about the python output using multiple inverted comma.

#Like above, we can also print the intege, boolen, and floats using the print common in the Python. For instance,
# For integer.
print(17) # It will provide you output 17.

#For Float
print(45.89) # It will provide you output 45.89.

# For Boolen,
print(True) # It is provide you value True.
print(False) # It will provide you output False.

# Even you can print multiple things at once. For instance,
print("Arpita is ",True, 100, "%", sep="/")

# If you want to print the different print statement in one sentence and you can use this code. For instance,
print("This is ", end="-")
print("Apita Sah")

#Data Types Section
# Let first know that datatype is the classification of data items.
# Integer Data Types 
print(12)
# Python can handle the long integer upto 1*10^308
print(1e308)

# Let first know that datatype is the classification of data items.

# Integer Data Types 
print(12) #It will give output 12
# Python can handle the long integer upto 1*10^308
print(1e308) # It will give output 1e+308

# Decimal/Float Data Types
print(13.88) # It will give output 13.88
# We can also say that Python can handle larger decimal or float value to
print(1.7e308) #It will give output 1.7e+308

# Boolean Data Types
# This Data Types are used to print the True and False in Python.
print(True)
print(False)

# Text/String Data Types
# In this data types you can print the text or string using the print function. For inatance,
print("Hello I am here to make my coding habits in Python.")

# Complex Data Types
# In this data types you are able to print the complex number like real and imaginary number together in Python. For instance,
print(4+5j) # In other programming language or in real life we uses 4+5i in the comple number but in the python in the place of i we have to write j to get the complex number.

# List Data Types
# List data types in the python helps to print the list of data in the python and it is mutal types of data. For inatance,
print([10,20,30,40,50])

# Tuple Data Types
# Tuple data types is used to print the tuple data in the python and it is immutable types of data. For instance,
print((5,10,15,20))

# Note one think in the mind that list and tuple is not a same thing. This is because list is a kind of mutable data type like it can be canged according to you requirement and needs but tuple is an immutable types of data which cannot be changed. This is the main difference between the list and tuple in the python.

# Sets Data Types
# Sets is a kind os data types in the python which is also a kind of immutable data types in python. For inatance,
print({1,3,5,7,9})

# Dictionary Data Types
# Dictionary is also a kind of data type which is used to give the value and name and it will print. For instance,
print({'Name':'Arpita Sah', 'Gender': 'Female'})

# Also we have to know about the type() function in the python. For instance,
# If you want to check the data types of any data just print the below syntax to check it.
print(type(132)) # It will give you the types of data integer data types like this only youcan check any kind of data types using function type().

# Arithmetic Operators
# In python there are arithmetic operators like +,-,*,/,//.
# Now see how arithemetic operators work.
print(10+20) # It will give output: 30
print(30-10) # It will give output: 20
print(10*3) # It will give output: 30
print(50/10) # It will give output: 5.0
print(67//6) # It will give output: 11
print(12%5) # It will give output: 2
print(5**2) # It will give square of 5 output: 25

# Relational Operators
print(12>5) #Output: True
print(4<10) #Output:True
print(10>=5) #Output:True
print(10<=20) #Output:True
print(20==50) #Output: False
print(5!=10) #Output:True

# Logical Operators
print(1 and 1)
print(1 and 0)
print(0 or 0)
print(1 or 0)
print(not(1))
print(not(0))

#Bitwise Operators
# Bitwise and operators 
print(5 & 6) #Output: 4
print(5 | 6) #Output: 7
print(5 ^ 6) #Output: 3
print(~3) #Output:-4
print(4 >> 2) #Output: 
print(4 << 2) #Output:

# Membership Operators
# in/not in
# Membership Operators
# in/not in
print('K' in 'Kathmandu') #It will give Output: True
print('K' not in 'Kathmandu') #It will give Output: False

# Fin the sum of three digit number enter by user.
User_number=int(input("Enter any 3 digit number:")) # It will ask the 3 digit number from user.
sum=0 #Initial sum value is assign 0
while User_number>0: # Loop will run untill the User_number is greater than 0.
  rem=User_number%10 # It will give the remender value means last value.
  sum=sum+rem #It will add the last value and provide the sum of 3 digits number.
  User_number=User_number//10 # It will provide the integer division of digit.
print("Sum of 3 digit number is: ",sum) # Lastly, you will get the output by adding 3 digit number over here.
  
print()

# Login Program and indentation.
# In this login page the email id:arpitasah750@gmail.com along with password=12345 than it will print the command Welcome else it will print your email and password is wrong.
email=input("Enter your email password: ")
password=input("Enter your password: ")
if email=='arpitasah750@gmail.com' and password=='12345':
  print("Thank you for login, and Welcome")
else:
  print("Your email and password is wrong.")


# Login Program and indentation.
# In this login page the email id:arpitasah750@gmail.com along with password=12345 than it will print the command Welcome else it will print your email and password is wrong.
email=input("Enter your email password: ")
password=input("Enter your password: ")
if email=='arpitasah750@gmail.com' and password=='12345':
  print("Thank you for login, and Welcome")
elif email=='arpitasah750@gmail.com' and password!='12345':
  print("Your password is incorrect.")
  password=input('Enter your password:')
  if password=='12345':
    print("Your password is right, Welcome!")
  else:
    print("Your password is wrong Again!")
else:
  print("Your email and password is wrong.")
print()

# Find the maximum of three given number.
num1=int(input("Enter the value of first number: "))
num2=int(input("Enter the value of second number: "))
num3=int(input("Enter the value of third number: "))
if num1>num2 and num1>num3:
  print(f"{num1} is maximum number among {num1},{num2},{num3}.")
elif num2>num3:
  print(f"{num2} is maximum number among {num1},{num2},{num3}.")
else:
  print(f"{num3} is maximum number among {num1},{num2},{num3}.")
print()

# Menu driven Calculator.
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
opr=input("Enter '+','-','*','/'")
if opr=='+':
  print(f"Sum of two number is: {num1+num2}")
elif opr=='-':
   print(f"Substraction of two number is: {num1-num2}")
elif opr=='*':
   print(f"Multiplication of two number is: {num1*num2}")
else:
   print(f"Division of two number is: {num1/num2}")
print()

# Math
import math
print(math.factorial(5))
print()

#keywords
import keyword
print(keyword.kwlist)
print()

#random
import random
print(random.randint(1,100))
print()

#datetime
import datetime
print(datetime.datetime.now())

#help('modules') # To check the modules present in the python.

# While loop
# Write a program to print table using while loop.
num=int(input("Enter a number: "))
i=1
while i<11:
  print(f"{num}*{i}={num*i}")
  i+=1
  
