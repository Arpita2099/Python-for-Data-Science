# What is List: List is the type of data types wher you can stotre multiple items in one list. Same type of data is store in the list. 

# List Vs Array
# Fixed Vs Dynamic (List have dynamic size.)
# Convenience->Hetrogeneous (List are Hetrogeneous because it store mixer of data items)
# Speed of Excution (List speed is slower than that of array)
# Memory (List comsume more storage than that of array)

# Characterstics of List
# Ordered
# Changeable/ Mutable
# Hetrogeneous
# Can duplicates
# Are dynamic
# Can be nested
# item can be accessed
# can contains any kind of objects in python

# id() function: print the memory address. For instance,
L=[1,2,3]
print(id(L[0]))
print(id(L[1]))
print(id(L[2]))

# How to create a list
# Empty
print([]) #Output: []

# 1D-> Homogeneous List
print([1,2,3,4,5]) #Output: [1, 2, 3, 4, 5]

# 2D-> 
print([1,2,3,4,[5,6,7]]) # This is a Hetrogeneos List. #Output: [1, 2, 3, 4, [5, 6, 7]]

# 3D
print([[[1,2],[3,4]],[[5,6],[7,8]]]) # This is a Homogeneous List. #Output: [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]

# Hetrogeneous
print([1,True,'Hello',3+4j]) #Output: [1, True, 'Hello', (3+4j)]

# Using Type Conversion
print(list("Hello")) # Output: ['H', 'e', 'l', 'l', 'o']

# Accessing items from a List
#Indexing
# Positive indexing
l=[1,2,3,4,5]
print(l[1]) # Output: 2

L=[1,2,3,4,[5,6,7]]
print(L[4][0]) # Output: 5

print()
L=[[[1,2],[3,4]],[[5,6],[7,8]]]
print(L[1][0][0]) # Output: 5

# Negative indexing
l=[1,2,3,4,5]
print(l[-2]) # Output: 4
print()
L=[1,2,3,4,[5,6,7]]
print(L[-1][-3]) # Output: 5
print()
L=[[[1,2],[3,4]],[[5,6],[7,8]]]
print(L[-1][-2][-2]) # Output: 5

# Slicing 
l=[1,2,3,4,5]
print(l[1:]) # Output: [2,3,4,5]
print(l[1:3]) # Output: [2,3]

# Adding items to a List
# append: Append helps to add only one number at the end.
L=[1,2,3,4,5]
L.append(6)
print(L) # Output: [1,2,3,4,5,6]
print()

# extend: Extend can add multiple iteams at once to the list.
L=[1,2,3,4,5]
L.extend(6,7,8,9)
print(L) # Output: [1,2,3,4,5,6,7,8,9]

# insert: Used to add data according to your desire.
L=[1,2,3,4,5]
L.insert(1,100)
print(L) # Output: [1, 100, 2, 3, 4, 5]

# Editing items from a List
L= [1, 2, 3, 4, 5]
# Editing with negative indexing.
L[-1]=500
# Editing with positive indexing.
L[0]=100
# Editing with slicing 
L[1:4]=200, 300, 400
print(L)

# Deleting items from a List
# del
L= [1, 2, 3, 4, 5]
# Deleting with negative indexing.
del L[-1]
# Deleting with positive indexing.
del L[1]
# Deleting with slicing 
del L[2:3]
print(L) # Output: [1, 3]
print()

# remove()
l=[1,2,3,4,5,6]
l.remove(6)
print(l) # Output: [1, 2, 3, 4, 5]
print()

# pop()
l=[1,2,3,4,5,6]
l.pop(5) # It means delete the number in index 5 and if you will not give any index number in the pop() than it will delete the last index because if default index is (-1)
print(l) # Output: [1, 2, 3, 4, 5]
print()

# clear()
l=[1,2,3,4,5]
l.clear()
print(l) # It will give you [] empty list because clear is used to clear all the data of list.
print()

# Operations on Lists
# Arithmetic Operators
L1=[1,2,3,4,5]
L2=[6,7]
print(L1+L2) # Output: [1, 2, 3, 4, 5, 6, 7]
print(L1*2) # Output: [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

# Membership Operators
L1=[1,2,3]
print(2 in L1) # Output: True

# Loops
L1 =[1,2,3,4,5]
for i in L1:
  print(i) 
# Output:1
#        2
#        3
#        4
#        5

  
# Disadvantages of Python List
