# String Function
# isalnum(): If you will give string alpha_numeric than I will give True. For instance,
print("Arpita750".isalnum())
print('@arpita750'.isalnum()) # It will give output: False because it have @ which is not the alpha_numeric.

# isalpha(): It will give true to the enter string if it contain alphabetical otherwise, it will give false.
print("ArpitaSah".isalpha()) # True
print("arpita345".isalpha()) # False

# isdigit(): It will return true if the given string contain digit on it otherwise, it will returns false.
print('1234'.isdigit()) # True
print('arpi4567'.isdigit()) # False

# isidentifier(): It will return true if the string contain is written in the form of identifier otherwise it will return false.
print('1age'.isidentifier()) # False
print('age1'.isidentifier()) # True

# Split()/Join(): Split(): It is used to split the string into the list and joint(): It is used to join the listed string into the string together.
print('Hi I am Arpita and I started Python on Data Science'.split()) # Output: ['Hi', 'I', 'am', 'Arpita', 'and', 'I', 'started', 'Python', 'on', 'Data', 'Science']
print('Hi I am Arpita and I started Python on Data Science'.split(i)) # Output: ['Hi I am Arpita and I started Pyt', 'on on Data Science']
print(" ".join(['Hi', 'I', 'am', 'Arpita', 'and', 'I', 'started', 'Python', 'on', 'Data', 'Science'])) #Output: Hi I am Arpita and I started Python on Data Science

# replace(): It will replce the string with the new written string.
print('Hey my name is Arpita Sah'.replace('Arpita','Arpi')) # Output: Hey my name is Arpi Sah

#sptip(): It will remove the space after string end and print the string.
print("Arpita            ".strip()) # Output: Arpita
print("Arpita Sah           ".strip()) # Output: Arpita Sah
