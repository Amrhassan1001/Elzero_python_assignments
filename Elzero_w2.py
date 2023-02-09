#-----------------------------------------------------------------------
######################### Assignments 11 => 18 #########################
#-----------------------------------------------------------------------

######################### Assignment 1 #########################

# "Hello 'Osama', How You Doing \ """ Your Age Is "38"" + And Your Country Is: Egypt
name = "amr"
age = "18"
country = "Egypt"

print("Hello '"+name+"', How You Doing "'\\ """ Your Age Is "'+ age +'"" + And Your Country Is:'+ country , )


######################### Assignment 2 #########################
 
#  "Hello 'Osama', How You Doing \
# """ Your Age Is "38"" +
# And Your Country Is: Egypt

print("Hello '"+name,"', How You Doing \n "'\\ """ Your Age Is "'+ age ,'"" + \n And Your Country Is:'+ country , )

######################### Assignment 3 #########################

name = 'Elzero'

# Needed Output
# Second Letter Is "l"
# Third Letter Is "z"
# Last Letter Is "o"

print("Second Letter Is \"" + name[1] +"\"")
print("Third Letter Is \"" + name[2] +"\"")
print("Last Letter Is \"" + name[3] +"\"")

######################### Assignment 4 #########################

name = 'Elzero'

# Needed Output
# "lze"
# "Ezr"
# "rzE"

print("Second Letter Is \"" + name[1:4] +"\"")
print("Third Letter Is \"" + name[0:5:2] +"\"")
print("Last Letter Is \"" + name[4::-2] +"\"")

######################### Assignment 5 #########################

name = "#@#@Elzero#@#@"

# Needed Output
# Elzero

print(name.strip("#@"))

######################### Assignment 6 #########################

num1 = "9"
num2 = "15"
num3 = "130"
num4 = "950"
num5 = "1500"

# Needed Output
# 0009
# 0015
# 0130
# 0950
# 1500

print(num1.zfill(4))
print(num2.zfill(4))
print(num3.zfill(4))
print(num4.zfill(4))
print(num5.zfill(4))

######################### Assignment 7 #########################

name_one = "Osama"
name_two = "Osama_Elzero"

# Needed Output
# @@@@@@@@@@@@@@@Osama
# @@@@@@@@Osama_Elzero

print(name_one.rjust(20,"@"))
print(name_two.rjust(20,"@"))

######################### Assignment 8 #########################

name_one = "OSamA"
name_two = "osaMA"

# Needed Output
# osAMa
# OSAma

print(name_one.swapcase())
print(name_two.swapcase())

######################### Assignment 9 #########################

msg = "I Love Python And Although Love Elzero Web School"

# Needed Output
# 2

print(msg.count("Love"))

######################### Assignment 10 #########################

name = "Elzero"

# Needed Output
# 2

print(name.index("z"))

######################### Assignment 11 #########################

msg = "I <3 Python And Although <3 Elzero Web School"

# Needed Output
# I Love Python And Although <3 Elzero Web School

print(msg.replace("<3","Love",1))

######################### Assignment 12 #########################

msg = "I <3 Python And Although <3 Elzero Web School"

# Needed Output
# I Love Python And Although Love Elzero Web School

print(msg.replace("<3","Love"))

######################### Assignment 13 #########################

name = "Osama"
age = 38
country = "Egypt"

# Needed Output Using f""
# My Name Is Osama, And My Age Is 38, And My Country Is Egypt

print(f"My Name Is {name}, And My Age Is {age}, And My Country Is {country}")

############################# End ###############################
