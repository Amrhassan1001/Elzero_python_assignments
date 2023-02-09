# ------------------------------------------------------------------------
# ######################## Assignments 65 => 68 ##########################
# ------------------------------------------------------------------------

# ######################## Assignment 1 #########################

import os
num = 1

while num <= 50:
    if num == 25:
        file = open(r"C:\Users\Golden10\Desktop\python\special-text.txt", "w")
    else:
        file = open(fr"C:\Users\Golden10\Desktop\python\text{num}.txt", "w")
        file.write(f"Elzero Web School => {num} ")
    num += 1
    file.close()

print(os.getcwd())
print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.basename(file.name))
print(num)

# ######################## Assignment 2 #########################

num = 1
file = open(fr"C:\Users\Golden10\Desktop\python\text1.txt", "a")
file.write("\nAppended => Elzero Web School" * 50)
file.close()

# ######################## Assignment 3 #########################

file = open(fr"C:\Users\Golden10\Desktop\python\text1.txt", "r")

num_of_lines = 0
num_of_words = []
num_of_chars = 0
num_of_l = 0
not_chars = 0

for line in file :
    num_of_lines += 1
    num_of_words += line.split()
    num_of_l += line.count("l")
    not_chars += line.count(" ") + 2*line.count("\n")
        # \n count as 2 in files.tell()
        # and when we do line.count("\n") count \n as 1
        # so we multiply line.count by 2 


print(f"Number Of Lines Is => {num_of_lines}")
print(f"Number Of words Is => {len(num_of_words)}")
print(f"Number Of Chars Is => {file.tell() - not_chars}")
print(f"Number Of l Is => {num_of_l}")

# ######################## Assignment 4 #########################

import os

num = 50
while num > 40 :
    os.remove(fr"C:\Users\Golden10\Desktop\python\text{num}.txt")
    num -= 1 

# ############################# End ###############################