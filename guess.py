import random
import time

#Set up the game enviroment/welcome message
print ('Welcome to Number Guess \nThe aim of the game is to guess 3 random numbers')





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
            time.sleep(1)
            return False
        except:
            print('Please Enter only numbers')
            continue
            
#check users guess aganist the correct answers

def guess_check():
    global answer_product
    global guess_product
    if answer_product == guess_product:
        print('Congrats You Won!!')
        exit()
    else:
        print('You Have Lost. Try Again')
        exit()
        # have to figure out hwo to retry the guess section here.

number_generator()
user_guess()
guess_check()



""" Things to do:
add retry after failure 
add lives maybe?
add difficulty select/levels
clean up the code a little bit
make functions modules just to get some hands on with that process """

