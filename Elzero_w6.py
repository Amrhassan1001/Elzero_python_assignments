#-----------------------------------------------------------------------
######################### Assignments 41 => 46 #########################
#-----------------------------------------------------------------------

# ######################### Assignment 1 #########################

# Inputs

# Needed Output
# [num1 20] [operation +] [num2]
# Example One 20 + 40 = 60
# Example Two 20 * 40 = 800

num1 = int(input('Put the first number => ').strip())
num2 = int(input('Put the second number => ').strip())

operation = input(' the operator is of the Arithmetic operation => ').strip()

if operation == "+" :
  print ( num1 + num2 )

elif operation == "-" :
  print ( num1 - num2 )

elif operation == "*" :
  print ( num1 * num2 )

elif operation == "/" :
  print ( num1 / num2 )

elif operation ==  "%" :
  print ( num1 % num2 )

else : print("Wrong Operator")


# ######################### Assignment 2 #########################

# Needed Output
# "App Is Suitable For You" # If Age Larger Than 6
# "App Is Not Suitable For You" # if Age Smaller Than 16
# age = 17

age = int(input("Enter Your Age  "))
print("App Is Suitable For You" if age >= 16 else "App Is Not Suitable For You")

# ######################### Assignment 3 #########################

# Input Example 38

# Needed Output
# "Your Age In Months Is 456 Months" # Months Example
# "Your Age In Weeks Is 1824 Weeks" # Weeks Example

age = int(input('Enter your age .   '))

if  age > 10 and age < 100 :
  months = age * 12
  weeks = months * 4
  days = weeks * 7
  hours = days * 24
  minutes = hours * 60
  seconds = minutes * 60

  print(f'Your Age In Months Is {age} years')
  print(f'Your Age In Months Is {months:,} months')
  print(f'Your Age In Months Is {days:,} days ')
  print(f'Your Age In Months Is {hours:,} hours ')
  print(f'Your Age In Months Is {minutes:,} minutes ')
  print(f'Your Age In Months Is {seconds:,} seconds ')

else : print('Your Age Is Not Supported')

# ######################### Assignment 4 #########################

# Input Example One "Egypt"
# Input Example Two "Ghana"
# # Needed Output
# "Your Country Eligible For Discount And The Price After Discount Is $70" # Egypt Example
# "Your Country Not Eligible For Discount And The Price Is $100" # Ghana Example

country = input("Input Your Country   ").strip().capitalize()
countries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA", "USA", "Bahrain", "England"]
price = 100
discount = 30

if country in countries :

  print(f'Your Country Eligible For Discount And The Price After Discount Is ${ price - discount} ')

else : 
  
  print(f'Your Country Not Eligible For Discount And The Price Is ${ price } ')

# ############################# End ###############################

