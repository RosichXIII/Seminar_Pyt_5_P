# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random

candy = 2021
max_candy_taken = 28
mode_select = int(input('Выберите режим игры\nПротив игрока - введите "1"\nПротив бота - введите "2"\n'))
initiative = int(input('Чей ход открывает игру?\nPlayer 1 - введите "1"\nPlayer 2 - введите "2"\nСлучайно - введите "3"\n'))
turn = 1
if mode_select == 1:
    if initiative == 1:
        while candy > 0:
            if turn % 2 == 1:
                print(f'Конфет осталось: {candy}')
                taken_amount = int(input('Ход Player 1: '))
                if taken_amount in range(1, max_candy_taken + 1):
                    candy -= taken_amount
                    turn +=1
                else:
                    while taken_amount not in range(1, max_candy_taken + 1):
                        taken_amount = int(input(f'Возьмите не более {max_candy_taken} конфет\n'))
                    candy -= taken_amount
                    turn +=1
            else:
                print(f'Конфет осталось: {candy}')
                taken_amount = int(input('Ход Player 2: '))
                if taken_amount in range(1, max_candy_taken + 1):
                    candy -= taken_amount
                    turn +=1
                else:
                    while taken_amount not in range(1, max_candy_taken + 1):
                        taken_amount = int(input(f'Возьмите не более {max_candy_taken} конфет\n'))
                    candy -= taken_amount
                    turn +=1
        if turn % 2 == 0:
            print('Победил Player 1!')
        else:
            print('Победил Player 2!')
    if initiative == 2:
        while candy > 0:
            if turn % 2 == 0:
                print(f'Конфет осталось: {candy}')
                taken_amount = int(input('Ход Player 1: '))
                if taken_amount in range(1, max_candy_taken + 1):
                    candy -= taken_amount
                    turn +=1
                else:
                    while taken_amount not in range(1, max_candy_taken + 1):
                        taken_amount = int(input(f'Возьмите не более {max_candy_taken} конфет\n'))
                    candy -= taken_amount
                    turn +=1
            else:
                print(f'Конфет осталось: {candy}')
                taken_amount = int(input('Ход Player 2: '))
                if taken_amount in range(1, max_candy_taken + 1):
                    candy -= taken_amount
                    turn +=1
                else:
                    while taken_amount not in range(1, max_candy_taken + 1):
                        taken_amount = int(input(f'Возьмите не более {max_candy_taken} конфет\n'))
                    candy -= taken_amount
                    turn +=1
        if turn % 2 == 1:
            print('Победил Player 1!')
        else:
            print('Победил Player 2!')
    else:        
        initiative = random.randint(0, 99)
        if initiative in range(50):
            while candy > 0:
                if turn % 2 == 1:
                    print(f'Конфет осталось: {candy}')
                    taken_amount = int(input('Ход Player 1: '))
                    if taken_amount in range(1, max_candy_taken + 1):
                        candy -= taken_amount
                        turn +=1
                    else:
                        while taken_amount not in range(1, max_candy_taken + 1):
                            taken_amount = int(input(f'Возьмите не более {max_candy_taken} конфет\n'))
                        candy -= taken_amount
                        turn +=1
                else:
                    print(f'Конфет осталось: {candy}')
                    taken_amount = int(input('Ход Player 2: '))
                    if taken_amount in range(1, max_candy_taken + 1):
                        candy -= taken_amount
                        turn +=1
                    else:
                        while taken_amount not in range(1, max_candy_taken + 1):
                            taken_amount = int(input(f'Возьмите не более {max_candy_taken} конфет\n'))
                        candy -= taken_amount
                        turn +=1
            if turn % 2 == 0:
                print('Победил Player 1!')
            else:
                print('Победил Player 2!')
        else:
            while candy > 0:
                if turn % 2 == 0:
                    print(f'Конфет осталось: {candy}')
                    taken_amount = int(input('Ход Player 1: '))
                    if taken_amount in range(1, max_candy_taken + 1):
                        candy -= taken_amount
                        turn +=1
                    else:
                        while taken_amount not in range(1, max_candy_taken + 1):
                            taken_amount = int(input(f'Возьмите не более {max_candy_taken} конфет\n'))
                        candy -= taken_amount
                        turn +=1
                else:
                    print(f'Конфет осталось: {candy}')
                    taken_amount = int(input('Ход Player 2: '))
                    if taken_amount in range(1, max_candy_taken + 1):
                        candy -= taken_amount
                        turn +=1
                    else:
                        while taken_amount not in range(1, max_candy_taken + 1):
                            taken_amount = int(input(f'Возьмите не более {max_candy_taken} конфет\n'))
                        candy -= taken_amount
                        turn +=1
            if turn % 2 == 1:
                print('Победил Player 1!')
            else:
                print('Победил Player 2!')
elif mode_select == 2:
    if initiative == 1:
        while candy > 0:
            if turn % 2 == 1:
                print(f'Конфет осталось: {candy}')
                taken_amount = int(input('Ход Player 1: '))
                if taken_amount in range(1, max_candy_taken + 1):
                    candy -= taken_amount
                    turn +=1
                else:
                    while taken_amount not in range(1, max_candy_taken + 1):
                        taken_amount = int(input(f'Возьмите не более {max_candy_taken} конфет\n'))
                    candy -= taken_amount
                    turn +=1
            else:
                if candy > max_candy_taken:
                    print(f'Конфет осталось: {candy}')
                    print('Ход Player 2: ', end = '')
                    if candy % max_candy_taken == 0:
                        taken_amount = random.randint(1, max_candy_taken - 1)
                    else:
                        taken_amount = max_candy_taken
                    print(taken_amount)
                    candy -= taken_amount
                    turn +=1
                else:
                    print(f'Конфет осталось: {candy}')
                    print('Ход Player 2: ', end = '')
                    taken_amount = candy
                    print(taken_amount)
                    candy -= taken_amount
                    turn +=1
        if turn % 2 == 0:
            print('Победил Player 1!')
        else:
            print('Победил Player 2!')
    if initiative == 2:
        while candy > 0:
            if turn % 2 == 0:
                print(f'Конфет осталось: {candy}')
                taken_amount = int(input('Ход Player 1: '))
                if taken_amount in range(1, max_candy_taken + 1):
                    candy -= taken_amount
                    turn +=1
                else:
                    while taken_amount not in range(1, max_candy_taken + 1):
                        taken_amount = int(input(f'Возьмите не более {max_candy_taken} конфет\n'))
                    candy -= taken_amount
                    turn +=1
            else:
                if candy > max_candy_taken:
                    print(f'Конфет осталось: {candy}')
                    print('Ход Player 2: ', end = '')
                    if candy % max_candy_taken == 0:
                        taken_amount = random.randint(1, max_candy_taken - 1)
                    else:
                        taken_amount = max_candy_taken
                    print(taken_amount)
                    candy -= taken_amount
                    turn +=1
                else:
                    print(f'Конфет осталось: {candy}')
                    print('Ход Player 2: ', end = '')
                    taken_amount = candy
                    print(taken_amount)
                    candy -= taken_amount
                    turn +=1
        if turn % 2 == 1:
            print('Победил Player 1!')
        else:
            print('Победил Player 2!')
    else:
        initiative = random.randint(0, 99)
        if initiative in range(50):
            while candy > 0:
                if turn % 2 == 1:
                    print(f'Конфет осталось: {candy}')
                    taken_amount = int(input('Ход Player 1: '))
                    if taken_amount in range(1, max_candy_taken + 1):
                        candy -= taken_amount
                        turn +=1
                    else:
                        while taken_amount not in range(1, max_candy_taken + 1):
                            taken_amount = int(input(f'Возьмите не более {max_candy_taken} конфет\n'))
                        candy -= taken_amount
                        turn +=1
                else:
                    if candy > max_candy_taken:
                        print(f'Конфет осталось: {candy}')
                        print('Ход Player 2: ', end = '')
                        if candy % max_candy_taken == 0:
                            taken_amount = random.randint(1, max_candy_taken - 1)
                        else:
                            taken_amount = max_candy_taken
                        print(taken_amount)
                        candy -= taken_amount
                        turn +=1
                    else:
                        print(f'Конфет осталось: {candy}')
                        print('Ход Player 2: ', end = '')
                        taken_amount = candy
                        print(taken_amount)
                        candy -= taken_amount
                        turn +=1
            if turn % 2 == 0:
                print('Победил Player 1!')
            else:
                print('Победил Player 2!')
        else:
            while candy > 0:
                if turn % 2 == 0:
                    print(f'Конфет осталось: {candy}')
                    taken_amount = int(input('Ход Player 1: '))
                    if taken_amount in range(1, max_candy_taken + 1):
                        candy -= taken_amount
                        turn +=1
                    else:
                        while taken_amount not in range(1, max_candy_taken + 1):
                            taken_amount = int(input(f'Возьмите не более {max_candy_taken} конфет\n'))
                        candy -= taken_amount
                        turn +=1
                else:
                    if candy > max_candy_taken:
                        print(f'Конфет осталось: {candy}')
                        print('Ход Player 2: ', end = '')
                        if candy % max_candy_taken == 0:
                            taken_amount = random.randint(1, max_candy_taken - 1)
                        else:
                            taken_amount = max_candy_taken
                        print(taken_amount)
                        candy -= taken_amount
                        turn +=1
                    else:
                        print(f'Конфет осталось: {candy}')
                        print('Ход Player 2: ', end = '')
                        taken_amount = candy
                        print(taken_amount)
                        candy -= taken_amount
                        turn +=1
            if turn % 2 == 1:
                print('Победил Player 1!')
            else:
                print('Победил Player 2!')