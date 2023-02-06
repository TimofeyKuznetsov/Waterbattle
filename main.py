import os
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
        for j in range(d):
            if a-1+i>=0 and c-1+j>=0 and a-1+i<=9 and c-1+j<=9:
                game_board[players_digital_number][a-1+i][c-1+j]=2
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
def Input(game_board):
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
                for j in range(10):
                    print(game_board[players_digital_number][j][i],end=' ')
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
                    if p==0:
                        g='К'
                        p=1
                    elif p==1:
                        g='Данные кординаты недопустимы. Введите к'
                    array_with_variables=input(g+'ординаты '+letter_number_of_the_ship+ur+'палубного корабля через пробел: ').split()
                    Y0=Exception_e_brief(array_with_variables[0])#Исключение "Й" из таблицы ASCII из y1
                    Y1=Exception_e_brief(array_with_variables[2])#Исключение "Й" из таблицы ASCII из y2
                    y1=ord(array_with_variables[0])-1040-Y0#Начальная вертикаль
                    x1=int(array_with_variables[1])-1#Начальная горизонталь
                    y2=ord(array_with_variables[2])-1040-Y1#Конечная вертикаль
                    x2=int(array_with_variables[3])-1#Конечная горизонталь
                    if y1>y2:
                        y1,y2=y2,y1
                    if x1>x2:
                        x1,x2=x2,x1
                    if y1==y2:
                        for j in range(numerical_number_of_ship_decks):
                            if x2-x1+1==numerical_number_of_ship_decks and game_board[players_digital_number][y1][x1 + j] != 2 and game_board[players_digital_number][y1][x1 + j] != 1:
                                u=1
                    elif x1 == x2:
                        for j in range(numerical_number_of_ship_decks):
                            if y2-y1+1==numerical_number_of_ship_decks and game_board[players_digital_number][y1+j][x1]!=2 and game_board[players_digital_number][y1+j][x1]!=1:
                                u=1
                    if u==1:
                        break
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
                    for j in range(10):
                        print(game_board[players_digital_number][j][i],end=' ')
                    print()
        os.system('CLS')
    p=0
    return game_board
def Battle(game_board):
    while victory_counter[0]!=0 or victory_counter[1]!=0:
        for players_digital_number in range(2):
            c=1
            while c==1:
                c=0
                print('Стреляет '+Letter_number_of_the_player()+'ый игрок')
                while 1!=0:
                    if p==0:
                        p=1
                        g='К'
                    else:
                        g='Вы уже стреляли в эту точку. Введите к'
                    d=input(g + 'ординаты выстрела через пробел:').split()
                    if ord(d[0])==1050:
                        Y=1
                    i=ord(d[0])-1040-Y
                    j=d[0]-1
                    if game_board[1-players_digital_number][i][j]==3:
                        break
                if game_board[1-players_digital_number][i][j]==1:
                    victory_counter[players_digital_number]-=1
                    c=1
                    game_board[1-players_digital_number][i][j]='*'
                else:
                    game_board[1-players_digital_number][i][j]=3
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
                    for j in range(10):
                        if game_board[players_digital_number][j][i]==1 or game_board[players_digital_number][j][i]==2:
                            print(0,end=' ')
                        else:
                            print(game_board[players_digital_number][j][i],end=' ')
                    print()
                    if victory_counter[0]==0:
                        return 0
                    if victory_counter[1]==0:
                        return 1
def Victory(victory_counter):
    if victory_counter[0]==0:
        print('Первый игрок победил!')
    if victory_counter[1]==0:
        print('Второй игрок победил!')
    for players_digital_number in range(2):
        print('Поле'+Letter_number_of_the_player()+'ого игрока:')
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
            for j in range(10):
                print(game_board[players_digital_number][j][i],end=' ')
            print()
victory_counter=[[20]for i in range (2)]
game_board=[[[0 for i in range(10)] for j in range(10)] for p in range(2)]
Victory(Battle(Input(game_board)))