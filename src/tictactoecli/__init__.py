import random
import time

from tictactoecli.mark import Mark
from tictactoecli.board import Board

marks = [Mark.X, Mark.O]

player_mark = marks[random.randint(0, 1)]
computer_mark = Mark.O if player_mark is Mark.X else Mark.X

board = Board()


def clear_console():
    print("\033[H\033[J", end='')


def sleep_and_clear_console(seconds):
    time.sleep(seconds)
    clear_console()


def start_player_turn():
    while True:
        print(board)

        try:
            position = int(input(
                'Enter an available number to place an ' + player_mark.name + ': ').strip())

            row_pos = (position - 1) // 3
            col_pos = (position - 1) % 3

            if [row_pos, col_pos] in board.available_positions():
                break
            else:
                print('Unavailable position. ')
                sleep_and_clear_console(2)

        except ValueError:
            print('Please enter a base-10 number.')
            sleep_and_clear_console(2)

    board.place_mark(row_pos, col_pos, player_mark)
    clear_console()


def start_computer_turn(difficulty_option):
    easy_mode = difficulty_option == 1
    hard_mode = difficulty_option == 2

    if easy_mode:
        positions = board.available_positions() + (board.positions_to_win(computer_mark) * 3)

        # Multiplying the `positions_to_win()` by 3 to increase the chance of those positions being chosen randomly (to make the computer smarter).

    if hard_mode:
        positions = board.available_positions()

        positions_to_win = board.positions_to_win(computer_mark)

        positions_to_block_win = board.positions_to_win(player_mark)

        if len(positions_to_win) != 0:
            positions = positions_to_win
        elif len(positions_to_block_win) != 0:
            positions = positions_to_block_win

    [row_pos, col_pos] = positions[random.randint(0, len(positions) - 1)]

    board.place_mark(row_pos, col_pos, computer_mark)


def play():
    colors = {
        'purple': '\033[0;95m',
        'cyan': '\033[0;96m',
        'red': '\033[0;91m',
        'green': '\033[0;92m',
        'blue': '\033[0;94m',
        'reset': '\033[0m',
        'purple_bold': '\033[1;35m'
    }

    clear_console()

    print(colors['purple'] +
          '\nWelcome to a command-line game of Tic-Tac-Toe!\n' + colors['reset'])

    print(colors['purple'] + 'First, choose the difficulty of the game:' + colors['reset'] + """
    * Easy  (1)
    * Hard  (2)
    """)

    got_valid_input = False

    while not got_valid_input:
        try:
            difficulty_option = int(input(
                colors['cyan'] + '(respond with 1 or 2) >' + colors['reset'] + ' ').strip())

            if difficulty_option not in [1, 2]:
                print(colors['red'] +
                      'Invalid input. Please enter 1 or 2.' + colors['reset'])
            else:
                got_valid_input = True
        except ValueError:
            print(colors['red'] +
                  'Invalid input. Please enter 1 or 2.' + colors['reset'])

    input(colors['cyan'] + 'start game? >' + colors['reset'] + ' ')

    print(colors['purple_bold'] + "\nYou're " + player_mark.name +
          ', and the computer is ' + computer_mark.name + '\n' + colors['reset'])

    input(colors['cyan'] + 'continue? > ' + colors['reset'])

    clear_console()

    is_player_turn = True if player_mark is Mark.X else False

    while (board.check_win() is Mark.NULL) and not board.is_tie():
        if is_player_turn:
            start_player_turn()
            is_player_turn = False
        else:
            start_computer_turn(difficulty_option)
            is_player_turn = True

    print(board)

    if board.check_win() is player_mark:
        print(colors['green'] + 'You won! Congratulations :)' +
              colors['reset'])

    if board.check_win() is computer_mark:
        print(colors['red'] + 'Computer won! You lost :(' + colors['reset'])

    if board.is_tie():
        print(colors['blue'] + 'Tie! No one won.' + colors['reset'])


if __name__ == '__main__':
    play()
