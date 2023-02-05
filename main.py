victory_counter=[[20]for i in range (2)]
game_board=[[[0 for i in range(10)] for j in range(10)] for p in range(2)]
def Ship_letter_number_calculator(a):
    if a==1:
        return 'первого'
    elif a==2:
        return 'второго'
    elif a==3:
        return 'третьего'
    else:
        return 'четвертого'
def Perimeter(a,b,c,d):
    for i in range(b):
        for j in range(d):
            game_board[players_digital_number][the_first_cordinate-a+i][the_second_cordinate-c+j]=2
def Perimeter_multideck(a,b,c,d):
    for i in range(b):
        for j in range(d):
            game_board[_players_digital_number][a+i][c+j]=2
def Exception_e_brief(a):
    if ord(a)==1050:
        return 1
    else:
        return 0
def Letter_number_of_the_player():
    if the_players_digital_number==0:
        return 'перв'
    else:
        return 'второ'
for the_players_digital_number in range(2):
    letter_number_of_the_player=Letter_number_of_the_player()[0].upper()+Letter_number_of_the_player()[1:]+'ый'
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
            Y=Exception_e_brief(array_with_variables[0])
            the_first_cordinate=ord(array_with_variables[0])-1040-Y
            the_second_cordinate=int(array_with_variables[1])-1
            if game_board[the_players_digital_number][the_first_cordinate][the_second_cordinate]!=1 and game_board[the_players_digital_number][the_first_cordinate][the_second_cordinate]!=2:
                break
#        for i in range(3):
#           for j in range(3):
#               if the_first_cordinate-1+i>=0 and the_second_cordinate-1+j>=0:
#                   game_board[players_digital_number][the_first_cordinate-1+i][the_second_cordinate-1+j]=2
        if the_first_cordinate==0:
            if the_second_cordinate==0:
                Perimeter(0,2,0,2)
            elif the_second_cordinate==9:
                Perimeter(0,2,1,2)
            else:
                Perimeter(0,2,1,3)
        elif the_first_cordinate==9:
            if the_second_cordinate==0:
                Perimeter(1,2,0,2)
            elif the_second_cordinate==9:
                Perimeter(1,2,1,2)
            else:
                Perimeter(1,2,1,3)
        else:
            if the_second_cordinate==0:
                Perimeter(1,3,0,2)
            elif the_second_cordinate==9:
                Perimeter(1,3,1,2)
            else:
                Perimeter(1,3,1,3)
        game_board[0][the_first_cordinate][the_second_cordinate]=1
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
                Y0=Exception_e_brief(Array_with_variables[0])
                Y1=Exception_e_brief(Array_with_variables[2])
                the_first_initial_cordinate=ord(Array_with_variables[0])-1040-Y0
                the_second_initial_cordinate=int(Array_with_variables[1])-1
                the_first_final_cordinate=ord(Array_with_variables[2])-1040-Y1
                the_second_final_cordinate=int(Array_with_variables[3])-1
                if the_first_initial_cordinate > the_first_final_cordinate:
                    the_first_initial_cordinate,the_first_final_cordinate=the_first_final_cordinate,The_first_initial_cordinate
                if the_second_initial_cordinate>the_second_final_cordinate:
                    the_second_initial_cordinate,the_second_final_cordinate=the_second_final_cordinate,The_second_initial_cordinate
                if the_first_initial_cordinate==the_first_final_cordinate:
                    for j in range(numerical_number_of_ship_decks):
                        if the_second_final_cordinate-the_second_initial_cordinate+1==numerical_number_of_ship_decks and game_board[the_players_digital_number][the_first_initial_cordinate][the_second_initial_cordinate + j] != 2 and game_board[the_players_digital_number][the_first_initial_cordinate][the_second_initial_cordinate + j] != 1:
                            u=1
                elif the_second_initial_cordinate == the_second_final_cordinate:
                    for j in range(numerical_number_of_ship_decks):
                        if the_first_final_cordinate-the_first_initial_cordinate+1==numerical_number_of_ship_decks and game_board[the_players_digital_number][the_first_initial_cordinate+j][the_second_initial_cordinate]!=2 and game_board[the_players_digital_number][the_first_initial_cordinate+j][the_second_initial_cordinate]!=1:
                            u=1
                if u==1:
                    break
            if the_first_initial_cordinate==the_first_final_cordinate:
                if the_first_initial_cordinate==0:
                    if the_second_initial_cordinate==0:
                        Perimeter_multideck(0,2,0,numerical_number_of_ship_decks+1)
                    elif the_second_final_cordinate==9:
                        Perimeter_multideck(0,2,9-numerical_number_of_ship_decks,numerical_number_of_ship_decks+1)
                    else:
                        Perimeter_multideck(0,2,the_second_initial_cordinate-1,numerical_number_of_ship_decks+2)
                elif the_first_initial_cordinate==9:
                    if the_second_initial_cordinate==0:
                        Perimeter_multideck(8,2,0,numerical_number_of_ship_decks+1)
                    elif the_second_final_cordinate==9:
                        Perimeter_multideck(8,2,9-numerical_number_of_ship_decks,numerical_number_of_ship_decks+1)
                    else:
                        Perimeter_multideck(8,2,the_second_initial_cordinate-1,numerical_number_of_ship_decks+2)
                else:
                    if the_second_initial_cordinate==0:
                        Perimeter_multideck(the_first_initial_cordinate-1,3,the_second_initial_cordinate,numerical_number_of_ship_decks+1)
                    elif the_second_final_cordinate==9:
                        Perimeter_multideck(the_first_initial_cordinate-1,3,9-numerical_number_of_ship_decks,Numerical_number_of_ship_decks+1)
                    else:
                        Perimeter_multideck(the_first_initial_cordinate-1,3,the_second_initial_cordinate-1,numerical_number_of_ship_decks+2)
                for i in range(numerical_number_of_ship_decks):
                    game_board[the_players_digital_number][the_first_initial_cordinate][the_second_initial_cordinate+i]=1
            elif the_second_initial_cordinate==the_second_final_cordinate:
                if the_second_initial_cordinate==0:
                    if the_first_initial_cordinate==0:
                        Perimeter_multideck(0,numerical_number_of_ship_decks+1,0,2)
                    elif the_first_final_cordinate==9:
                        Perimeter_multideck(9-numerical_number_of_ship_decks,numerical_number_of_ship_decks+1,0,2)
                    else:
                        Perimeter_multideck(the_first_initial_cordinate-1,numerical_number_of_ship_decks+2,0,2)
                elif the_second_initial_cordinate==9:
                    if the_first_initial_cordinate==0:
                        Perimeter_multideck(0,numerical_number_of_ship_decks+1,8,2)
                    elif The_first_final_cordinate==9:
                        Perimeter_multideck(9-numerical_number_of_ship_decks,numerical_number_of_ship_decks+1,8,2)
                    else:
                        Perimeter_multideck(the_first_initial_cordinate-1,numerical_number_of_ship_decks+2,8,2)
                else:
                    if the_first_initial_cordinate==0:
                        Perimeter_multideck(0,numerical_number_of_ship_decks+1,the_second_initial_cordinate-1,3)
                    elif the_first_final_cordinate==9:
                        Perimeter_multideck(9-numerical_number_of_ship_decks,numerical_number_of_ship_decks+1,the_second_initial_cordinate-1,3)
                    else:
                        Perimeter_multideck(the_first_initial_cordinate-1,numerical_number_of_ship_decks+2,the_second_initial_cordinate-1,3)
                for i in range(numerical_number_of_ship_decks):
                    game_board[players_digital_number][the_first_initial_cordinate+i][the_second_initial_cordinate]=1
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
    for i in range(300):
        print()
p=0
while victory_counter[0]!=0 or victory_counter[1]!=0:
    for players_digital_number in range(2):
        c=1
        while c==1:
            c=0
            print('Стреляет '++Letter_number_of_the_player()+'ый игрок')
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
                if game_board[1-the_players_digital_number][i][j]==3:
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
if first_players_victory_counter==0:
    print('Первый игрок победил!')
if second_players_victory_counter==0:
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