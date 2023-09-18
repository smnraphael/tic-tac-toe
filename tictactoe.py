from os import system, name

spot = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}

def set_board(spot):
    board = (f"+---+---+---+\n| {spot[1]} | {spot[2]} | {spot[3]} |\n+---+---+---+\n| {spot[4]} | {spot[5]} | {spot[6]} |\n+---+---+---+\n| {spot[7]} | {spot[8]} | {spot[9]} |\n+---+---+---+")
    print(board)
    print(">> ", end="")

def set_turn(turn):
    if turn % 2 == 0:
        return 'X'
    else:
        return 'O'

def check_win(spot):
    x = 'X'
    o = 'O'
    if (spot[1] == x and spot[2] == x and spot[3] == x) or (spot[1] == o and spot[2] == o and spot[3] == o) or (spot[4] == x and spot[5] == x and spot[6] == x) or (spot[4] == o and spot[5] == o and spot[6] == o) or (spot[7] == x and spot[8] == x and spot[9] == x) or (spot[7] == o and spot[8] == o and spot[9] == o):
        return True
    elif (spot[1] == x and spot[4] == x and spot[7] == x) or (spot[1] == o and spot[4] == o and spot[7] == o) or (spot[2] == x and spot[5] == x and spot[8] == x) or (spot[2] == o and spot[5] == o and spot[8] == o) or (spot[3] == x and spot[6] == x and spot[9] == x) or (spot[3] == o and spot[6] == o and spot[9] == o):
        return True
    elif (spot[1] == x and spot[5] == x and spot[9] == x) or (spot[1] == o and spot[5] == o and spot[9] == o) or (spot[3] == x and spot[5] == x and spot[7] == x) or (spot[3] == o and spot[5] == o and spot[7] == o):
        return True
    else:
        return False

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

playing = True
turn = 0
winner = False

while playing:
    clear()
    set_board(spot)
    choice = input()

    if str.isdigit(choice) and int(choice) in spot:
        if not spot[int(choice)] in {'X', 'O'}:
            spot[int(choice)] = set_turn(turn)
            turn += 1
    elif choice == 'q':
        playing = False

    if check_win(spot):
        playing = False
        winner = True
        clear()
        set_board(spot)
        if turn % 2 == 1:
            print("Winner is Player 1!")
        else:
            print("Winner is Player 2!")
    if turn > 8:
        playing = False
        if winner == False:
            print("No winner")
