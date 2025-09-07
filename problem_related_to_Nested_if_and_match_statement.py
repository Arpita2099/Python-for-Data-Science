# Login Program
# In this login page the email id:arpitasah750@gmail.com along with password=Nepal2082* than it will print the command Welcome.
# else it will print your email and password is wrong.
email=input("Enter your email password: ") # It will ask for your email id.
password=input("Enter your password: ") # It will ask you to input your password.
if email=='arpitasah750@gmail.com' and password=='Nepal2082*': # Here if condition will check that if both the password and email are correct.Then,
  print("Thank you for login, and Welcome.") # It will print Thank you for login, and Welcome.
elif email=='arpitasah750@gmail.com' and password!='Nepal2082*': # Elif condition will check if email is correct and password is incorrect. Then,
  print("Your password is incorrect.") # It will print Your password is incorrect.
  password=input('Enter your password:') # And it will again ask you to input the password.
  if password=='Nepal2082*': # This will check that again enter password is correct. Then,
    print("Your password is right, Welcome!") # Here, it will give output that Your password is right, Welcome!
  else: # Your enter password is again wrong. Then,
    print("I think you didn't remember password!") # It will give output that I think you didn't remember password!
else:
  print("Your email and password both are wrong.") # In here it will give output Your email and password both are wrong. 
                                                   # If your both email and password are incorrect.

# Checking the phase of electric bill using the electric bill calculator. By using match- switch case.
# The condition program is that,1st codn if consumed_unit is(0-100) phase 1: Basic Consumption.
# Calculation for first condition if consumed_unit*5.
# Second condition, if consumed_unit (101-300) phase 2: Moderate Consumption of electricity.
# Calculation for second condition if 100*5+(consumed_unit-100)*7.
# Third condition, if consumed_unit (above 300) phase 3: Highly Consumption of electricity.
# Calculation for second condition if 100*5+200*7+(consumed_unit-300)*10.
consumed_unit = int(input("Enter the number of units you Consumed: "))# Input consumed_unit.
match consumed_unit:
    case u if u <= 100 and u>=0: # Check the first condition.
        Total_bill = u * 5 # Formula of Total_bill
        print(f"Total bill of electricity is: {Total_bill}")#Give the total_bill when meet condition.
        print("Phase 1: Basic Consumption of Electricity.")# Print Pase 1 Output.
    case u if u <= 300 and u>=101: # Check the second condition.
        Total_bill = 100 * 5 + (u - 100) * 7 # Formula of Total_bill
        print(f"Total bill of electricity is: {Total_bill}")#Give the total_bill when meet condition.
        print("Phase 2: Moderate Consumption of Electricity.")# Print Pase 2 Output.
    case u if u > 300: # Check the third condition.
        Total_bill = 100 * 5 + 200 * 7 + (u - 300) * 10 # Formula of Total_bill
        print(f"Total bill of electricity is: {Total_bill}")#Give the total_bill when meet condition.
        print("Phase 3: Highly Consumption of Electricity.")# Print Pase 1 Output.
    case _: # Invalid condition if consumed_unit is in -
        print("Your bill is in negative.")
