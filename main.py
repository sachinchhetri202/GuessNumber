''' 
    * A program for beginners to get started with python.
    * @author Sachin Chhetri <sachinchhetri202@gmail.com>
    * Use of Random, loop, if/elif clause, and exception handling.  
'''

import random

number = random.randint(1, 9)
guess = 0
count = 0
print('********  Welcome to Guessing Game.  ********\n')
while guess != number and guess != "exit":
    try:
        guess = int(input("Guess the number between 1 to 9: "))

        if guess == "exit":
            break

        count += 1  # adds each time you enter a wrong number

        if count == 1 and guess == number:
            print("Congratulations! You guessed the number in your first try.")
        elif guess < number:
            print("The number you entered is lower than the guessed number. Try Again.\n")
        elif guess > number:
            print("The number you entered is higher than the guessed number. Try Again.\n")
        else:
            print("You got it!")
            print("And it took you", count, "tries to guess the number.")
    except ValueError:
        print("It looks like the number is missing.")



