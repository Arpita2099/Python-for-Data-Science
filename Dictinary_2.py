# Dictionary Operation
# Membershp Operatons
s={'a':1,'b':2,'c':3}
print('a' in s) # Output: True

# Iteration
for k in s:
    print(k,s[k])   
# Output: a 1
#         b 2   
#         c 3

# Dictionar Functions

# len/sorted
len(s) # Output: 3
sorted(s) # Output: ['a', 'b', 'c'] 

# items/keys/values
print(s.items()) # Output: dict_items([('a', 1), ('b', 2), ('c', 3)])s
print(s.keys()) # Output:dict_keys(['a', 'b', 'c'])    
print(s.values()) # Output: dict_values([1, 2, 3])

# update 
s.update({'d':4})
print(s) # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4} 
s.update(e=5)
print(s) # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5} 

# get
print(s.get('a')) # Output: 1
print(s.get('f')) # Output: None
print(s.get('f',6)) # Output: 6
print(s) # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# setdefault
print(s.setdefault('a',10)) # Output: 1     
print(s.setdefault('f',6)) # Output: 6
print(s) # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

