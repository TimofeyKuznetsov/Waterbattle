import os
import random
def Exception_e_brief(a):
    if ord(a)==1050:
        return 1
    else:
        return 0
def Input_cordinate_shoot(g):
    array_with_variables=input(g + 'ординаты выстрела через пробел: ').split()
    Y=Exception_e_brief(array_with_variables[0])
    y=ord(array_with_variables[0])-1040-Y
    x=int(array_with_variables[1])-1
    return Y,y,x
def Direction_check(a,b,numerical_number_of_ship_decks,c,players_digital_number,d,game_board):
    u=0
    if c==0:
        for i in range(numerical_number_of_ship_decks):
            if game_board[players_digital_number][a+i*b][d]!=1 and game_board[players_digital_number][a+i*b][d]!=2 and game_board[players_digital_number][a+i*b][d]!=3 and game_board[players_digital_number][a+i*b][d]!=4 and game_board[players_digital_number][a+i*b][d]!=5:
                u+=1
    else:
        for i in range(numerical_number_of_ship_decks):
            if game_board[players_digital_number][d][a+i*b]!=1 and game_board[players_digital_number][d][a+i*b]!=2 and game_board[players_digital_number][d][a+i*b]!=3 and game_board[players_digital_number][d][a+i*b]!=4 and game_board[players_digital_number][d][a+i*b]!=5:
                u+=1
    return a-(numerical_number_of_ship_decks-1),u
def Lines():
    print(' ',end='  ')
    for i in range(10):
        print(chr(1040+i+i//9),end=' ')
    print()
def Output(game_board,players_digital_number,a):
    Lines()
    for x in range(10):
        print(x+1,end=(' '*(2-x//9)))
        for y in range(10):
            if game_board[players_digital_number][x][y]==1 or game_board[players_digital_number][x][y]==2 or game_board[players_digital_number][x][y]==3 or game_board[players_digital_number][x][y]==4:
                print(a*((game_board[players_digital_number][x][y]==5)+1),end=' ')
            else:
                print(game_board[players_digital_number][x][y],end=' ')
        print()
def Tactics(a):
    while 1!=2:
        x,y=Randint(0,9)
        if abs(x%2-y%2)==a:
            break
def Ship_letter_number_calculator(a):
    if a==1:
        return 'первого'
    elif a==2:
        return 'второго'
    elif a==3:
        return 'третьего'
    else:
        return 'четвертого'
def Perimeter(a,b,c,d,players_digital_number,game_board):
    for y in range(b):
        for x in range(d):
            if a-1+y>=0 and c-1+x>=0 and a-1+y<=9 and c-1+x<=9:
                game_board[players_digital_number][a-1+y][c-1+x]=5
    return game_board
def Letter_number_of_the_player(players_digital_number):
    if players_digital_number==0:
        return 'перв'
    else:
        return 'второ'
def Randint(a,b):
    return random.randint(a,b),random.randint(a,b)
def Player_or_robot():
    i=0
    while 1!=0:
        if i==0:
            i=1
            g='С кем будешь играть с человеком или с компьютером? Ответьте либо с человеком, либо с компьютером: '
        else:
            g='Данный ответ недопустим, ответьте либо с человеком, либо с компьютером: '
        player_or_robot=input(g)
        if player_or_robot=='с человеком' or player_or_robot=='с компьютером':
            return player_or_robot
def Autofill():
    i=0
    while 1!=0:
        if i==0:
            i=1
            g='Нужно автозаполнение? Ответьте либо да, либо нет: '
        else:
            g='Данный ответ недопустим, ответьте либо да, либо нет: '
        autofill=input(g)
        if autofill=='да' or autofill=='нет':
            break
    if autofill=='да':
        return 1
    else:
        return 0
def Complexity():
    i=0
    while 1!=0:
        if i==0:
            i=1
            g='Какая сложность 1-ая или 2-ая? Ответьте либо 1, либо 2: '
        else:
            g='Данный ответ недопустим, ответьте либо 1, либо 2: '
        complexity=input(g)
        if complexity=='1' or complexity=='2':
            break
    return int(complexity)
def Multydeck_ship_input(numerical_number_of_ship_decks,letter_number_of_the_ship,ur,players_digital_number,p,u,game_board):
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
    if y1==y2:
        for x in range(numerical_number_of_ship_decks):
            if abs(x2-x1)+1==numerical_number_of_ship_decks and game_board[players_digital_number][y1][x1 + x]!=2 and game_board[players_digital_number][y1][x1 + x]!=1:
                u+=1
    elif x1 == x2:
        for x in range(numerical_number_of_ship_decks):
            if abs(y2-y1)+1==numerical_number_of_ship_decks and game_board[players_digital_number][y1+x][x1]!=2 and game_board[players_digital_number][y1+x][x1]!=1:
                u+=1
    return y1,y2,x1,x2,u
def Direction(a,b):
    correct_direction=[]
    if b!=0:
        correct_direction.append(0)
    if a!=9:
        correct_direction.append(1)
    if b!=9:
        correct_direction.append(2)
    if a!=0:
        correct_direction.append(3)
    return correct_direction
def Multydeck_ship_autofill(numerical_number_of_ship_decks,game_board,players_digital_number):
    x1,y1=Randint(0,9)
    correct_direction=[]
    correct_direction=Direction(y1,x1)
    direction=random.choice(correct_direction)
    if direction==0:
        x2,u=Direction_check(x1,-1,numerical_number_of_ship_decks,0,players_digital_number,y1,game_board)
        y2=y1
    elif direction==1:
        y2,u=Direction_check(y1,1,numerical_number_of_ship_decks,1,players_digital_number,x1,game_board)
        x2=x1
    elif direction==2:
        x2,u=Direction_check(x1,1,numerical_number_of_ship_decks,0,players_digital_number,y1,game_board)
        y2=y1
    else:
        y2,u=Direction_check(y1,-1,numerical_number_of_ship_decks,1,players_digital_number,x1,game_board)
        x2=x1
    return y1,y2,x1,x2,u
def Input(game_board,player_or_robot,autofill,correct_direction):
    for players_digital_number in range(2):
        letter_number_of_the_player=Letter_number_of_the_player(players_digital_number)[0].upper()+Letter_number_of_the_player(players_digital_number)[1:]+'ый'
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
                if autofill==1 or (players_digital_number==1 and player_or_robot==1):
                    x,y=Randint(0,9)
                else:
                    array_with_variables=input(g + 'ординаты '+letter_number_of_the_ship+' однопалубного корабля через пробел: ').split()
                    Y=Exception_e_brief(array_with_variables[0])#Исключение "Й" из таблицы ASCII из y
                    y=1#ord(array_with_variables[0])-1040-Y#Вертикаль
                    x=1#int(array_with_variables[1])-1#Горизонталь
                if game_board[players_digital_number][y][x]!=1 and game_board[players_digital_number][y][x]!=5:
                    break
            game_board=Perimeter(y,3,x,3,players_digital_number,game_board)
            game_board[players_digital_number][y][x]=1
            os.system('CLS')
            Output(game_board,players_digital_number,1)
        for numerical_number_of_ship_decks in range(2,5):
            for digital_number_of_the_ship in range(1,6-numerical_number_of_ship_decks):
                letter_number_of_the_ship=Ship_letter_number_calculator(digital_number_of_the_ship)
                if numerical_number_of_ship_decks==2:
                    ur=' двух'
                elif numerical_number_of_ship_decks==3:
                    ur=' трех'
                else:
                    ur=' четырех'
                p=0
                while 1!=0:
                    if autofill==1:
                        y1,y2,x1,x2,u=Multydeck_ship_autofill(numerical_number_of_ship_decks,game_board,players_digital_number)
                    elif player_or_robot==0:
                        y1,y2,x1,x2,u=Multydeck_ship_input(numerical_number_of_ship_decks,letter_number_of_the_ship,ur,players_digital_number,p,u,game_board)
                    elif player_or_robot==1 and players_digital_number==1:
                        y1,y2,x1,x2,u=Multydeck_ship_autofill(numerical_number_of_ship_decks,game_board,players_digital_number)
                    else:
                        y1,y2,x1,x2,u=Multydeck_ship_input(numerical_number_of_ship_decks,letter_number_of_the_ship,ur,players_digital_number,p,u,game_board)
                    if u==numerical_number_of_ship_decks:
                        print(u,numerical_number_of_ship_decks,'Это нужно')
                        break
                y1,y2,x1,x2=min(y1,y2),max(y1,y2),min(x1,x2),max(x1,x2)
                if y1==y2:
                    game_board=Perimeter(y1,3,x1,numerical_number_of_ship_decks+2,players_digital_number,game_board)
                    for i in range(numerical_number_of_ship_decks):
                        game_board[players_digital_number][y1][x1+i]=1
                elif x1==x2:
                    game_board=Perimeter(y1,numerical_number_of_ship_decks+2,x1,3,players_digital_number,game_board)
                    for i in range(numerical_number_of_ship_decks):
                        game_board[players_digital_number][y1+i][x1]=numerical_number_of_ship_decks
#                os.system('CLS')
                Output(game_board,players_digital_number,1)
                print(digital_number_of_the_ship)
#    os.system('CLS')
    p=0
    for players_digital_number in range(2):
        for x in range(10):
            for y in range(10):
                if game_board[players_digital_number][y][x]==5:
                    game_board[players_digital_number][y][x]=0
    return game_board
def Battle(game_board,player_or_robot,complexity):
    k=False
    victory_counter=[20 for i in range (2)]
    while victory_counter[0]!=0 or victory_counter[1]!=0:
        for players_digital_number in range(2):
            c=1
            while c==1:
                c=0
                if player_or_robot==0:
                    print('Стреляет '+Letter_number_of_the_player(players_digital_number)+'ый игрок.')
                elif players_digital_number==1:
                    print('Стреляет компьютер.')
                else:
                    print('Стреляет игрок.')
                i=0
                p=0
                while 1!=0:
                    if p==0:
                        p=1
                        g='К'
                    elif p==1:
                        g='Вы уже стреляли в эту точку. Введите к'
                    else:
                        g='Нет смысла туда стрелять. Введите к'
                        p=1
                    if player_or_robot==0:
                        Y,y,x=Input_cordinate_shoot(g)
                    elif players_digital_number==0:
                        Y,y,x=Input_cordinate_shoot(g)
                    elif complexity==2:
#                        if k:
#                            direction=random.random(correct_direction)
#                        else:
                        Tactics(i//50)
                    else:
#                        if k:
#
#                        else:
                        x,y=Randint(9)
                    if game_board[1-players_digital_number][y][x]!=6 and game_board[1-players_digital_number][y][x]!='*':
                        i+=complexity==2
                        break
                if game_board[1-players_digital_number][y][x]==1:
                    victory_counter[players_digital_number]-=1
                    c=1
                    if game_board[1-players_digital_number][y][x]==1 and player_or_robot==1:
#                        ship_len,minus_ship_len=game_board[1-players_digital_number][y][x]
#                        if minus_ship_len==0:
#                            minus_ship_len=game_board[1-players_digital_number][y][x]-1
#                            correct_direction=[]
#                            correct_direction=Direction(y,x)
#                            k=True
#                        elif minus_ship_len>1:
#                            minus_ship_len-=1
#                        else:
#                            minus_ship_len=0
#                            if correct_direction
                        game_board[1-players_digital_number][y][x]=6
                else:
                    game_board[1-players_digital_number][y][x]='*'
                os.system('CLS')
                Output(game_board,players_digital_number,0)
                if victory_counter[0]==0 or victory_counter[1]==0:
                    break
            if victory_counter[0]==0:
                return 0
            if victory_counter[1]==0:
                return 1
def Victory(victory_counter,player_or_robot):
    if victory_counter==0:
        print('Первый игрок победил!')
    elif victory_counter==0 and player_or_robot==1:
        print('Игрок победил!')
    elif player_or_robot==0:
        print('Второй игрок победил!')
    else:
        print('Компьютер победил!')
    for players_digital_number in range(2):
        print('Поле'+Letter_number_of_the_player()+'ого игрока:')
        Output(game_board,players_digital_number,1)
correct_direction=[]
game_board=[[[0 for i in range(10)] for x in range(10)] for p in range(2)]
player_or_robot=Player_or_robot()
if player_or_robot=='с компьютером':
    complexity=Complexity()
autofill=Autofill()
Victory(Battle(Input(game_board,int(player_or_robot!='с человеком'),autofill,correct_direction),int(player_or_robot!='с человеком'),complexity),int(player_or_robot!='с человеком'))