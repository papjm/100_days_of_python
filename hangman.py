import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in chosen_word:
  display += "_"
print(display)
end_of_game = False

while not end_of_game:
  guess = input("Guess a letter: ").lower()

  for position in range(len(chosen_word)):
    letter = chosen_word[position]
    print(f"Current position: {position}\n     Current letter: {letter}\n Guessed         letter: {guess}")
    if letter == guess:
        display[position] = letter
  print(display)

if "_" not in display:
  end_og_game = True
  print("You win.")
