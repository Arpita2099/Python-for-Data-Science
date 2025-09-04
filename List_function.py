# List Function
L=[1,2,3,4,10]
print(len(L))
print(min(L))
print(max(L))
print(sorted(L))
print(sorted(L,reverse=True))

# count
L=[1,2,3,1,4,1,5]
print(L.count(1))
print()

# index
L=[1,2,3,4,10]
print(L.index(1))

# reverse
L=[1,2,3,4,10]
# Permanently Reverse
L.reverse()
print(L)

# sort/sorted
L=[1,2,4,5,6,3]
print(sorted(L))
print(L)
L.sort() # Permanently sort
print(L)

# copy -> shallow
L = [1,2,3,4,5]
print(L)
print(id(L))
L1 = L.copy()
print(L1)
print(id(L1))

