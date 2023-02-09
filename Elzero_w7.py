# ------------------------------------------------------------------------
# ######################## Assignments 47 => 50 ##########################
# ------------------------------------------------------------------------

######################## Assignment 1 #########################

# Input
# num = 0
# Needed Output
# "Number 0 Is Not Larger Than 0"

num = int(input('Enter the number larger than 0 .     '))
a = 0

if num > 0:

  while num > 0 : 
    num -=1 
    if num == 6 :
      continue
    if num == 0 :
      break 
    print(num)
    a += 1

  print(f" {a } Numbers Printed Successfully.")  

else :
      print('"Number 0 Is Not Larger Than 0"')

# ######################### Assignment 2 #########################

# Input
# friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]

# Needed Output
# "Mohamed"
# "Shady"
# "Sherif"
# "Friends Printed And Ignored Names Count Is 2"

friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]

num = len(friends)
index = 0
count = 0

while index < num :

  if friends[index].istitle() :
    print(friends[index])
    count += 1
  index += 1

else :
   print(f"Friends Printed And Ignored Names Count Is { num - count }")

# ######################### Assignment 3 #########################

# Code
# skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]

# while skills:

  # Type The Code Here in One Line

# Needed Output
# "HTML"
# "CSS"
# "JavaScript"
# "PHP"
# "Python"

skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]
num = 0
while num < len(skills) : print(f"{skills[num]}") ; num += 1

# ######################### Assignment 4 #########################

my_friends = []
maximum = 4
num = 0
left = 4

while num < maximum :

  the_friend = input("Put the name   ").strip()
  
  if the_friend . islower():
    the_friend . capitalize()
    my_friends.append(the_friend)
    print(f"Friend {the_friend} Added => 1st Letter Become Capital")
    num += 1
    left -= 1
    print(my_friends)
    print("No names left " if left == 0 else f"Names Left in List Is {left}")
    print("# "* 30)

  elif the_friend . istitle():
    my_friends.append(the_friend)
    print(f"Friend {the_friend} Added ")
    num += 1
    left -= 1 
    print(my_friends)
    print("No names left " if left == 0 else f"Names Left in List Is {left}")
    print("# "* 30)

  elif the_friend . isupper(): 
    print ('the name is invalid')
    print("# "* 30)
  
# ------------------------------------------------------------------------
# ######################## Assignments  51 => 55 #########################
# ------------------------------------------------------------------------

######################## Assignment 1 #########################

# Input
# my_nums = [15, 81, 5, 17, 20, 21, 13]

# Needed Output
# "1 => 20"
# "2 => 15"
# "3 => 5"
# "All Numbers Printed"

my_nums = [15, 81, 5, 17, 20, 21, 13]

my_nums.sort(reverse = True)
index = 0

for num in my_nums :

  if num %5 == 0 :
    index += 1
    print (f"{index} => {num}")
    
else :
  print("All Numbers Printed")




######################### Assignment 2 #########################

for i in range(1,21) :

  if i == 6 or i == 8 or i == 12 :
    continue
  print(f"{i}".zfill(2))

print("All Numbers Printed")

######################### Assignment 3 #########################

# Input
# my_ranks = {
#   'Math': 'A',
#   "Science": 'B',
#   'Drawing': 'A',
#   'Sports': 'C'
# }
# # Needed Output
# "My Rank in Math Is A And This Equal 100 Points"
# "My Rank in Science Is B And This Equal 80 Points"
# "My Rank in Drawing Is A And This Equal 100 Points"
# "My Rank in Sports Is C And This Equal 40 Points"
# "Total Points Is 320"

my_ranks = {
  'Math': 'A',
  "Science": 'B',
  'Drawing': 'A',
  'Sports': 'C'
}

total = 0
for subject , degree in my_ranks.items() :
  
  if degree == 'A' :
    print(f"My Rank in {subject} Is A And This Equal 100 Points")
    total += 100

  elif degree == 'B' :
    print(f"My Rank in {subject} Is B And This Equal 80 Points")
    total += 80

  elif degree == 'C' :
    print(f"My Rank in {subject} Is C And This Equal 40 Points")
    total += 40

print(f"Total Points Is {total}")



######################### Assignment 4 #########################

# Needed Output
# "------------------------------"
# "-- Student Name => Ahmed"
# "------------------------------"
# "- Math => 100 Points"
# "- Science => 20 Points"
# "- Draw => 80 Points"
# "- Sports => 40 Points"
# "- Thinking => 100 Points"
# "Total Points For Ahmed Is 340"
# "------------------------------"
# "-- Student Name => Sayed"
# "------------------------------"
# "- Math => 80 Points"
# "- Science => 80 Points"
# "- Draw => 80 Points"
# "- Sports => 20 Points"
# "- Thinking => 100 Points"
# "Total Points For Sayed Is 360"
# "------------------------------"
# "-- Student Name => Mahmoud"
# "------------------------------"
# "- Math => 20 Points"
# "- Science => 100 Points"
# "- Draw => 100 Points"
# "- Sports => 80 Points"
# "- Thinking => 80 Points"
# "Total Points For Mahmoud Is 380"

students = {
  "Ahmed": {
    "Math": "A",
    "Science": "D",
    "Draw": "B",
    "Sports": "C",
    "Thinking": "A"
  },
  "Sayed": {
    "Math": "B",
    "Science": "B",
    "Draw": "B",
    "Sports": "D",
    "Thinking": "A"
  },
  "Mahmoud": {
    "Math": "D",
    "Science": "A",
    "Draw": "A",
    "Sports": "B",
    "Thinking": "B"
  }
}

# first method

for name in students :

  print ("------------------------------")
  print (f"-- Student Name => {name}")
  print ("------------------------------")
  total = 0

  for subjects in students[name] :

    if students[name][subjects] == 'A' :
      print(f"{subjects} => 100 points")
      total += 100

    elif students[name][subjects] == 'B' :
      print(f"{subjects} => 80 points")
      total += 80

    elif students[name][subjects] == 'C' :
      print(f"{subjects} => 40 points")
      total += 40

    elif students[name][subjects] == 'D' :
      print(f"{subjects} => 20 points")
      total += 20
    
  print(f"Total Points For {name} Is {total}")

# second method

for name , grades in students.items() :

  print ("------------------------------")
  print (f"-- Student Name => {name}")
  print ("------------------------------")
  total = 0

  for subjects , degree in grades.items() :

    if degree == 'A' :
      print(f"{subjects} => 100 points")
      total += 100

    elif degree == 'B' :
      print(f"{subjects} => 80 points")
      total += 80

    elif degree == 'C' :
      print(f"{subjects} => 40 points")
      total += 40

    elif degree == 'D' :
      print(f"{subjects} => 20 points")
      total += 20
    
  print(f"Total Points For {name} Is {total}")

# ############################# End ###############################