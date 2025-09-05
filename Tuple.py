# Tuples: A tuple in Python is similar to a list. The different between the tuple and list is that we cannot change elements of tuple because it is immutable but we can change the elements of list because it is mutalble.
# Characterstics of tuples are:
# Ordered 
# Unchangeble
# Allows duplicate

# Creating a Tuple
# Empty
t1=()
print(t1)

# Creating a tuple with a single item
t2=(2,)
print(t2)

# Homogeneous Tuple
t3=(1,2,3,4,5)
print(t3)

# Hetrogeneous Tuple
t4=(1,'Hello',True,3+4j)
print(t4)

# 2D tuple 
t= (1,2,3,(4,5))
print(t)

# Using type conversion
t5=tuple('hello')
print(t5)

# Accessing items
# Indexing
t6=(5,10,15,20)
print(t6[1])
print(t6[-1])

# Slicing
print(t6[1:3])

# Editing items
# Tuple cannot be edited because tuple is immutable.

# Adding items
# Even you can not add in the tuple because tuple is immutable.

# Deleting items
# You can delete whole tuple using del tuple_name, you are unable to delete the elements of tuple again same reason.

# Operations on Tuples
# Arithmetic Operators (+ and *)
t7=(1,2,3)
t8=(3,4,5)
print(t7+t8)
print(t7*3)

# Membership 
print(1 in t7)

# Loop 
for i in t7:
  print(i)

# Tuple Function
T=(1,2,3,4,5)
print(len(T))
print(sum(T))
print(min(T))
print(max(T))
print(sorted(T))
print(sorted(T,reverse=True))
print(T.count(1))
print(T.index(5))

# Unnpacking tuple
a,b,c=(1,2,3)
print(a,b,c)

# zipping tuples
a=(1,2,3,4,5)
b=(6,7,8,9,10)
print(tuple(zip(a,b)))
