# ------------------------------------------------------------------------
# ######################## Assignments 69 => 71 ##########################
# ------------------------------------------------------------------------

# ######################## Assignment 1 #########################

values = (0, 1, 2)

if any(values):

  my_var = 0

my_list = [True, 1,  1, ["A", "B"], 10.5, my_var]

if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):

  print("Good")

else:

  print("Bad")

# "Good"

# ######################## Assignment 2 #########################

v = 40

my_range = list(range(v))

print(sum(my_range, v) + pow(v, v, v))  # 820

# ######################## Assignment 3 #########################

n = 20

l = list(range(n))

if round(sum(l) / n) == max(0, 3, 10, 2, -100, -23, 9):

  print("Good")

# Output => Good

# ######################## Assignment 4 #########################

def my_all(args) :
  count = 0
  for num in args :
    if bool(num) == True:
      count += 1
  if count == len(args) :
    return True
  else :
    return False

# my_all
print(my_all([1, 2, 3])) # True
print(my_all([1, 2, 3, []])) # False

##################################

def my_any(args) :
  count = 0
  for num in args :
    if bool(num) == True:
      count += 1
  if count >= 1 :
    return True
  else :
    return False

# my_any
print(my_any([0, 1, [], False])) # True
print(my_any([(), 0, False])) # False

##################################

def my_min(args) :
  
    low = args[0]
    for i in args:
        if i < low:
            low = i
    return low

# my_min
print(my_min([10, 100, -20, -100, 50])) # -100
print(my_min((10, 100, -20, -100, 50))) # -100

##################################

def my_max(args) :
  
    max = args[0]
    for i in args:
        if i > max:
            max = i
    return max

# my_max
print(my_max([10, 100, -20, -100, 50, 700])) # 700
print(my_max((10, 100, -20, -100, 50, 700))) # 700

# ------------------------------------------------------------------------
# ######################## Assignments 72 => 75 ##########################
# ------------------------------------------------------------------------

# ######################## Assignment 1 #########################

# Output
# "Eman"
# "Ahmed"
# "Sameh"
# "Osama"

# --------- with Predefined Function ---------

friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]

def remove_chars(string) :
  return string[1:-1]

cleaned_list  = map(remove_chars , friends_map)

for string in cleaned_list  :
    print(string)

# --------- with lambda Function ---------

friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]

cleaned_list  = map(lambda string : string[1:-1] , friends_map)

for string in cleaned_list  :
    print(string)

# ######################## Assignment 2 #########################

# Output
# "Wessam"
# "Essam"

# --------- with Predefined Function ---------

friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]

def get_names(name) :
  return name.endswith("m")

names = filter(get_names , friends_filter)

for name in names :
    print(name)

# --------- with lambda Function ---------

friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]

names = filter(lambda name : name.endswith("m") , friends_filter)

for name in names :
    print(name)

# ######################## Assignment 3 #########################

# Output
# 96

# --------- with Predefined Function ---------

from functools import reduce

nums = [2, 4, 6, 2]
def Multiply(n1 , n2) :
  return n1 * n2 

result = reduce( Multiply , nums)

print( result )

# --------- with lambda Function ---------

from functools import reduce
nums = [2, 4, 6, 2]

result = reduce( lambda n1,n2 : n1 * n2 , nums)
print( result )

# ######################## Assignment 4 #########################

# Output
# "50 - JavaScript"
# "52 - Python"
# "53 - PHP"
# "55 - CSS"
# "56 - HTML"

# -------- first method --------

skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")

skills_counter = enumerate(reversed(skills) , 50)

for key ,value in skills_counter :
  if type(value) == int :
    continue
  else :
    print(f"{key} - {value}")

# -------- second method --------

skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")

skills_list = list(skills)
skills_list.reverse()
counter = 50

for skill in skills_list :
  if type(skill) == int or type(skill) == float :
    counter += 1
    continue
  else :
    print(f"{counter} - {skill}")
    counter += 1

# ############################# End ###############################