""" Guessing Game That Let's You Know If You're Right! Legally! I Promise! """

import random

random_number = random.randint(1,10) #random number 1-10

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n Guess the number, 1-10')

guess = ''



while True:
    guess = int(input("Pick a number from 1 to 10: "))
    if guess < random_number:
        print("Too low!")
    elif guess > random_number:
        print("Too high!")
    else:
        print("You won!")
        play_again = input("Do you want to play again? (y/n) ").lower()
        if(play_again == "y"):
            random_number = random.randint(1,10)
            guess = None
        else:
            print("Thank you for playing")
            break

  
  
  
  
  
   
""" 
def guess():
    user_guess = input()
    if user_guess == random_number:
        print("You win!") 
    else:
        print('Whoops, not it. Want to play again? Y/N')
        user_choice = input().lower()
        if user_choice == 'y':
                user_guess = input("Guess the number: ")
        else:
            quit()


guess()


 """

        