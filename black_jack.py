import random
def deal_card():
  cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]:
  card = random.choice(cards)
  return card
#Hint: deal user and computer two cards each using deal_card()

def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
user_cards = []
computer_cards = []
is_game_over = False
for _ in range(2):
  user_cards.append(deal_cards())
  computer_cards.append(deal_cards())
user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)
print(f" Your cards: {user_cards}, current score: {user_score}")

if user_score == 0 or computer_score == 0 or user_score > 21:
  is_game_over = True
  
  
   
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)
