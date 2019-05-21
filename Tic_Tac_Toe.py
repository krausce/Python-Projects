import random

game_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']

def clear_game_board():
    index = 1
    while index < len(game_board):
        game_board[index] = ' '
        index += 1


def display_board():
    clear_display()
    print(f'_____________\n|   |   |   |\n| {game_board[1]} | {game_board[2]} | {game_board[3]} |\n'
          f'|___|___|___|\n|   |   |   |\n| {game_board[4]} | {game_board[5]} | {game_board[6]}'
          f' |\n|___|___|___|\n|   |   |   |\n| {game_board[7]} | {game_board[8]} | {game_board[9]} |\n|___|___|___|')

def clear_display():
    print('\n' * 100)

def player_input():
    player_marker = ''

    while not (player_marker == 'X' or player_marker == 'O'):
        player_marker = input('Select whether you want to be an X or an O : ').upper()

    if player_marker == 'X':
        return ('X', 'O')

    return ('O', 'X')

def place_marker(marker, position):

    game_board[position] = marker

def win_check(mark):
    return ((game_board[1] == mark and game_board[2] == mark and game_board[3] == mark) or #Top row win
            (game_board[4] == mark and game_board[5] == mark and game_board[6] == mark) or #Middle row win
            (game_board[7] == mark and game_board[8] == mark and game_board[9] == mark) or #Bottom row win
            (game_board[1] == mark and game_board[4] == mark and game_board[7] == mark) or #Left col win
            (game_board[2] == mark and game_board[5] == mark and game_board[8] == mark) or #Mid col win
            (game_board[3] == mark and game_board[6] == mark and game_board[9] == mark) or #Rht col win
            (game_board[1] == mark and game_board[5] == mark and game_board[9] == mark) or #Diag win
            (game_board[3] == mark and game_board[5] == mark and game_board[7] == mark))   #Diag win

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 1'
    return 'Player 2'

def space_check(position):
    return game_board[position] == ' '

def full_board_check():
    for i in range(1, 10):
        if space_check(i):
            return False
    return True

def player_choice():
    position = 0
    try:
        while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(position):
            position = int(input('Choose your next move: (1-9) '))

        return position
    except:
        print('Please only enter whole numbers (1-9).')
        return player_choice()

def replay():
    play = ''

    while not (play == 'Y' or play == 'N'):
        play = input('Would you like to play again? Y or N : ').upper()

    return play == 'Y'

print('Welcome to Tic-Tac-Toe!')

play_game = True

while play_game:
    clear_game_board()
    display_board()
    player_markers = player_input()
    first_player = choose_first()

    while not (full_board_check() or win_check(player_markers[0]) or win_check(player_markers[1])):

        if first_player == 'Player 1':
            game_board[player_choice()] = player_markers[0]
            display_board()
            if win_check(player_markers[0]):
                print('Congratulations Player 1! You\'ve won!')
            elif full_board_check():
                print('The game ended in a tie.')
            first_player = 'Player 2'
        else:
            player_selection = random.randint(1, 9)
            while not space_check(player_selection):
                player_selection = random.randint(1, 9)
            game_board[player_selection] = player_markers[1]
            display_board()
            if win_check(player_markers[1]):
                print('Better luck next time, the computer won.')
            elif full_board_check():
                print('The game ended in a tie.')
            first_player = 'Player 1'
    play_game = replay()
