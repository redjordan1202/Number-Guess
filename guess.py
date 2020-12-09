import random
import time

#Set up the game enviroment/welcome message
print ('Welcome to Number Guess \nThe aim of the game is to guess 3 random numbers')





#Define 3 random numbers to be the answer and get product of the 3 number

answer_product = 0

def number_generator():
    global answer_product
    num0 = random.randrange(1,9)
    num1 = random.randrange(1,9)
    num2 = random.randrange(1,9)
    answer_product = num0 * num1 * num2


#take user guess for all 3 numbers 

def user_guess():
    guess0, guess1, guess2 = input('Enter your Guesses with a space serpating each Number').split()
    print(str(guess0 + guess1 + guess2))








#check to make sure the guess is a number this will use the try command


#check to see if the guess is correct by checking product of guess vs product of the random numbers




#possibly add difficulty levels if I can figure it out









#Run the game
number_generator()
time.sleep(3)
print('The product of the 3 Secret Numbers is: ' + str(answer_product))
user_guess()