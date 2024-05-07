import random

VALID_CHOICES = ['rock', 'paper', 'scissors']

def get_outcome(player, computer):
    prompt(f"You choose {choice}, computer chose {computer_choice}")
    match player:
        case 'rock':
            if computer == 'scissors':
                print('You win')
            elif computer == 'paper':
                print('Computer wins')
            else:
                print('It\'s a tie')
        case 'paper':
            if computer == 'rock':
                print('You win')
            elif computer == 'scissors':
                print('Computer wins')
            else:
                print('It\'s a tie')
        case 'scissors':
            if computer == 'paper':
                print('You win')
            elif computer == 'rock':
                print('Computer wins')
            else:
                print('It\'s a tie')

def prompt(message):
    print(f"==> {message}")

while True:
    prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
    choice = input()

    while choice not in VALID_CHOICES:
        prompt("Thats not a valid choice")
        choice = input()

    computer_choice = random.choice(VALID_CHOICES)
    print(get_outcome(choice, computer_choice))

    prompt("Would you like to play again? (y/n)?")
    answer = input().lower()
    while answer == '' or (answer[0] != 'n' and answer[0] != 'y'):
        prompt("Please enter 'y' or 'n'.")
        answer = input().lower()
    if answer[0] == 'n':
        break