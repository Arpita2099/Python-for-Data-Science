# String in Python
# String in python are the squence of unicode character.

# Creating String:
# Using single inverted Comma
str1='Hello, Arpita this side.'
print(str1)
print()

# Using Double inverted Comma
str2="Hello, and Welcome to Python string creation."
print(str2)
print()

# Triple inverted Comma
str3='''
Hey,
I am here to learn python.
And practice the real world example using python.
Thank You!!
'''
print(str3)
print()

# Accessing String:
# Indexing:
s="Arpita Sah"
print(s[1])

# Slicing
print(s[0:6])
print(s[0:])

# Editing Strings:
# We cannot change the string in the python because it is immutable.

# Deleting Strings:
string="Hello World!"
del string
print(string) #It will through error that string is not defined.

# Operations on String:
# Arithmetic Operations
print("Arpita"," ","Sah")
print("Arpita"*5)
print()

# Relational Operations
print("Kathmandu"=="Kathmandu") #True
print("Kathmandu"!="Nepal") #True
print("Nepal">"Kathmandu") #False # Compare lexiographically
print()

# Logical Operations
print('Arpita' and 'Sah') # It will give output: Sah
print('Arpita' or 'Sah') # It will give output: Arpita
print('' and 'Sah') # It will give output: ''
print('' or 'Sah') # It will give output: Sah
print(not '') # It will give output: True
print(not 'Arpita') # It will give output: False
print()

# Loop on String
for i in 'Arpita':
  print(i)
print()
for i in 'Sah':
  print("Arpita")
 print()

# Membership Operations
print('A' in 'Arpita') # Output: True
print('A' not in 'Arpita') # Output: False
print()

# String Functions:
# Common Function in String:
# len function
print(len("Hello World")) # It will provide you the length of string along with space. Output:11
print()

# max function
print(max("Arpita")) # It will provide you the maximum character in string acoording to comparision of ASCII value. Output: t
print()

# min function
print(min("Arpita")) # It will provide you the minimum character in the string according to comparision of ASCII value. Output: A
print()

# sorted function
print(sorted("Hello World")) # It helps to sort string on list in ascending order.Output: [' ', 'H', 'W', 'd', 'e', 'l', 'l', 'l', 'o', 'o', 'r']
print(sorted("Hello World",reverse=True)) # It helps to sort string on list in descending order. Output: ['r', 'o', 'o', 'l', 'l', 'l', 'e', 'd', 'W', 'H', ' ']
print()

# Capitalize
string="arpita Sah"
print(string.capitalize()) #Output: Arpita sah
print()

# Title
s="the beauty of nature"
print(s.title()) # Output: The Beauty Of Nature
print()

# Upper
s="sah"
print(s.upper()) # Output: SAH
print()

# Lower
s="SAH"
print(s.lower()) # Output: sah
print()

# Swapcase
print("Hello world".swapcase()) # Output: hELLO WORLD
print()

# Count
print("Myself Arpita Sah".count('a'))
print()

# Find
print("Myself Arpita Sah".find('Sah')) 
print("Myself Arpita Sah".find('Name')) # It will give output: -1
print()

# Index
print("Myself Arpita Sah".indes('Name')) # It will through you error.
print()

# endswith
print("Myself Arpita Sah".endswith('Sah')) 
print()

# startswith
print("Myself Arpita Sah".startswith('Myself')) 
print()

# Format
name="Arpita Sah"
gender="Female"
print("Hi my name is {} and my gender is {}.".format(name,gender))
