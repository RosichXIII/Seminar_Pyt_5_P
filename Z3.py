# Создайте программу для игры в ""Крестики-нолики"".

board = list(range(1,10))

def draw_board(board):
    print ("-" * 13)
    for i in range(3):
        print ("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print ("-" * 13)

def take_input(player_symbol):
    valid = False
    while not valid:
        player_move = input(f'Ход {player_symbol}.\n')
        try:
            player_move = int(player_move)
        except:
            print ("Введите число от 1 до 9.")
            continue
        if player_move in range(1, 10):
            if (str(board[player_move-1]) not in "XO"):
                board[player_move-1] = player_symbol
                valid = True
            else:
                print ("Клетка занята. Выберите другую клетку.")
        else:
            print ("Некорректный ввод. Введите число от 1 до 9.")

def win_check(board):
    win_conditions = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for each in win_conditions:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

def main(board):
    count = 0
    win = False
    while not win:
        draw_board(board)
        if count % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        count += 1
        if count > 4:
            temp = win_check(board)
            if temp:
                print (f'Победил {temp}!')
                win = True
                break
        if count == 9:
            print ("Ничья.")
            break
    draw_board(board)

main(board)