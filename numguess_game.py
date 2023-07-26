import math
import random

secret = random.choice(list(range(1,101)))
guess = int(input('Enter a guess for a random number: '))
guesses = 1

while secret != guess:
  if guess > secret:
    print('too large, try again')
  elif guess < secret:
    print('too small, try again')
  guess = int(input('Enter a guess for a random number: '))
  guesses += 1

print(f' it took you {guesses} guesses to get the secret number!')