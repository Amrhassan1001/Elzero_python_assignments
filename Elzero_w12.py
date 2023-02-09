# ------------------------------------------------------------------------
# ######################## Assignments 86 => 89 ##########################
# ------------------------------------------------------------------------

# ######################## Assignment 1 #########################

my_list = ["E", "Z", "R", 1, 2, 3]
my_tuple = ("L", "E", "O")
my_data = []

final_string = ""
for data in zip(my_list, my_tuple):

    final_string += "".join(data)
    final_string = final_string.title()

print(final_string) # Elzero

# ######################## Assignment 2 #########################

my_list1 = ["E", "L", "Z", "E", "R", "O", 1, 2]
my_tuple = ("E", "Z", "R", 1, 2, "E", "R", "O")
my_list2 = ("L", "E", "O", 1, 2, "E", "R", "O")
my_data = []


final_string = ""
for item1, item2, item3 in zip(my_list1, my_tuple, my_list2):

    if type(item1) == str  :
      final_string += item1 
    final_string = final_string.title()
    
print(final_string) # Elzero

# ######################## Assignment 3 #########################

from PIL import Image

my_image = Image.open("D:\Amr\python\Elzero Assignments\elzero-pillow.png")

my_box = (400, 0, 800, 400)
my_crop = my_image.crop(my_box)
my_convert = my_crop.convert("L")

my_convert.show()
my_convert.save(r"D:\Amr\python\Elzero Assignments\new1.png")

my_rotate = my_image.rotate(180)

my_box2 = (0, 0, 1200, 400)
my_crop2 = my_rotate.crop(my_box2)

my_convert2 = my_crop2.convert("L")
my_convert2.show()
my_convert2.save(r"D:\Amr\python\Elzero Assignments\new2.png")

# ######################## Assignment 4 #########################

def say_hello_to(name):
  """
  parameter(someone) => Person Name
  Function To Say Hello To Anyone
  """
  return f"Hello {name}"

print(say_hello_to("Osama")) # "Hello Osama"
help(say_hello_to)

# ######################## Assignment 5 #########################
'''file to pylint '''
myFriends = ["Ahmed", "Osama", "Sayed"]

def say_hello(some_peoples) -> list:
    """ function to say hello """
    for someone in some_peoples:
        print(f"Hello {someone}")

say_hello(myFriends)

# ------------------------------------------------------------------------
# ######################## Assignments 90 => 94 ##########################
# ------------------------------------------------------------------------

# ######################## Assignment 1 #########################

NUM = input("Add Your Number ")

if NUM.isalpha() :
    raise Exception("Exception: Only Numbers Allowed")

elif len(NUM) > 1:
    raise Exception("IndexError: Only One Character Allowed")

elif int(NUM) > 0:
    print(f"The Number Is {NUM}")

elif int(NUM) == 0 :
    raise Exception("ValueError: Number Must Be Larger Than 0")

else :
    raise Exception("Exception: Only Numbers Allowed")

# ######################## Assignment 2 #########################

try :
    LETTER = str(input("Add Letter From A to Z  "))
    if len(LETTER) >= 2 :
        raise IndexError
    if LETTER.isupper() == False or LETTER.isalpha == False :
        raise TypeError

except TypeError:
    print("The Letter Not In A - Z")
except IndexError:
    print("You Must Write One Character Only")
else :
    print(f"You Typed {LETTER}")

# ######################## Assignment 3 #########################

def calculate(num1, num2) -> int :
  return num1 + num2

print(calculate(20, 30))

# ############################# End ###############################
