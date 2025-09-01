# Sum of digit of code:
Code=int(input("Enter any digit of Code and get the sum of that digit of Code: "))
sum=0
while Code>0:
    R=Code%10
    sum=sum+R
    Code=Code//10
print(sum)

#Assignment
# Guess ATM Pin
ATM_Pin=2025
attempts=0
while attempts<3:
    Guess_Pin=int(input("Enter the four digit ATM pin: "))
    if(Guess_Pin==ATM_Pin):
        print("Your ATM pine is Right")
        break
    else:
        attempts=attempts+1
        if attempts<3:
            print("Your enter pine is wrong, Try again")
        else:
            print("You enetr 3 time wrong pine nd your ATM block.")
print()

# Dice rooling
count=0
while True:
    Dice_number=int(input("Enter any number between 1-6: "))
    count=count+1
    if Dice_number==6:
        print("You got 6 congratulation.")
        print(f"You got 6 in {count} attempts.")
        break
    else:
        print("Try Again!.")
print()
# Reverse number using while loop
num=int(input("Enter any number: "))
while num>=0:
    print(num)
    num=num-1
print()

# For loop 
# 10 times clapping. Healthy and not Healthy.
clapp=int(input("Enter the number of clapping: "))
count=0
for i in range(clapp):
    count=count+1
if count==10:
    print("Person are Healthy.")
else:
    print("Person are not Healthy.")
print()

# Sum and average of even Number 1-50
sum=0
count=0
for a in range(1,51):
    if a % 2 ==0:
        sum=sum+a
        count=count+1
ave=sum/count
print("Sum of even number between 1-50 is: ",sum)
print("Average of even number between 1-50 is: ",ave)
print()

# Sum of 1-50 which is divisible by 3 and 5.
sum=0
for i in range(1,51):
    if i%3==0 and i%5==0:
        sum=sum+1
print("Sum of 1-50 number divisible by 3 and 5:", sum)
print()

# 1-100 sum and divisible by 2,4, and 6. If sum is not than print the only divisible numbers.
sum=0
for i in range(1,101):
    if i%2==0 and i%4==0 and i%6==0:
        sum=sum+i
print("The sum of all divisible number by 2,4,and 6 is: ",sum)
print()
