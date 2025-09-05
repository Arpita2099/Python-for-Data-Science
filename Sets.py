# Sets
# Set is an unordered collectionn of iteams. Every set element is unique (no duplicates) and must be immutable (can not be changed). However, a set itself is mutable. We can add or remove iteams from it.
# Set can also be used to perform mathematical set operations like union, intersection, symmetric difference, etc.
# Characterstics of Sets
# Unordered
# Mutable
# No Duplicates
# Can't contain mutable data types

# Creating Sets
# empty
s=set()
print(s)

# 1D and 2D sets
s1={4,6,8}
print(s1)
# In set you can not print the 2D set.

# Hetrogeneous Sets
s3={1, 'help',4.5,(1,4,6)}
print(s3) 

# Using Type conversion
s4=set([7,9,3])
print(s4)

# Note: Set can not have mutable items

# Ordered do not mattern in the set. For instance,
s1={1,2,3}
s2={3,2,1}
print(s1==s2) # It will give Output: True

# Accessing the sets: Accessing items are not allowed in the set because it is unordered.
# Editing items in sets: You can not edit items in the set.

# Adding items in sets
s={1,2,3,4,5}
#add
s.add(6) # and can add at anywere.
#update
print(s) 

# Update
s.update([7,8,9,10])
print(s)

# Deleting items in sets
#S={10,20,30}
#del S
#print(S)

# discard: It will not through an error
s.discard(10)
print(s)

# remove; It will through an error if number are not their.
s.remove(9)
print(s)

# pop 
s.pop()
print(s)

# clear()
s.clear()
print(s)

# Operations of sets
s1={1,2,3,4,5}
s2={1,3,5,7,9}
# Union(|)
print(s1|s2)
# Intersection(&)
print(s1&s2)

# Difference(-)
print(s1-s2)
print(s2-s1)

# Symmetric Difference(^)
print(s1^s2)

# Membership Test
print(1 in s1)
print(1 not in s2)

# Iteration
for i in s2:
  print(i)
