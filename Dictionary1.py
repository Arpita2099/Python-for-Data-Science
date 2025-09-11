# 2D dictionary
s={
    'name':'Arpita',
    'college':'PGS',
    'Tri': 'Third Trimester',
    'Subject':{
        'NET-100':100,
        'TECH-100': 99,
        'PRG-200': 99
    }
}
print(s)
# Output: {'name': 'Arpita', 'college': 'PGS', 'Tri': 'Third Trimester', 'Subject': {'NET-100': 100, 'TECH-100': 99, 'PRG-200': 99}}

# Using sequence and dic function
D=dict([(1,1),(2,2),(3,3)])
print(D)
D1=dict([('Name','Arpita'),('Title','Sah')])
print(D1)
#Output: {1: 1, 2: 2, 3: 3}
#Output: {'Name': 'Arpita', 'Title': 'Sah'}

# duplicate keys
# If we will print this, then this will show error
# D2={'name':'Arpita','name':'Arpi'}
# print(D2)

# mutuable items as keys
# my_dict={'name':'Washton Sah','Age':13}
# print(my_dict[0])
my_dict={'name':'Washton Sah','Age':13}
print(my_dict['name'])
print(my_dict.get('Age'))
# Output: Washton Sah
# Output: 13

# Adding Key-Value Pair
D['gender']='male'
print(D)
D1['weight']=72
print(D1)
# Output: {1: 1, 2: 2, 3: 3, 'gender': 'male'}
# Output: {'Name': 'Arpita', 'Title': 'Sah', 'weight': 72}

# How can we remove key-value pair
d= {'Name': 'Arpita',5:6, 'Title': 'Sah', 'weight': 72}
# pop
d.pop(5)
print(d)
# Output: {'Name': 'Arpita', 'Title': 'Sah', 'weight': 72}

# popitem
d.popitem()
print(d)
# Output: {'Name': 'Arpita', 'Title': 'Sah'}

# del
del d['Name']
print(d)
# Output: {'Name': 'Arpita', 'Title': 'Sah'}

# clear
d.clear()
print()

# Editing Key-value pair
s['Subject']['NET-100']=99
print(s)
# Output: {'name': 'Arpita', 'college': 'PGS', 'Tri': 'Third Trimester', 'Subject': {'NET-100': 99, 'TECH-100': 99, 'PRG-200': 99}}

