rows = int(input('enter number of rows'))

for i in range(1,rows+1):
  for j in range(1,i+1):
    print('*',end='')
  print()

row=int(input("Enter number of row: "))
for i in range(1,row+1):
  for j in range(1,i+1):
    print("*",end='')
  print()

# Second Question:
row=int(input("Enter the row: "))
for i in range(1+row+1):
  for j in range(1,i+1):
    print(j,end='')
  print()

# Loop Control Statement

# Break: Search is an example of break which is also known as linear searching.
for i in range(1,11):
  if i==6:
    break
  print(i) # It will give output: 1-5 only.

# Find the prime number and the range is given by the user.
lower=int(input("Enter a lower number: "))
upper=int(input("Enter a upper number: "))
for i in range(lower,upper+1):
  for j in range(2,i):
    if i%j==0:
      break
  else:
    print(i)
    
# Continue: Skip product is the example of continue in real life.
for i in range(1,11):
  if i==5:
    continue
  print(i) # It will give output: 1-10 except 5.
  
# Pass
for i in range(1,11):
  pass # If you do not want to get error or do not have any code than you can use pass.
