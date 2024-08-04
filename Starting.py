import random
import time

def guessing_game():
    number_to_guess = random.randint(1, 100)
    Ur_Guess = None
    
    v = 0

    max = 3


    while Ur_Guess != number_to_guess:

        

        if v >= max :
            print (" Checking Tries.......  ")
            time.sleep(2)
            
            print ("You have past the limits of tries. Better luck next time!!!")

            exit()
           
        Ur_Guess = int(input("Guess a number from 1 to a 100 " ))

        if Ur_Guess < number_to_guess:
            print ("Guess higher than that!! ")

        elif Ur_Guess > number_to_guess:
            print("Guess smaller than that !! ")
        
        elif Ur_Guess == number_to_guess:
            print ("Congragulations you got it correct!!! ")
    
        v = v+1

            
guessing_game()
