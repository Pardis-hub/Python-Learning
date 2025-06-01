import random

number = random.randint(1, 10)
print('Guess a number between 1 and 10: ')
for round in range(5):
    guess_number = int(input())
    if guess_number == number:
        print(f"You guessed the number in {round+1} tries!")
        break
    elif guess_number < 1 or guess_number > 10:
        print('Your guess is not between 1 and 10!')
    elif guess_number != number and round == 4:
        print('You did not guess right in 5 tries!')
        break
    elif guess_number < number :
        print('Your guess is too low')
    elif guess_number > number:
        print('Your guess is too high')





