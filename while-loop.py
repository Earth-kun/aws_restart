import random

#print the intro of the game
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

#instantiate the number and isGuessRight variables
number = random.randint(1,10)
isGuessRight = False

#the while loop will continue if isGuessRight is false
while isGuessRight != True:
    #ask user for input
    guess = input("Guess a number between 1 and 10: ")
    #the user input is the same with the random number, setting isGuessRight to true and ending the while loop
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    #the while loop will continue if the user input is not equal to the random number
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))