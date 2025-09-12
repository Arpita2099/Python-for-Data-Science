# Dictionary Comprehensions
print({i: i**2for i in range(1,11)})
# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

# using existind dictionary
distances={'Kathmandu':500,'Pokhara':200,'Chitwan':150}
print({key:value*0.62 for (key,value) in distances.items()})
# Output: {'Kathmandu': 310.0, 'Pokhara': 124.0, 'Chitwan': 93.0}

# Using Zip function
days=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
temp_c=[30.5,32.0,31.5,29.0,28.5,27.0,26.5]
print({i:j for (i,j) in zip(days,temp_c)})
# Output: {'Sunday': 30.5, 'Monday': 32.0, 'Tuesday': 31.5, 'Wednesday': 29.0, 'Thursday': 28.5, 'Friday': 27.0, 'Saturday': 26.5}

# Using if condition
products={'phone':10000,'laptop':0,'tablet':20000,'desktop':0}
print({key:value for (key,value) in products.items() if value>0})
# Output: {'phone': 10000, 'tablet': 20000}

# Nested Dictionary Comprehensions
print({i:{j:i*j for j in range(2,11)} for i in range(2,5)})
# Output: {2: {2: 4, 3: 6, 4: 8, 5: 10, 6: 12, 7: 14, 8: 16, 9: 18, 10: 20}, 3: {2: 6, 3: 9, 4: 12, 5: 15, 6: 18, 7: 21, 8: 24, 9: 27, 10: 30}, 4: {2: 8, 3: 12, 4: 16, 5: 20, 6: 24, 7: 28, 8: 32, 9: 36, 10: 40}}
