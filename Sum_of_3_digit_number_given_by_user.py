# Find the sum of three digit number enter by user.
User_number=int(input("Enter any 3 digit number:")) # It will ask the 3 digit number from user.
sum=0 #Initial sum value is assign 0
while User_number>0: # Loop will run untill the User_number is greater than 0.
  rem=User_number%10 # It will give the remender value means last value.
  sum=sum+rem #It will add the last value and provide the sum of 3 digits number.
  User_number=User_number//10 # It will provide the integer division of digit.
print("Sum of 3 digit number is: ",sum) # Lastly, you will get the output by adding 3 digit number over here.
  
