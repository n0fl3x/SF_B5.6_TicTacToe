# Greetings function
def greetings_rules():
    print("                       Hello! I'm glad to welcome you in tic-tac-toe game.")
    print("                   It's a game for two players where they take their turns one by")
    print("                                              another.")
    print(" ")
    print("                    For every turn just enter a number of game field sector")
    print("                       where you want to place your token and press enter.")
    print(" ")
    print("                    First player who collect 3 same tokens in one row, column")
    print("                                        or diagonal wins.")
    print(" ")
    print("                                Play smart & enjoy your game! :)")


game_field = [i + 1 for i in range(9)]

win_conditions = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
                  [1, 4, 7], [2, 5, 8], [3, 6, 9],
                  [1, 5, 9], [3, 5, 7]]


# Game field demonstration function
def field_show():
    print('')
    print('=========')
    for q in range(3):
        if q != 2:
            print(game_field[0 + q * 3], ' | ', game_field[1 + q * 3], ' | ', game_field[2 + q * 3], sep='')
            print('---------')
        else:
            print(game_field[0 + q * 3], ' | ', game_field[1 + q * 3], ' | ', game_field[2 + q * 3], sep='')
            print('=========')
            print('')


# Take-turn function
def take_turn(token):
    while True:
        turn_info = input("Where you want to place your " + token + " : ")
        if not turn_info.isdigit():
            print('')
            print("Use only numbers! Try again.")
            print('')
            continue
        elif int(turn_info) < 1 or int(turn_info) > 9:
            print('')
            print("Out of range! Try again.")
            print('')
            continue
        elif game_field[int(turn_info) - 1] == "X" or game_field[int(turn_info) - 1] == "O":
            print('')
            print("This sector is already taken!")
            print('')
            continue
        game_field[int(turn_info) - 1] = token
        break


# Win checking function
def win_check():
    for k in win_conditions:
        if (game_field[k[0] - 1]) == (game_field[k[1] - 1]) == (game_field[k[2] - 1]):
            return game_field[k[1] - 1]
    else:
        return False


# Main game function
def game():
    turn_cnt = 0
    while True:
        field_show()
        if turn_cnt % 2 == 0:
            take_turn('X')
        else:
            take_turn('O')
        if turn_cnt > 3:
            winner = win_check()
            if winner:
                field_show()
                print("Player with", winner, "wins!")
                break
        turn_cnt += 1
        if turn_cnt > 8:
            field_show()
            print("It's a tie.")
            break


greetings_rules()
game()
