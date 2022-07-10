import random
r = random.randint(1, 100)

while True:
    guess = input('guess a number, between 1 to 100:')
    guess = int(guess)
    if guess == r:
        print('bingo!')
        break
    elif guess < r:
        print('wrong, guess a higher number')
    elif guess > r:
        print('wrong, guess a lower number')


