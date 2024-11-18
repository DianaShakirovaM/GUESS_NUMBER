from random import randint



NOT_GUESSED = True
computer_number = randint(1, 100)


while not_guessed:
    print('Enter yout number:')
    user_number = int(input())
    if computer_number == user_number:
        print('Great intuition! You guessed the number!')
        not_guessed = False
    if user_number > computer_number:
        print('Your number is more than computer one. Try again!') 
    else:
        print('Yor number is less than computer one. Try again!')
