#-----------------------------------------------------------------------
######################### Assignments 19 => 20 #########################
#-----------------------------------------------------------------------

######################### Assignment 1 #########################

print(type(10))
print(type(-1))
print(type(12.0))
print(type(1+5j))



# ######################### Assignment 2 #########################
 
a = 1+2j

# Print Imaginary Part Here
# Print Real Part Here

print(a.imag)
print(a.real )

# ######################### Assignment 3 #########################

num = 10

# Needed Ouput
# 10.0000000000

# By formatting 
print("{:.10f}".format(num))

# ######################### Assignment 4 #########################

num = 159.650

# Needed Output
# 159
# <class 'int'>

print(int(num))
print(type(int(num)))


# ######################### Assignment 5 #########################

# 100 ? 115 = -15
# 50 ? 30 = 1500
# 21 ? 4 = 1
# 110 ? 11 = 10
# 97 ? 20 = 4

print(100 - 115)
print(50 * 30)
print(21 % 4)
print(110 // 11)
print(97 // 20)

#-----------------------------------------------------------------------
######################### Assignments 21 => 23 #########################
#-----------------------------------------------------------------------

######################### Assignment 1 #########################

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# Needed Output
# "Osama" => Method One
# "Osama" => Method Two
# "Mahmoud" => Method One
# "Mahmoud" => Method Two

print(friends[0])
print(friends.pop(0))
print(friends[-1])
print(friends.pop(-1))

# ######################### Assignment 2 #########################

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# Needed Output
# "Osama", "Sayed", "Mahmoud"
# "Ahmed", "Ali"

print(friends[::2])
print(friends[1::2])

# ######################### Assignment 3 #########################

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# Needed Output
# "Ahmed", "Sayed", "Ali",
# "Ali", "Mahmoud"

print(friends[1:4])
print(friends[-2:])


# ######################### Assignment 4 #########################

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# Needed Output
# ["Osama", "Ahmed", "Sayed", "Elzero", "Elzero"]

friends[-2:] = ["Elzero" , "Elzero"]

print(friends)

# ######################### Assignment 5 #########################

friends = ["Osama", "Ahmed", "Sayed"]

# Needed Output
# ["Nasser", "Osama", "Ahmed", "Sayed"]
# ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]

friends.insert(0 ,"Nasser")
print(friends)
friends.append("Salem")
print(friends)

# ######################## Assignment 6 #########################

friends = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]

# Needed Output
# ["Ahmed", "Sayed", "Salem"]
# ["Ahmed", "Sayed"]

friends[0:2] = []
print(friends)
friends[2:] = []
print(friends)

# or By remove Method 

# ######################### Assignment 7 #########################

friends = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]

# Needed Output
# ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]

friends = friends + employees + school 
print(friends)

# ######################### Assignment 8 #########################

friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]

# Needed Output
# ['Ahmed', 'Eman', 'Ramy', 'Samah', 'Sayed', 'Shady']
# ['Shady', 'Sayed', 'Samah', 'Ramy', 'Eman', 'Ahmed']

friends.sort()
print(friends)
friends.sort(reverse= True)
print(friends)

# ######################### Assignment 9 #########################

friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]

# Needed Output
# 6

print(len(friends))

# ######################### Assignment 10 #########################

technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]

# Needed Output
# Django
# Web

print(technologies[4][0]) 
print(technologies[4][-1]) 

#-----------------------------------------------------------------------
######################### Assignments 24 => 25 #########################
#-----------------------------------------------------------------------

# ######################### Assignment 1 #########################

# Needed Output

# "Osama"
# <class 'tuple'>

name = "Osama",

print(name[0])
print(type(name))

# ######################### Assignment 2 #########################

friends = ("Osama", "Ahmed", "Sayed")

# Needed Output

# ("Elzero", "Ahmed", "Sayed")
# <class 'tuple'>
# 3 Elements

friends = list(friends)
friends[0] = 'Elzero'
friends = tuple(friends)

print(friends)
print(type(friends))
print(f"{len(friends)} Elements")

# ######################### Assignment 3 #########################

# nums = (1, 2, 3)
# letters = ("A", "B", "C")

# # Needed Output

# # nums_and_letters_one = (1, 2, 3, "A", "B", "C")
# # 6 Elements

# nums_and_letters_one = nums + letters

# print(nums_and_letters_one)
# print(f"{len(nums_and_letters_one)} Elements")

# # ######################### Assignment 4 #########################

# my_tuple = (1, 2, 3, 4)

# # Needed Output

# # 1
# # 2
# # 4

# a,b, _ ,c = my_tuple

# print (a)
# print (b)
# print (c)

# # ############################# End ###############################


