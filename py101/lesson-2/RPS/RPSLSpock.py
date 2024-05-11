# ask user for input choice
# generate random choice for computer
# compare the choices
# select round winner
# adjust the score based on winner and count round
# check scores to see if either player has reached 3
# declare overall winner and ask to player again
import random

VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']

scores = {'player_score': 0,
          'computer_score': 0,
          'round_number': 0,
}

def display_introduction():
    print(f'Choose one: {", ".join(VALID_CHOICES)}')

def player_sign():
    try:
        sign = input()

    except ValueError:
        player_sign()

    else:
        if sign not in VALID_CHOICES:
            print('Invalid input choose again.')
            player_sign()
        return sign

def computer_sign():
    return random.choice(VALID_CHOICES)

def print_signs():
    player = player_sign()
    computer = str(computer_sign())
    print(f"Player picked {player}, computer picked {computer}")
    return player, computer

def compare_signs():
    players = print_signs()
    if ((players[0] == 'rock' and players[1] in ['lizard', 'scissors']) or
        (players[0] == 'paper' and players[1] in ['rock', 'spock']) or
        (players[0] == 'scissors' and players[1] in ['paper', 'lizard']) or
        (players[0] == 'lizard' and players[1] in ['spock', 'paper']) or
        (players[0] == 'spock' and players[1] in ['scissors', 'rock'])):          
        outcome = 'player'

    elif ((players[0] == 'rock' and players[1] in ['paper', 'spock']) or
        (players[0] == 'paper' and players[1] in ['scissors', 'lizard']) or
        (players[0] == 'scissors' and players[1] in ['spock', 'rock']) or
        (players[0] == 'lizard' and players[1] in ['rock', 'scissors']) or
        (players[0] == 'spock' and players[1] in ['paper', 'lizard'])):
        outcome = 'computer'
    else:
        outcome = 'tie'
    return outcome
    
def determine_winner(winner):
    if winner == 'player':
        adjust_score('player')
        print(f'{winner.title()} wins!')

    elif winner == 'computer':
        adjust_score('computer')
        print(f'{winner.title()} wins!')

    else:
        adjust_score('tie')
    return best_of_five()

def adjust_score(str):
    if str =='player':
        scores['player_score'] += 1
    if str == 'computer':
        scores['computer_score'] += 1
    if str == 'tie':
        print('It\'s a tie')
    scores['round_number'] += 1

def best_of_five():
    print(f"The player's score: {scores['player_score']}\nThe computer's score: {scores['computer_score']}\n"
          f"Current round: {scores['round_number']}") #Current match: {scores['game_number']}")
    
    if scores['player_score'] == 3:
        return play_again()
    
    elif scores['computer_score'] == 3:
        print_champ('computer')
        return play_again()
    return True

def print_champ(champ):
    print(f'The champion is {champ}')
    # scores['game_number'] += 1

def reset_scores():
    scores['player_score'] = 0
    scores['computer_score'] = 0
    scores['round_number'] = 0

def play_again():
    reset_scores()
    if input('Would you like to play again? (y/n)\n') != 'y':
        if input("Do you want to quit? (y/n)\n") != 'n':
            return False
    return True

while True:
    # display_introduction()
    # compared = compare_signs()
    # game_over = determine_winner(compared)
    # if not game_over:
    #     break
    display_introduction()
    if not determine_winner(compare_signs()):
        break