import random
number = random.radiant(1,100)
player_name = input("Hello, What's your name?")
number_of_guesses = 0
print('okay! '+ player_name+ 'I am Guessing a number between 1 and 100')

while number_of_guesses < 5:
        guess = int(input())
        number_of_guesses += 1
        if guess < number:
            print('Your Guess is too low')
        if guess > number:
            print('Your Guess is too high')
        if guess == number:
            break
if guess == number:
    print('You guessed the number in ' + str(number_of_guesses) + ' tries!')
else:
    print('You guessed incorrectly, The number was ' +str(number))
        