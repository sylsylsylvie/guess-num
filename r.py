import random
start = input('choose a range, from:')
end= input('to:')
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0
count = int(count)
while True:
    guess = input('guess a number:')
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


