import os
import random
def Ship_letter_number_calculator(a):
    if a==1:
        return 'первого'
    elif a==2:
        return 'второго'
    elif a==3:
        return 'третьего'
    else:
        return 'четвертого'
def Perimeter(a,b,c,d,players_digital_number):
    for i in range(b):
        for x in range(d):
            if a-1+i>=0 and c-1+x>=0 and a-1+i<=9 and c-1+x<=9:
                game_board[players_digital_number][a-1+i][c-1+x]=2
def Exception_e_brief(a):
    if ord(a)==1050:
        return 1
    else:
        return 0
def Letter_number_of_the_player(players_digital_number):
    if players_digital_number==0:
        return 'перв'
    else:
        return 'второ'
def Randint(a,b):
    return random.randint(a,b)
def Player_or_robot():
    i=0
    while 1!=0:
        if i==0:
            i=1
            g='С кем будешь играть с человеком или с компьютером? '
        else:
            g='Данный ответ недопустим, ответьте либо человек, либо компьютер: '
        player_or_robot=input(g)
        if player_or_robot=='C человеком' or player_or_robot=='С компьютером':
            break
            return player_or_robot
def Autofill():
    i=0
    while 1!=0:
        if i==0:
            i=1
            g='Нужно автозаполнение? '
        else:
            g='Данный ответ недопустим, ответьте либо да, либо нет:'
        autofill=input(g)
        if autofill=='да' or autofill=='нет':
            break
    if autofill=='да':
        return 0
    else:
        return 1
def Complexity():
    i=0
    while 1!=0:
        if i==0:
            i=1
            g='Какая сложность 1-ая или 2-ая?'
        else:
            g='Данный ответ недопустим, ответьте либо 1, либо 2:'
        complexity=input(g)
        if complexity=='1' or complexity=='2':
            break
    return int(complexity)
def Multydeck_ship_input(numerical_number_of_ship_decks,letter_number_of_the_ship,ur,players_digital_number):
    if p==0:
        g='К'
        p=1
    else:
        g='Данные кординаты недопустимы. Введите к'
    array_with_variables=input(g+'ординаты '+letter_number_of_the_ship+ur+'палубного корабля через пробел: ').split()
    os.system('CLS')
    Y0=Exception_e_brief(array_with_variables[0])#Исключение "Й" из таблицы ASCII из y1
    Y1=Exception_e_brief(array_with_variables[2])#Исключение "Й" из таблицы ASCII из y2
    y1=ord(array_with_variables[0])-1040-Y0#Начальная вертикаль
    x1=int(array_with_variables[1])-1#Начальная горизонталь
    y2=ord(array_with_variables[2])-1040-Y1#Конечная вертикаль
    x2=int(array_with_variables[3])-1#Конечная горизонталь
    u=0
    if y1==y2:
        for x in range(numerical_number_of_ship_decks):
            if abs(x2-x1)+1==numerical_number_of_ship_decks and game_board[players_digital_number][y1][x1 + x]!=2 and game_board[players_digital_number][y1][x1 + x]!=1:
                u+=1
    elif x1 == x2:
        for x in range(numerical_number_of_ship_decks):
            if abs(y2-y1)+1==numerical_number_of_ship_decks and game_board[players_digital_number][y1+x][x1]!=2 and game_board[players_digital_number][y1+x][x1]!=1:
                u+=1
    return u
def Input(game_board,player_or_robot,autofill):
    for players_digital_number in range(2):
        letter_number_of_the_player=Letter_number_of_the_player(players_digital_number)[0].upper()+Letter_number_of_the_player()[1:]+'ый'
        print(letter_number_of_the_player+' игрок расставляет корабли.')
        for digital_number_of_the_ship in range(1,5):
            letter_number_of_the_ship=Ship_letter_number_calculator(digital_number_of_the_ship)
            p=0
            while 1!=0:
                if p==0:
                    g='К'
                    p=1
                elif p==1:
                    g='Данная кординаты недопустимы. Введите к'
                if players_digital_number==1:
                    if player_or_robot==0:
                        x=Randint(0,9)
                        y=Randint(0,9)
                    elif autofill==0:
                        x=Randint(0,9)
                        y=Randint(0,9)
                        array_with_variables=input(g + 'ординаты '+letter_number_of_the_ship+' однопалубного корабля через пробел: ').split()
                        os.system('CLS')
                        Y=Exception_e_brief(array_with_variables[0])#Исключение "Й" из таблицы ASCII из y
                        y=ord(array_with_variables[0])-1040-Y#Вертикаль
                        x=int(array_with_variables[1])-1#Горизонталь
                else:
                    if autofill==0:
                        x=Randint(0,9)
                        y=Randint(0,9)
                    else:
                        array_with_variables=input(g + 'ординаты '+letter_number_of_the_ship+' однопалубного корабля через пробел: ').split()
                        Y=Exception_e_brief(array_with_variables[0])#Исключение "Й" из таблицы ASCII из y
                        y=ord(array_with_variables[0])-1040-Y#Вертикаль
                        x=int(array_with_variables[1])-1#Горизонталь
                if game_board[players_digital_number][y][x]!=1 and game_board[players_digital_number][y][x]!=2:
                    break
            Perimeter(y,3,x,3,players_digital_number)
            game_board[0][y][x]=1
            print(' ',end='  ')
            for i in range(10):
                if i==9:
                    print('К')
                else:
                    print(chr(1040+i),end=' ')
            for i in range(10):
                if i<9:
                    print(i+1,end='  ')
                else:
                    print(10,end=' ')
                for x in range(10):
                    print(game_board[players_digital_number][x][i],end=' ')
                print()
        for numerical_number_of_ship_decks in range(2,5):
            for digital_number_of_the_ship in range(1,5-numerical_number_of_ship_decks+1):
                letter_number_of_the_ship=Ship_letter_number_calculator(digital_number_of_the_ship)
                if numerical_number_of_ship_decks==2:
                    ur=' двух'
                elif numerical_number_of_ship_decks==3:
                    ur=' трех'
                else:
                    ur=' четырех'
                p=0
                while 1!=0:
                    u=0
                    Multydeck_ship_input(numerical_number_of_ship_decks,letter_number_of_the_ship,ur,players_digital_number)
#                    if autofill==0:
#                        
#                    else:
#                        if player_or_robot==1:
#                            Multydeck_ship_input(numerical_number_of_ship_decks,letter_number_of_the_ship,ur,players_digital_number)
#                        elif player_or_robot==0:
#                            if players_digital_number==1:
#
#                            else:
#                                Multydeck_ship_input(numerical_number_of_ship_decks,letter_number_of_the_ship,ur,players_digital_number)
                    if u==numerical_number_of_ship_decks:
                        break
                        
                if y1>y2:
                    y1,y2=y2,y1
                if x1>x2:
                    x1,x2=x2,x1
                if y1==y2:
                    Perimeter(y1,3,x1,numerical_number_of_ship_decks+2,players_digital_number)
                    for i in range(numerical_number_of_ship_decks):
                        game_board[players_digital_number][y1][x1+i]=1
                elif x1==x2:
                    Perimeter(y1,numerical_number_of_ship_decks+2,x1,3,players_digital_number)
                    for i in range(numerical_number_of_ship_decks):
                        game_board[players_digital_number][y1+i][x1]=1
                print(' ',end=' ')
                for i in range(10):
                    if i==9:
                        print('К')
                    else:
                        print(chr(1040+i))
                for i in range(10):
                    print(i+1,end=' ')
                    for x in range(10):
                        print(game_board[players_digital_number][x][i],end=' ')
                    print()
    os.system('CLS')
    p=0
    return game_board
def Battle(game_board,player_or_robot,complexity):
    victory_counter=[20 for i in range (2)]
    while victory_counter[0]!=0 or victory_counter[1]!=0:
        for players_digital_number in range(2):
            c=1
            while c==1:
                c=0
                if player_or_robot==1:
                    print('Стреляет '+Letter_number_of_the_player()+'ый игрок.')
                else:
                    if players_digital_number==1:
                        print('Стреляет компьютер.')
                    else:
                        print('Стреляет игрок.')
                while 1!=0:
                    if p==0:
                        p=1
                        g='К'
                    else:
                        g='Вы уже стреляли в эту точку. Введите к'
                    if player_or_robot==1:
                        array_with_variables=input(g + 'ординаты выстрела через пробел:').split()
                        Y=Exception_e_brief(array_with_variables[0])
                        y=ord(array_with_variables[0])-1040-Y
                        x=array_with_variables[0]-1
                    else:
                        if complexity==2:
                            while 1!=2:
                                x=Randint(0,9)
                                y=Randint(0,9)
                                if abs(x%2-y%2)==1:
                                    break
                        else:
                            x=Randint(0,9)
                            y=Randint(0,9)
                    if game_board[1-players_digital_number][y][x]!=3:
                        break
                if game_board[1-players_digital_number][y][x]==1:
                    victory_counter[players_digital_number]-=1
                    c=1
                    game_board[1-players_digital_number][y][x]='*'
                else:
                    game_board[1-players_digital_number][y][x]=3
                os.system('CLS')
                print(' ',end='  ')
                for i in range(10):
                    if i==9:
                        print('К')
                    else:
                        print(chr(1040+i),end=' ')
                for i in range(10):
                    if i<9:
                        print(i+1,end='  ')
                    else:
                        print(10,end=' ')
                    for x in range(10):
                        if game_board[players_digital_number][x][y]==1 or game_board[players_digital_number][x][y]==2:
                            print(0,end=' ')
                        else:
                            print(game_board[players_digital_number][x][y],end=' ')
                    print()
                if victory_counter[0]==0 or victory_counter[1]==0:
                    break
            if victory_counter[0]==0:
                return 0
            if victory_counter[1]==0:
                return 1
def Victory(victory_counter,player_or_robot):
    if victory_counter==0:
        print('Первый игрок победил!')
    if victory_counter==1:
        if player_or_robot==0:
            print('Второй игрок победил!')
        else:
            print('Компьютер победил!')
    for players_digital_number in range(2):
        print('Поле'+Letter_number_of_the_player()+'ого игрока:')
        print(' ',end='  ')
        for y in range(10):
            if y==9:
                print('К')
            else:
                print(chr(1040+y),end=' ')
        for i in range(10):
            if i<9:
                print(i+1,end='  ')
            else:
                print(10,end=' ')
            for x in range(10):
                print(game_board[players_digital_number][x][i],end=' ')
            print()
#
#
#
game_board=[[[0 for i in range(10)] for x in range(10)] for p in range(2)]
player_or_robot=Player_or_robot()
if player_or_robot==0:
    complexity=Complexity()
autofill=Autofill()
if player_or_robot=='С человеком':
    Victory(Battle(Input(game_board,0,autofill),0),0,complexity)
else:
    Victory(Battle(Input(game_board,1,autofill),1),1,complexity)