import random

VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']

GAME_ROUNDS = 5

WINNING_COMBOS = {
    'rock':     ['scissors', 'lizard'],
    'paper':    ['spock', 'rock'],
    'scissors': ['paper', 'lizard'],
    'lizard':   ['spock', 'paper'],
    'spock':    ['rock', 'scissors'],
}

scores = {'player_score': 0,
          'computer_score': 0,
          'round_number': 0,
}

def prompt(str):
    print(f"==> {str}")

def display_choices():
    prompt(f"Pick one of the following: {', '.join(VALID_CHOICES)}")

def short_form(sign):
    for item in VALID_CHOICES:
        if item.startswith(sign):
            return item
        
def get_player_choice():
    try:
        player_sign = input()

    except (ValueError, TypeError):
        pass

    else:
        if short_form(player_sign) in VALID_CHOICES:
            return short_form(player_sign)
        prompt("Invalid choice.")

def computer_choice():
    return random.choice(VALID_CHOICES)

def return_round_winner(player):
    computer = computer_choice()
    print(f"Player choose: {player}, Computer choose: {computer}")

    if computer in WINNING_COMBOS[player]:
        return 'player'
    
    elif player in WINNING_COMBOS[computer]:
        return 'computer'
    
    else:
        return ''
    
def announce_winner(victory):
    prompt(f"{victory.title()} wins!") if victory else print("It's a tie")

def update_scores(winner):
    winner = f"{winner}_score"
    scores[winner] += 1
    scores['round_number'] += 1
    display_round_info()

def display_round_info():
    print(f"Player score: {scores.get('player_score')}")
    print(f"Computer score: {scores.get('computer_score')}")
    print(f"Round number: {scores.get('round_number')}")

def determine_best_of_winner(best_of_winner):
    return scores[f"{best_of_winner}_score"] == 3

def print_victor_and_reset(victor):
    if determine_best_of_winner(victor):
        prompt(f"{victor.title()} wins best of {GAME_ROUNDS}")
        reset_scores()

def play_again():
    prompt("Play again? y/n")
    return input() == 'y'

def reset_scores():
    for item in scores:
        scores[item] = 0

while True:
    display_choices()
    player_choice = get_player_choice()
    
    if player_choice:
        round_winner = return_round_winner(player_choice)
        announce_winner(round_winner)
        
        if round_winner:
            update_scores(round_winner)
            print_victor_and_reset(round_winner)

        if not play_again():
            break