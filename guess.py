import random
import time

#Define 3 random numbers to be the answer and get product of the 3 number

def game_setup():
    global answer_product
    global lives
    num0 = random.randrange(2,difficulty)
    num1 = random.randrange(2,difficulty)
    num2 = random.randrange(2,difficulty)
    answer_product = num0 * num1 * num2
    lives = 3
    print('The product of the 3 Secret Numbers is: ' + str(answer_product) + '\n')
    print('You have ' + str(lives) + ' lives.\n')

#take user guess for all 3 numbers and check if guess is numbers 

def user_guess():
    while True:
        guess0, guess1, guess2 = input('Enter your Guesses with a space serpating each Number:  ').split()
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
            
#This is to set difficulty and change the number range based on the difficulty that the user selects.

def difficulty_select():
    global difficulty
    while True:
        print('Please Select a Diffculty Level')
        user_input = input('1 2 or 3:  ')
        if user_input not in ('1', '2', '3'):
            print('Please make a Valid Selection')
            continue
        else:
            if user_input == '1':
                difficulty = 3
            elif user_input == '2':
                difficulty = 6
            elif user_input == '3':
                difficulty = 9
        break


def Main():
    global lives
    print ('Welcome to Number Guess \n\nThe aim of the game is to guess 3 random numbers\n')
    difficulty_select()
    game_setup()
    #Check if the users guess is correct
    while lives > 0:
        user_guess()
        if guess_product == answer_product:
            print('Congrats!! You Won!!')
            return False
        else:
            print('Your answer is wrong. Try again!')
            lives -= 1
            print('You have ' + str(lives) + ' lives left.')
            continue
    else:
        print('You are out of Lives. \n GAME OVER.' )
        exit()

#Run the game

Main()




""" Things to do:
add lives maybe?
add difficulty select/levels
clean up the code a little bit
make functions modules just to get some hands on with that process """

