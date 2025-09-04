# Finding the length of given string without using len() function.
str=input("Enter a String: ")
count=0
for i in str:
  count+=1
print("The length of string is: ",count)

# Extract the user name from the given email.
# For instance, if email is: arpitasah750@gmail.com. Then, user name is arpitasah750.
str=input("Enter a email: ")
position=str.index('@')
print(str[0:position])

# Count the frequency of particular character in a provided string.
string=input("Enter what you want to write: ")
condition=input("What you want to search: ")
count=0
for i in string:
  if i==condition:
    count=count+1
print("Frequency is: ",count)

# Write a program which can remove a particular character from a string.
str=input("Enter any string: ")
condition=input("Enter what you want to remove: ")
result=''
for i in str:
  if i !=condition:
    result=result+i
print(result)

# Write a program that can check whether the given string is palindrome or not.
string=input("Enter any string: ")
flag=True
for i in range(0,len(string)//2):
  if string[i]!=string[len(string)-i-1]:
    flage= False
    print("Not a palindrome string.")
    break
if flag:
  print("String is palindrome.")

# Write a program to count the number of words in string without using split().
s=input("Enter any string: ")
L=[]
temp=''
for i in s:
  if i!=' ':
    temp=temp+i
  else:
    L.append(temp)
    temp=''
L.append(temp)    
print(L)

# Write a python program to convert a string to title case without using title()
s=input("Enter a string: ")
L=[]
for i in s.split():
  L.append(i[0].upper()+i[1:].lower())
print(" ".join(L))

# Write a program that can convert an integer to string.
num=int(input("Enter the number: "))
digit='0123456789'
result=''
while num!=0:
  result=digit[num%10]+result
  num=num//10
print(result)
print(type(result))

