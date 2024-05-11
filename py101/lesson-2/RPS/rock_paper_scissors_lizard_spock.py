import random

VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']
NUMBER_OF_ROUNDS = 5

def prompt(message):
    print(f"==> {message}")

def choice_prompt():
    choice = input().lower()
    shortened_choice = shortened_word(choice)
    return shortened_choice

def shortened_word(letters):
    for word in VALID_CHOICES:
        if letters[0:2] in word[0:2]:
            return word

def determine_winner(final_round, final_player_score, final_computer_score):
    if (final_player_score == 3 or
        final_computer_score == 3):
        prompt(f"Current round: {final_round}")
        if final_player_score > final_computer_score:
            prompt(
        "Game over." 
        f"Player wins {final_player_score} out of {final_round}.")
        else:
            prompt(
        "Game over."
        f"Computer wins {final_computer_score} out of {final_round}.")
        scores = start_rounds()
        return scores

def start_rounds():
    current_round = 0
    player_score = 0
    computer_score = 0
    return [current_round, player_score, computer_score]

def increment_score(round_winner, current_scores):

    if round_winner == True:
        current_scores[1] += 1
        current_scores[0] += 1
    elif round_winner == False:
        current_scores[2] += 1
        current_scores[0] += 1

    current_round = current_scores[0]
    player_score = current_scores[1]
    computer_score = current_scores[2]
        
    print(f"Player score is {player_score}")
    print(f"Computer score is {computer_score}")
    prompt(f"Current round is {current_round}")
    if determine_winner(current_round, player_score, computer_score) != None:
        return start_rounds()

def display_outcome(player, computer):
    prompt(f"You choose {abbr_choice}, computer chose {computer_choice}")
    if ((player == 'rock' and computer in ['scissors', 'lizard']) or
        (player == 'paper' and computer in ['rock', 'spock']) or
        (player == 'scissors' and computer in ['paper', 'lizard']) or
        (player == 'lizard' and computer in ['paper', 'spock']) or
        (player == 'spock' and computer in ['rock', 'scissors'])):
        print("You win")
        return True
    elif ((player == 'rock' and computer in ['paper', 'spock']) or
        (player == 'paper' and computer in ['scissors', 'lizard']) or
        (player == 'scissors' and computer in ['rock', 'spock']) or
        (player == 'lizard' and computer in ['rock', 'scissors']) or
        (player == 'spock' and computer in ['rock', 'scissors'])):
        print("Computer wins")
        return False
    else:
        print("It's a tie")
        return None
    
scores = start_rounds()
while True:
    prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
    abbr_choice = choice_prompt()

    while abbr_choice not in VALID_CHOICES:
        prompt("Thats not a valid choice")
        abbr_choice = choice_prompt()

    computer_choice = random.choice(VALID_CHOICES)
    win = display_outcome(abbr_choice, computer_choice)
    if (increment_score(win, scores)) != None:
        scores = start_rounds()
    prompt("Would you like to play again? (y/n)?")

    answer = input().lower()
    while answer == '' or (answer[0] != 'n' and answer[0] != 'y'):
        prompt("Please enter 'y' or 'n'.")
        answer = input().lower()
    if answer[0] != 'y':
        break