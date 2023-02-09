#-----------------------------------------------------------------------
######################### Assignments 26 => 32 #########################
#-----------------------------------------------------------------------

######################### Assignment 1 #########################

my_list = [1, 2, 3, 3, 4, 5, 1]
# Needed Output

# 1, 2, 3, 4, 5
# <class 'list'>
# 1, 2, 3, 4

my_list.sort()

unique_list = set(my_list)
unique_list = list(unique_list)

print(unique_list)
print(type(unique_list))
print(unique_list[0:4])


# ######################### Assignment 2 #########################

nums = {1, 2, 3}
letters = {"A", "B", "C"}

# Needed Output

# {1, 2, 3, "A", "B", "C"}
# {1, 2, 3, "A", "B", "C"}
# {1, 2, 3, "A", "B", "C"}

print(nums | letters)
print(nums.union(letters))
nums.update(letters)
print(nums)



# ######################### Assignment 3 #########################

my_set = {1, 2, 3}
letters = {"A", "B", "C"}

# Needed Output

# {1, 2, 3}
# set()
# {"A", "B"}

print(my_set)
# -----------
my_set.clear()
print(my_set)
# -----------
my_set.add("A")
my_set.add("B")
print(my_set)
# -----------
my_set.discard("C")
print(my_set)




# ######################### Assignment 4 #########################

set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}

# Needed Output
# True

print(set_one.issubset(set_two))
# or
print(set_two.issuperset(set_one))

# ######################### Assignment 5 #########################

# Create Dictionary Here

# Needed Output

# "HTML Progress Is 90%"
# "CSS Progress Is 80%" 
# "Python Progress Is 30%"
# "AI Progress Is 20%"

skills = {
  "Html" : "90%" ,
  "Css" : "80%",
  "Python" : "30%",
}
skills.update({"AI":"20%"})

print(f"Html progress is {skills['Html']}")
print(f"Css progress is {skills['Css']}")
print(f"Python progress is {skills['Python']}")
print(f"AI progress is {skills['AI']}")

# ############################# End ###############################