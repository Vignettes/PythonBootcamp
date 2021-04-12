from random import randint

def rps_game():
    print('...rock...')
    print('...paper...')
    print('...scissors...')

    player = input("Rock, paper, or scissors? \n").lower()
    rand_num = randint(0,2)
    if rand_num == 0:
        computer = 'rock'
    elif rand_num == 1:
        computer = 'paper'
    else: 
        computer = 'scissors'
    print(computer)

    if player == computer:
        print("It's a tie")
    elif player == 'rock':
        if computer == "scissors":
            print("Player 1 wins!")
        elif computer == "paper":
            print("Player 2 wins!")
    elif player == "paper":
        if computer == "rock":
            print("Player 1 wins!")
        elif computer == "scissors":
            print("Player 2 wins!")
    elif player == "scissors":
        if computer == "paper":
            print("Player 1 wins!")
        elif computer == "rock":
            print("Player 2 wins!")
    else:
        print("Something went wrong")
        
def try_again():
    decision = input("Want to play again? Y/N ").upper()
    if decision == "Y":
        rps_game()
        try_again()
    else: 
        quit()
    
        
rps_game()
try_again()

