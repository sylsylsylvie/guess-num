import random
r = random.randint(1, 100)
count = 0
count = int(count)
while True:
    guess = input('guess a number, between 1 to 100:')
    guess = int(guess)
    count += 1
    if guess == r:
        print('bingo!')
        print('you have guessed', count,'time(s) in total')
        break
    elif guess < r:
        print('wrong, guess a higher number')
    elif guess > r:
        print('wrong, guess a lower number')
    print('you have guessed', count, 'time(s)')


