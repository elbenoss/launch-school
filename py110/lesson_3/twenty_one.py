import random
#import sys

numbers = list(range(2, 11))
faces = ['Jack', 'Queen', 'King', 'Ace']
ranks = numbers + faces
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
deck_of_cards = [f'{rank} of {suit}' for suit in suits for rank in ranks]
player_hand = []
dealer_hand = []

def prompt(message):
    print(f'=> {message}')


def shuffle(deck):
    random.shuffle(deck)
    deal_card(player_hand)
    deal_card(player_hand)
    deal_card(dealer_hand)
    deal_card(dealer_hand)

def deal_card(hand):
    hand.append(deck_of_cards.pop())

def show_hands():
    print(f'You have {player_hand}')
    print(f'Dealer has {dealer_hand[0]}')

def calculate_score(hand):
    score = 0
    for card in hand:
        if card.split()[0].isdigit():
            score += int(card.split()[0])
        elif card.split()[0] == 'Ace':
            if score < 11:
                score += 11
            else:
                score += 1
        else:
            score += 10
    return score

def busted():
    player_score = calculate_score(player_hand)
    if player_score > 21:
        return 'Player'
    if calculate_score(dealer_hand) > 21:
        return 'Dealer'
    return False

def winner():
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)
    if player_score == 21:
        print(f'Player wins with {player_score}')
        print(f'Dealer score: {dealer_score}')
    elif dealer_score == 21:
        print(f'Dealer wins with {player_score}')
    elif player_score > dealer_score:
        print(f'Player wins with {player_score}')
        print(f'Dealer score: {dealer_score}')
    elif dealer_score > player_score:
        print(f'Dealer wins with {dealer_score}')
    else:
        print('Nobody wins')


shuffle(deck_of_cards)

while True:
    show_hands()
    option =  input("hit or stay? ")
    if option != 'hit':
        prompt("invalid option")
    else:
        deal_card(player_hand)
    if busted() or  option == 'stay':
        show_hands()
        break


while calculate_score(dealer_hand) < 17:
    deal_card(dealer_hand)

if busted():
#    sys.stdout.write(f"{busted()} busts with ")
    print(f"{busted()} busts with ", end='')
    print(f"{calculate_score(player_hand)}" \
            if busted() == 'Player' else f"{calculate_score(dealer_hand)}")
    print('Game over')
    # probably end game

else:
    prompt("You choose to stay!") # player didn't bust
    winner()
    print(f"Player score: {calculate_score(player_hand)}")
