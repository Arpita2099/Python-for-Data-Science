# List comprehension: It provides a concise way of creating a lists.

# Syntax 
# newlist=[expression for item in iterable if condition== True]

#  Some of the advantage of list comprehension.
# More time-efficient and space-efficient than loop.
# It required fewer lines of code.
# It transforms iterative statement into a formula.

# Adding number 1-10 using loop
L=[]
for i in  range(1,11):
  L.append(i)
print(L)

# Using List comprehension
L=[]
L=[i for i in range(1,11)]
print(L)

# Scalar multiplication of a vector using loop
v=[1,2,3]
s=4
a=[]
for i in v:
  a.append(i*s)
print(a)

# Using List comprehension
v=[1,2,3]
s=4
a=[]
a=[i*s for i in v]
print(a)

# Add Squares
L=[1,2,3,4,5]
print([i**2 for i in L])

# Find all the number which is divisible by 3 and 5 from 1-50
print("Number divisible by 3 and 5: ",[i for i in range(1,51) if i%3==0 and i%5==0])

# Find the language which start with J
languages=["C","Java","Javascript","Python"]
print("Language start with J is: ",[i for i in languages if i.startswith('J')])

# Nested if with list comprehension
Fruits=['Apple','Avocado','Banana','Orange']
Fruits1=['Apple','Avocado','Banana','Orange','Anar']
print([fruit for fruit in Fruits if fruit.startswith('A') if fruit in Fruits])

# Print a 3*3 matrix list comprehension -> nested list comprehension
print([[i*j for i in range(1,4)] for j in range(1,4)])

# Cartesian products -> List Comprehension on 2 lists together.
L1=[1,2,3]
L2=[4,5,6]
print([i*j for i in L1 for j in L2])

# 2 way to traverse a List
# itemwise
l=[1,2,3,4,5]
for i in l:
  print(i)
  
# indexwise
l=[1,2,3,4,5]
for i in range(0,len(l)):
  print(i)
print()

l=[1,2,3,4,5]
for i in range(0,len(l)):
  print(l[i])

# Zip() Function Example:
L1=[1,2,3,4]
L2=[-1,-2,-3,-4]
print(list(zip(L1,L2)))
# Output: [(1, -1), (2, -2), (3, -3), (4, -4)]
