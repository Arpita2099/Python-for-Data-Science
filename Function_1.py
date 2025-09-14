# Function in Python
# Write a function program to print the given number is even or odd.
def even_odd():
    num=int(input("Enter any numnber: "))
    if num%2==0:
       print(f" {num} is even.")
    else:
        print(f" {num} is odd.")
even_odd ()
# If user will give 11, it will give output even.
# If user will give 12, it will give output odd.

# Types of Argument:
# Default Argument
def power(a=1,b=1):
    return a**b
print(power(2,3)) # Output: 8
print(power(2)) # Output: 2

# Positional Argument
def power(a,b):
    return a**b
print(power(2,3)) # Output: 8

# Keyword Argument
print(power(b=2,a=3)) # Output: 9

# *args and **kwargs
# These are the special python keywords that are used to pass the variable length of arguments to a function.

# *args 
# It allows us to pass a variable number of non-keyword arguments to a function.
# For instance of arg:
# This is using the normal function. But what if you what to print the multiple of indefine number input receive and can provide the multiplication of all.
def multiply(a,b):
    return a*b
print(multiply(2,3))

# Using args 
def multiply(*args):
    product=1
    for i in args:
        product= product*i
    return product
print(multiply(1,2,3,4,5,6))

# Also we can write anything instead of args like any name. For instance,
def multiply(*arpi):
    product=1
    for i in arpi:
        product= product*i
    return product
print(multiply(1,2,3,4,5,6))
# Output: 720

# How to excess documentation of function.
# print(even_odd.__doc__)
# print(print.__doc__)
# ** kwargs 
# **kwargs allows us to pass any number of keyword arguments.
# Keyword arguments mean that they contain a key-value pair a Python dictionary.
def display(**kwargs):
    for (key,value) in kwargs.items():
        print(key,"->",value)
display(Nepal="Kathmandu", Srilanka="Colombo", Pakistan="islambad")
# Output: 
#Nepal -> Kathmandu
# Srilanka -> Colombo
# Pakistan -> islambad

# Point tobe noted:
# Order of the arguments matter(normal->*args->**kwargs)
# The words "args" and "kwargs" are only a convention, you can use any name of your choice.
