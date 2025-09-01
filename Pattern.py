# *
# **
# ***
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
