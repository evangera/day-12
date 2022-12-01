from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game! ")

hes_thinking = random.randrange(100)
print("I'm thinking of a number between 1 and 100.")
print(f"Pssst, the correct answer is {hes_thinking}")

guess_amount = 0
choose_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
while choose_difficulty != 'easy' and choose_difficulty != 'hard':
  choose_difficulty = input("Please insert correct value: 'easy' or 'hard': ")
if choose_difficulty == 'easy':
  guess_amount = 10
elif choose_difficulty == 'hard':
  guess_amount = 5

def start_game(guess_amount, hes_thinking):
  player_guess = 0
  while player_guess != hes_thinking:
    player_guess = input("Make a guess: ")
    while not player_guess.isdigit():
      player_guess = input("Please insert whole number: ")
    player_guess = int(player_guess)
    if player_guess != hes_thinking:
      guess_amount -= 1
    if player_guess == hes_thinking:
      return print(f"You got it! The answer was {hes_thinking}")
    if guess_amount == 0:
      return print(f"You've run out of guesses, you lose. The right answer was {hes_thinking}")
    elif player_guess < hes_thinking:
      print("Too low.")
    elif player_guess > hes_thinking:
      print("Too high.")

start_game(guess_amount, hes_thinking)
