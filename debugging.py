def my_function():
  for i in range(1, 20):
    if i ==20:
      print("You got it")
my_function
#debugging this
from random import randint
dice_imgs = ["1", "2", "3", "4", "5", "6"]
dice_num = randint(1, 6)
print(dice_imgs[dice_num])

#play computer
year = int (input("What is your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year => 1994:
  print("You are a Gen Z")

# Fix the error
age = int(input("How old are you"))
if age > 18:
  print(f"you can drive at age {age}")
  
