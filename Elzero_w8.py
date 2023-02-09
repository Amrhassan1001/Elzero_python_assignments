# ------------------------------------------------------------------------
# ######################## Assignments 56 => 59 ##########################
# ------------------------------------------------------------------------

# ######################## Assignment 1 #########################

def calculate(n1 , n2, op ="add" ):

  if op.lower() == "add" or op.lower() == "a" or op == "+" :
    return(n1 + n2) 

  if op.lower() == "subtract" or op.lower() == "s" or op == "-" :
    return(n1 - n2)

  if op.lower() == "multiply" or op.lower() == "m" or op == "*" :
    return(n1 * n2) 

  else :
    return("the operation doesn\'t exist")


print(calculate(10 , 20 , "A"))
print(calculate(10 , 20 , "S"))
print(calculate(10 , 20 , "M"))

# ######################## Assignment 2 #########################

def addition(*nums) :
  sum = 0
  for num in nums:

    if num == 10 :
      continue
    if num == 5 :
      sum -= num 
    else :
      sum += num 
  
  return (sum)


print(addition(10, 20, 30, 10, 15)) # 65
print(addition(10, 20, 30, 10, 15, 5, 100)) # 160

# ######################## Assignment 3 #########################

def show_skills(name , *skills) :

  if len(skills) == 0 :
    print(f"Hello {name} You Have No Skills To Show")
  else : 
    print(f"Hello {name} Your Skills Is")
    for skill in skills :
      print(skill)

show_skills("Amr", "HTML", "CSS", "JS","python")

# ######################## Assignment 4 #########################

def say_hello(name = "Unknown", age = "Unknown", country = "Unknown") :

  return(f"Hello {name} Your Age Is {age} And You Live In {country}")

# ------------------------------------------------------------------------
# ######################## Assignments 60 => 64 ##########################
# ------------------------------------------------------------------------

# # ######################## Assignment 1 #########################

def get_score(**skills) :
    for skill , score in skills.items() :
      print(f"{skill} => {score}")

get_score(Logic=70, Problems=60)

# ######################## Assignment 2 #########################

def get_people_scores(name = "" ,**skills) :

  if len(skills) == 0 :
      print(f"Hello {name} You Have No Scores To Show")

  elif len(name) == 0 :
    for k , v in skills.items() :
      print(f"{k} => {v}")

  else :
    print(f"Hello {name} This Is Your Score Table:")
    for k , v in skills.items() :
      print(f"{k} => {v}")

get_people_scores("Osama", Math=90, Science=80, Language=70)
get_people_scores("Mahmoud", Logic=70, Problems=60)
get_people_scores( Logic=70, Problems=60)
get_people_scores("Ahmed")

# ######################## Assignment 3 #########################


scores_list = { 
  "Math" : 90 ,
  "Science" : 80 ,
  "Language" : 70 }

def get_the_scores(name = "" ,**skills) :

  if len(skills) == 0 :
      print(f"Hello {name} You Have No Scores To Show")

  elif len(name) == 0 :
    for k , v in skills.items() :
      print(f"{k} => {v}")

  else :
    print(f"Hello {name} This Is Your Score Table:")
    for k , v in skills.items() :
      print(f"{k} => {v}")

get_the_scores("Osama", **scores_list)
get_the_scores("Osama")
get_the_scores(**scores_list)

# ############################# End ###############################