import os
import random
import platform
def Input_cordinate_shoot(g):
    array_with_variables=input(g + 'ординаты выстрела через пробел: ').split()
    Y=int(ord(array_with_variables[0])==1050)
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
    while True:
        x,y=Randint(0,9)
        if abs(x%2-y%2)==a:
            break
def Perimeter(a,b,c,d,players_digital_number,game_board):
    for y in range(b):
        for x in range(d):
            if a-1+y>=0 and c-1+x>=0 and a-1+y<=9 and c-1+x<=9:
                game_board[players_digital_number][a-1+y][c-1+x]=5
    return game_board
def Randint(a,b):
    return random.randint(a,b),random.randint(a,b)
def Multydeck_ship_input(numerical_number_of_ship_decks,letter_number_of_the_ship,ur,players_digital_number,repetition_counter,game_board):
    place_check=0
    if repetition_counter==0:
        question_text='К'
        repetition_counter=1
    else:
        question_text='Данные кординаты недопустимы. Введите к'
    array_with_variables=input(question_text+'ординаты '+letter_number_of_the_ship+ur+'палубного корабля через пробел: ').split()
    os.system('CLS')
    Y0=int(ord(array_with_variables[0])==1050)#Исключение "Й" из таблицы ASCII из y1
    Y1=int(ord(array_with_variables[2])==1050)#Исключение "Й" из таблицы ASCII из y2
    x1=ord(array_with_variables[0])-1040-Y0#Начальная вертикаль
    y1=int(array_with_variables[1])-1#Начальная горизонталь
    x2=ord(array_with_variables[2])-1040-Y1#Конечная вертикаль
    y2=int(array_with_variables[3])-1#Конечная горизонталь
    if y1==y2:
        for x in range(numerical_number_of_ship_decks):
            if abs(x2-x1)+1==numerical_number_of_ship_decks and game_board[players_digital_number][y1][x1+x]!=2 and game_board[players_digital_number][y1][x1+x]!=3 and game_board[players_digital_number][y1][x1+x]!=4 and game_board[players_digital_number][y1][x1+x]!=1 and game_board[players_digital_number][y1][x1+x]!=5:
                place_check+=1
    elif x1==x2:
        for x in range(numerical_number_of_ship_decks):
            if abs(y2-y1)+1==numerical_number_of_ship_decks and game_board[players_digital_number][y1+x][x1]!=2 and game_board[players_digital_number][y1+x][x1]!=3 and game_board[players_digital_number][y1+x][x1]!=4 and game_board[players_digital_number][y1+x][x1]!=1 and game_board[players_digital_number][y1+x][x1]!=5:
                place_check+=1
    return y1,y2,x1,x2,place_check
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
Letter_number_of_the_player={0:'перв',1:'второ'}
Ship_letter_numbers={1:'первого',2:'второго',3:'третьего',4:'четвертого'}
correct_direction=[]
game_board=[[[0 for i in range(10)] for x in range(10)] for p in range(2)]
if platform.system()=='Windows':#Определение системы для очистки консоли
    clean='cls'
else:
    clean='clear'
repetition_counter=0
while True:
    if repetition_counter==0:
        repetition_counter=1
        question_text='С кем будешь играть с человеком или с компьютером? Ответьте либо с человеком, либо с компьютером: '
    else:
        question_text='Данный ответ недопустим, ответьте либо с человеком, либо с компьютером: '
    player_or_robot=input(question_text)
    if player_or_robot=='с человеком' or player_or_robot=='с компьютером':
        break
if player_or_robot=='с компьютером':
    repetition_counter=0
    while True:
        if repetition_counter==0:
            repetition_counter=1
            question_text='Какая сложность 1-ая или 2-ая? Ответьте либо 1, либо 2: '
        else:
            question_text='Данный ответ недопустим, ответьте либо 1, либо 2: '
        complexity=input(question_text)
        if complexity=='1' or complexity=='2':
            complexity=int(complexity)
            break
repetition_counter=0
while True:
    if repetition_counter==0:
        repetition_counter=1
        question_text='Нужно автозаполнение? Ответьте либо да, либо нет: '
    else:
        question_text='Данный ответ недопустим, ответьте либо да, либо нет: '
    autofill=input(question_text)
    if autofill=='да' or autofill=='нет':
        autofill=autofill=='да'
        break
for player_digital_number in range(2):
    print(Letter_number_of_the_player[player_digital_number][0].upper()+Letter_number_of_the_player[player_digital_number][1:]+'ый'+' игрок расставляет корабли.')
    for digital_number_of_the_ship in range(1,5):
        letter_number_of_the_ship=Ship_letter_numbers[digital_number_of_the_ship]
        repetition_counter=0
        while True:
            if repetition_counter==0:
                question_text='К'
                repetition_counter=1
            elif repetition_counter==1:
                question_text='Данная кординаты недопустимы. Введите к'
            if autofill==1 or (player_digital_number==1 and player_or_robot==1):
                x,y=random.randint(0,9),random.randint(0,9)
            else:
                array_with_variables=input(question_text + 'ординаты '+letter_number_of_the_ship+' однопалубного корабля через пробел: ').split()
                Y=int(ord(array_with_variables[0])==1050)#Исключение "Й" из таблицы ASCII из y
                x=ord(array_with_variables[0])-1040-Y#Вертикаль
                y=int(array_with_variables[1])-1#Горизонталь
            if game_board[player_digital_number][y][x]!=1 and game_board[player_digital_number][y][x]!=5:
                break
        game_board=Perimeter(y,3,x,3,player_digital_number,game_board)
        game_board[player_digital_number][y][x]=1
        os.system('CLS')
        Output(game_board,player_digital_number,1)
    for numerical_number_of_ship_decks in range(2,5):
        for digital_number_of_the_ship in range(1,6-numerical_number_of_ship_decks):
            letter_number_of_the_ship=Ship_letter_numbers[digital_number_of_the_ship]
            if numerical_number_of_ship_decks==2:
                ur=' двух'
            elif numerical_number_of_ship_decks==3:
                ur=' трех'
            else:
                ur=' четырех'
            repetition_counter=0
            while True:
                if autofill==1:
                    y1,y2,x1,x2,u=Multydeck_ship_autofill(numerical_number_of_ship_decks,game_board,player_digital_number)
                elif player_or_robot==0:
                    y1,y2,x1,x2,u=Multydeck_ship_input(numerical_number_of_ship_decks,letter_number_of_the_ship,ur,player_digital_number,repetition_counter,game_board)
                elif player_or_robot==1 and player_digital_number==1:
                    y1,y2,x1,x2,u=Multydeck_ship_autofill(numerical_number_of_ship_decks,game_board,player_digital_number)
                else:
                    y1,y2,x1,x2,u=Multydeck_ship_input(numerical_number_of_ship_decks,letter_number_of_the_ship,ur,player_digital_number,repetition_counter,game_board)
                if u==numerical_number_of_ship_decks:
                    print(u,numerical_number_of_ship_decks,'Это нужно')
                    break
            y1,y2,x1,x2=min(y1,y2),max(y1,y2),min(x1,x2),max(x1,x2)
            if y1==y2:
                game_board=Perimeter(y1,3,x1,numerical_number_of_ship_decks+2,player_digital_number,game_board)
                for repetition_counter in range(numerical_number_of_ship_decks):
                    game_board[player_digital_number][y1][x1+repetition_counter]=1
            elif x1==x2:
                game_board=Perimeter(y1,numerical_number_of_ship_decks+2,x1,3,player_digital_number,game_board)
                for repetition_counter in range(numerical_number_of_ship_decks):
                    game_board[player_digital_number][y1+repetition_counter][x1]=numerical_number_of_ship_decks
#            os.system('CLS')
            Output(game_board,player_digital_number,1)
            print(digital_number_of_the_ship)
#os.system('CLS')
repetition_counter=0
for player_digital_number in range(2):
    for x in range(10):
        for y in range(10):
            if game_board[player_digital_number][y][x]==5:
                game_board[player_digital_number][y][x]=0
k=False
victory_counter=[20 for i in range (2)]
while victory_counter[0]!=0 or victory_counter[1]!=0:
    for player_digital_number in range(2):
        c=1
        while c==1:
            c=0
            if player_or_robot==0:
                print('Стреляет '+Letter_number_of_the_player[player_digital_number]+'ый игрок.')
            elif player_digital_number==1:
                print('Стреляет компьютер.')
            else:
                print('Стреляет игрок.')
            repetition_counter=0
            repetition_counter=0
            while True:
                if repetition_counter==0:
                    repetition_counter=1
                    question_text='К'
                elif repetition_counter==1:
                    question_text='Вы уже стреляли в эту точку. Введите к'
                else:
                    question_text='Нет смысла туда стрелять. Введите к'
                    repetition_counter=1
                if player_or_robot==0:
                    Y,y,x=Input_cordinate_shoot(question_text)
                elif player_digital_number==0:
                    Y,y,x=Input_cordinate_shoot(question_text)
                elif complexity==2:
#                    if k:
#                        direction=random.random(correct_direction)
#                    else:
                    Tactics(repetition_counter//50)
                else:
#                    if k:
#                    else:
                    x,y=Randint(9)
                if game_board[1-player_digital_number][y][x]!=6 and game_board[1-player_digital_number][y][x]!='*':
                    repetition_counter+=complexity==2
                    break
            if game_board[1-player_digital_number][y][x]==1:
                victory_counter[player_digital_number]-=1
                c=1
                if game_board[1-player_digital_number][y][x]==1 and player_or_robot==1:
#                    ship_len,minus_ship_len=game_board[1-players_digital_number][y][x]
#                    if minus_ship_len==0:
#                        minus_ship_len=game_board[1-players_digital_number][y][x]-1
#                        correct_direction=[]
#                        correct_direction=Direction(y,x)
#                        k=True
#                    elif minus_ship_len>1:
#                        minus_ship_len-=1
#                    else:
#                        minus_ship_len=0
#                        if correct_direction
                    game_board[1-player_digital_number][y][x]=6
            else:
                game_board[1-player_digital_number][y][x]='*'
            os.system('CLS')
            Output(game_board,player_digital_number,0)
            if victory_counter[0]==0 or victory_counter[1]==0:
                break
if victory_counter==0:
    print('Первый игрок победил!')
elif victory_counter==0 and player_or_robot==1:
    print('Игрок победил!')
elif player_or_robot==0:
    print('Второй игрок победил!')
else:
    print('Компьютер победил!')
for player_digital_number in range(2):
    print('Поле'+Letter_number_of_the_player[player_digital_number]+'ого игрока:')
    Output(game_board,player_digital_number,1)
Victory(Battle(Input(game_board,int(player_or_robot!='с человеком'),autofill,correct_direction),int(player_or_robot!='с человеком'),complexity),int(player_or_robot!='с человеком'))