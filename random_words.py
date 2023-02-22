word_list = ["ardvark","baboon","camel"]
import random
chosen_word = random.choice(word_list)

input("Guess a letter").lower()
for letter in chosen_word:
  if letter == guess:
    print("right")
  else:
    print("wrong")
