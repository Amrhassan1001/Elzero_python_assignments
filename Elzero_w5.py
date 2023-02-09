#-----------------------------------------------------------------------
######################### Assignments 33 => 37 #########################
#-----------------------------------------------------------------------

######################### Assignment 1 #########################

# Needed Output

# True
# True
# True
# True
# False
# False
# False
# False

print(bool("Elzero"))
print(bool(100))
print(bool([1,2,5,8,6,7]))
print(bool(True))
print(bool(""))
print(bool(0))
print(bool(False))
print(bool(None))

# ######################### Assignment 2 #########################

html = 80
css = 60
javascript = 70

# Needed Output
# True

print(bool(html > 50 and css > 50 and javascript > 50 ))


# # ######################### Assignment 3 #########################

num_one = 10
num_two = 20
num = 20

# Needed Output
# True
# False

print(bool(num > num_one or num > num_two))
print(bool(num > num_one and num > num_two))



# # ######################### Assignment 4 #########################

num_one = 10
num_two = 20

# Needed Output
# 30
# 27000
# 1000
# 200.0
# <class 'str'>

result = num_one + num_two
print(result)

result **= 3
print(result)

result %= 26000
print(result)

result /= 5
print(result)

print(type(result))
print(type(str(result)))

#-----------------------------------------------------------------------
######################### Assignments 38 => 40 #########################
#-----------------------------------------------------------------------

# ######################### Assignment 1 #########################

# Input
# "     osAmA   "

# Needed Output
# "Hello Osama, Happy To See You Here."

name = input("put your name  ").strip().capitalize()
print(f"Hello {name}, Happy To See You Here.")

# ######################### Assignment 2 #########################

# Inputs

# 16 # Input One
# 24 # Input Two

# # Needed Output

# "Hello Your Age Is Under 16, Some Articles Is Not Suitable For You" # If Age < 16
# "Hello Your Age Is {Age_Value_If_Larger_Than_16}, All Articles Is Suitable For You" # If Age Is 16+

age = int(input("What is Your Age ?  ").strip())

if age < 16 :
    print('"Hello Your Age Is Under 16, Some Articles Is Not Suitable For You"')

else :
    print(f'"Hello Your Age Is {age} , All Articles Is Suitable For You"')

######################### Assignment 3 #########################

# Inputs

# "Osama" # First Name
# "Mohamed" # Second Name

# Needed Output

# "Hello {First_Name} {First_Letter_From_Second_Name}." # Example "Osama M."

First_Name = input(' your First name ?  ').strip().capitalize() 
Second_name = input(' your Second name ?  ').strip().capitalize()

print(f'"Hello {First_Name} {Second_name[0]}."')

######################### Assignment 4 #########################

# Inputs

# "Osama@Nn.Sa" # Email

# Needed Output

# "Your Name Is Osama"
# "Email Service Provider Is nn"
# "Top Level Domain Is sa"

Email = input('your Email ?   ').strip().lower()

print(f'"Your Name Is {Email[0:Email.index("@")].capitalize()}"')

print(f'"Email Service Provider {Email[Email.index("@") + 1 :Email.index(".")]}"')

print(f'"Top Level Domain Is {Email[Email.index(".") + 1 : ]}"')


# ############################# End ###############################