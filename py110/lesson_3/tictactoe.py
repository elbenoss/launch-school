import os
import random


INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'

board = {
        1: ' ',
        2: ' ',
        3: ' ',
        4: ' ',
        5: ' ',
        6: ' ',
        7: ' ',
        8: ' ',
        9: ' ',
}


# print board
def display_board(board):
    os.system('clear')

    prompt(f"You are {HUMAN_MARKER}. Computer is {COMPUTER_MARKER}.")
    print('')
    print('     |     |')
    print(f"  {board[1]}  |  {board[2]}  |  {board[3]}  ")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[4]}  |  {board[5]}  |  {board[6]}  ")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[7]}  |  {board[8]}  |  {board[9]}  ")
    print('     |     |')
    print('')

def initialize_board():
    return {square: INITIAL_MARKER for square in range(1, 10)}


def prompt(message):
    print(f'==> {message}')


def empty_squares(board):
    return [key for key, value in board.items() if value == INITIAL_MARKER]


def player_chooses_square(board):

    while True:
        valid_choices = [str(num) for num in empty_squares(board)]
        prompt(f"Choose a square ({', '.join(valid_choices)})")

        square = int(input().strip())

        if square in empty_squares(board):
            break
        prompt("That's not a valid choice.")

    board[int(square)] = HUMAN_MARKER


def computer_chooses_square(board):
    if board_full(board):
        return
    square = random.choice(empty_squares(board))
    board[square] = COMPUTER_MARKER


def detect_winner(board):
    winning_lines = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9], # rows
        [1, 4, 7], [2, 5, 8], [3, 6, 9], # columns
        [1, 5, 9], [3, 5, 7]             # diagonals
    ]

    for line in winning_lines:
        sq1, sq2, sq3 = line
        if (HUMAN_MARKER in board[sq1] 
            and HUMAN_MARKER in board[sq2] 
            and HUMAN_MARKER in board[sq3]):
            return 'Player'

        elif (COMPUTER_MARKER in board[sq1] 
              and COMPUTER_MARKER in board[sq2] 
              and COMPUTER_MARKER in board[sq3]):
            return 'Computer'
    return None


def board_full(board):
    return len(empty_squares(board)) == 0

def someone_won(board):
    return bool(detect_winner(board))

def play_tic_tac_toe():
    while True:
        board = initialize_board()

        while True:
            display_board(board)

            player_chooses_square(board)
            
            if someone_won(board) or board_full(board):
                break
            computer_chooses_square(board)

        display_board(board)
        if someone_won(board):
            prompt(f"{detect_winner(board)} won!")
        else:
            prompt("It's a tie!")
        prompt("Player again? (y or n)")
        answer = input().lower()

        if answer[0] != 'y':
            break

    prompt("Thanks for playing tic-tac-toe.")

play_tic_tac_toe()
