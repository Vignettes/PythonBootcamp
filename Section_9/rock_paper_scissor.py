#player one enter choice
#player two enters choice
#shoot
#winner

def my_lenny():
    i = 0
    while i < 15:
        print('( ͡° ͜ʖ ͡°) ( ͡° ͜ʖ ͡°) ( ͡° ͜ʖ ͡°) ( ͡° ͜ʖ ͡°)')
        print('  Cheaters Beware Cheaters Beware')
        i += 1

def cool_lenny():
    i = 0
    while i < 15:
        print('( ͡ʘ ͜ʖ ͡ʘ) ( ͡ʘ ͜ʖ ͡ʘ) ( ͡ʘ ͜ʖ ͡ʘ) ( ͡ʘ ͜ʖ ͡ʘ) ')
        print('  Cheaters Beware Cheaters Beware')
        i += 1

print('...rock...')
print('...paper...')
print('...scissors...')

player_1 = input('Rock, paper, or scissors?')
my_lenny()
cool_lenny()
player_2 = input('Rock, paper, or scissors?')
my_lenny()
cool_lenny()

""" if not player_1  == 'rock' or player_1 == 'paper' or player_1 == 'scissors' and player_2 == 'rock' or player_2 == 'paper' or player_2 == 'scissors':
    print('Try again')
    player_1 = input('Rock, paper, or scissors?')
    my_lenny()
    cool_lenny()
    player_2 = input('Rock, paper, or scissors?')
    my_lenny()
    cool_lenny() """

""" if not player_1  == 'rock' or player_1 == 'paper' or player_1 == 'scissors' and player_2 == 'rock' or player_2 == 'paper' or player_2 == 'scissors':
    print(f'Come back when you are sober!')
    quit()
 """

    
if type(player_1) == str and type(player_2) == str:
    print('(ง ͠° ͟ل͜ ͡°)ง Ok, I have received your weapons (ง ͠° ͟ل͜ ͡°)ง')
    player_1 = player_1.lower()
    player_2 = player_2.lower()
    if player_1 == 'rock' and player_2 == 'paper':
        print('Player One has been vanquished')
    elif player_1 == 'paper' and player_2 == 'rock':
        print('Player Two has been vanquished')
    elif player_1 == 'scissors' and player_2 == 'paper':
        print('Player Two has been vanquished')
    elif player_2 == 'rock' and player_1 == 'paper':
        print('Player Two has been vanquished')
    elif player_2 == 'paper' and player_1 == 'rock':
        print('Player One has been vanquished')
    elif player_2 == 'scissors' and player_1 == 'paper':
        print('Player One has been vanquished')
    elif player_1 == 'paper' and player_2 == 'scissors':
        print('Player One has been vanquished')
    else: 
        print('Tie')


    
