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

# Menu driven Calculator.
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
opr=input("Enter '+','-','*','/': ")
if opr=='+':
  print(f"Sum of two number is: {num1+num2}")
elif opr=='-':
   print(f"Substraction of two number is: {num1-num2}")
elif opr=='*':
   print(f"Multiplication of two number is: {num1*num2}")
else:
   print(f"Division of two number is: {num1/num2}")

