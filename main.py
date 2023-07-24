import random

number = random.randint(1, 10)
attempts = 0

while attempts < 3:
    guess = int(input('Enter your guess: '))
    if guess == number:
        print('Congratulations! You won!')
        break
    else:
        print('Wrong guess. Try again.')
        attempts += 1
else:
    print('You lost. The correct number was', number)
