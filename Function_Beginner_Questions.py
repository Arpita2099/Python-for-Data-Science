# Here are the some of the beginner level of function question.

# Write a function that takes a number as input and prints whether it is even or odd.
def Even_Odd():
    num=int(input("Enter any Number: "))
    if num%2==0:
        return'Even'
    else:
        return'Odd'
print(Even_Odd())

# Write a function program that calculates the factorial of given number.
def factorial():
    fact=1
    num=int(input("Enter any Number: "))
    for i in range(1,num+1):
        fact=fact*i
    return fact
print(f"Factorial is :",factorial())

# Write a function that returns the sum of all numbers from 1 to n.
def Sum_Num():
    sum=0
    num=int(input("Enter any Number: "))
    for i in range(1,num+1):
        sum=sum+i
    return sum
print("Sum of all number is: ",Sum_Num())

# Write a function that takes two numbers and print the largest one.
def Largest_One():
  num1=int(input("Enter first Number: "))  
  num2=int(input("Enter second number: "))
  if num1>num2:
      return num1,'The largest Number.'
  else:
      return num2,'The largest Number.'
print(Largest_One())
