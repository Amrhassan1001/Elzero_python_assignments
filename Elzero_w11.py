# ------------------------------------------------------------------------
# ######################## Assignments 76 => 78 ##########################
# ------------------------------------------------------------------------

# ######################## Assignment 1 #########################

import random 

print(f"Random Number Between 10 And 50 => {random.randrange(10,51)} ")
print(f"Random Even Number Between 2 And 10 => {random.randrange(2,11,2)} ")
print(f"Random Odd Number Between 1 And 9 => {random.randrange(1,10,2)} ")
print(dir(random))

# ######################## Assignment 2 #########################

import sys
sys.path.append(f"D:\\Amr\\python\\python")

import my_mod 

print(my_mod.say_hallo("amr"))
print(my_mod.say_welcome("amr"))

# ######################## Assignment 3 #########################

from my_mod import say_welcome 

print(say_welcome("amr"))

# ######################## Assignment 4 #########################

from my_mod import say_welcome as new_welcome

print(new_welcome("amr"))

# ------------------------------------------------------------------------
# ######################## Assignments 79 => 80 ##########################
# ------------------------------------------------------------------------

# ######################## Assignment 1 #########################

import datetime 

today = datetime.datetime.now().date()
date =  datetime.datetime(2021, 6, 25).date()

print(f"The Date Is {date}")
print(f"Today Is {today}")
print(f"Days From {date} To {today} => {(today - date).days}")

# ######################## Assignment 2 #########################

# Today Is "2021, 8, 10"
# "2021-08-10"
# "Aug 10, 2021"
# "10 - Aug - 2021"
# "10 / Aug / 21"
# "10 / August / 2021"
# "Tue, 10 August 2021"

print(datetime.datetime.now().date())
print(datetime.datetime.now().strftime("%b %d, %Y"))
print(datetime.datetime.now().strftime("%d - %b - %Y"))
print(datetime.datetime.now().strftime("%d / %b / %y"))
print(datetime.datetime.now().strftime("%d / %B / %Y"))
print(datetime.datetime.now().strftime("%a, %d %B %Y"))

# ------------------------------------------------------------------------
# ######################## Assignments 81 => 85 ##########################
# ------------------------------------------------------------------------

# ######################## Assignment 1 #########################

def reverse_string(my_string):
  yield my_string[::-1]

for c in reverse_string("Elzero"):
  print(c)

# ######################## Assignment 2 #########################

def my_decorator(func):

  def nested_func() : 
      print("Sugar Added From Decorators")
      func()
      print("####################")

  return nested_func 

@my_decorator
def make_tea():
  print("Tea Created")

@my_decorator
def make_coffe():
  print("Coffe Created")

make_tea()
make_coffe()

# ############################# End ###############################
