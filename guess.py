import random
import time

#Define 3 random numbers to be the answer and get product of the 3 number

def number_generator():
    num0 = random.randrange(2,9)
    num1 = random.randrange(2,9)
    num2 = random.randrange(2,9)
    global answer_product
    answer_product = num0 * num1 * num2
    print('The product of the 3 Secret Numbers is: ' + str(answer_product))

#take user guess for all 3 numbers and check if guess is numbers 

def user_guess():
    while True:
        guess0, guess1, guess2 = input('Enter your Guesses with a space serpating each Number').split()
        try:
            global guess_product
            guess_product = int(guess0) * int(guess1) * int(guess2)
            print('You Guessed ' + str(guess0) + ', ' + str(guess1)+ ', '  + str(guess2))
            print("Checking Answer...")
            time.sleep(.5)
            return False
        except:
            print('Please Enter only numbers')
            continue
            
#check users guess aganist the correct answers

def Main():
    print ('Welcome to Number Guess \nThe aim of the game is to guess 3 random numbers')
    number_generator()
    while True:
        user_guess()
        if guess_product == answer_product:
            print('Congrats!! You Won!!')
            return False
        else:
            print('Your answer is wrong. Try again!')
            continue

#Run the game

Main()




""" Things to do:
add lives maybe?
add difficulty select/levels
clean up the code a little bit
make functions modules just to get some hands on with that process """

