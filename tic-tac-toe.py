import random
board= [[1,2,3], [4,5,6],[7,8,9]]





def DisplayBoard(board):
    
    print("+-------------+-------------+-------------+")
    print("|             |             |             |")
    print("|     ",board[0][0],"     |     ",board[0][1],"     |     ",board[0][2],"     |")
    print("|             |             |             |")
    print("+-------------+-------------+-------------+")
    print("|             |             |             |")
    print("|     ",board[1][0],"     |     ",board[1][1],"     |     ",board[1][2],"     |")
    print("|             |             |             |")
    print("+-------------+-------------+-------------+")
    print("|             |             |             |")
    print("|     ",board[2][0],"     |     ",board[2][1],"     |     ",board[2][2],"     |")
    print("|             |             |             |")
    print("+-------------+-------------+-------------+")
    
DisplayBoard(board)
print("La computadora jugará primero con las Xs")
board[1][1]="X"
DisplayBoard(board)
#
# la función acepta un parámetro el cual contiene el estado actual del tablero
# y lo muestra en la consola
#



def EnterMove(board):
    lstFreeFields = MakeListOfFreeFields(board)
    print(lstFreeFields)
    # Obtener dato correcto
    #while True:
    while game_over == False:
        position = input("Ingrese posición de la O: ")
        fila, columna = traduciDatoIn(position)
        if position not in (1, 2, 3, 4, 5, 6, 7, 8, 9):
            print("chrukIngrese posición válida de la O ")
        if (fila, columna) not in lstFreeFields:
            print("pupuIngrese posición válida de la O ")
        if position in ["O", "X"]:
            print("22----Ingrese posición válida de la O ")
        if not position:
            print("ficuriIngrese posición válida de la O")
        else:
            position1 = int(position) 
            break

 #Traducir position de usuario en elemento de lista
    
    fila, columna = traduciDatoIn(position1)
    
    board[fila][columna] = "O"
    #print (fila, columna)
    
    

                
                
def traduciDatoIn(position):
    if position == 1 or position == 2 or position == 3:
        fila = 0
    elif position == 4 or position == 5 or position == 6:
        fila = 1
    else:
        fila = 2

    if position == 1 or position == 4 or position == 7:
        columna = 0
    elif position == 2 or position == 5 or position == 8:
        columna = 1
    else: 
        columna = 2
    return fila, columna



def MakeListOfFreeFields(board):
    lstFreeFields = []
    for i in range (3):
        for j in range (3):
            if board[i][j] not in ["O", "X"]:
                lstFreeFields.append((i, j))
    return lstFreeFields

def VictoryFor(board, sign):
    if sign == "X":
        ganador = "Computadora"
    if sign == "O":
        ganador = "Usted"

    for i in range (3):
        if board[i][0] == sign and board[i][1] == sign and board[i][2] == sign:
            return ganador
        if board[0][i] == sign and board[1][i] == sign and board[2][i] == sign:
            return ganador
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return ganador
    if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return ganador

def DrawMove(board):
    lstFreeFields = MakeListOfFreeFields(board) #ver los lugares vacios
    com = len(lstFreeFields)
    if com > 0:
        lugar = random.randrange(com)
        fila, columna = lstFreeFields[lugar]
        board[fila][columna] = "X"

# LOOP PRINCIPAL
game_over = False
while game_over == False:
    EnterMove(board)
    ganadorcio = VictoryFor(board, "O")
    if ganadorcio == "Usted":
        print("El ganador es usted")
        game_over = True
        break
    DisplayBoard(board)
    DrawMove(board)
    ganadorcio = VictoryFor(board, "X")
    if ganadorcio == "Computadora":
        print("El ganador es la computadora")
        game_over = True
        break
    DisplayBoard(board)
    lstvacios = MakeListOfFreeFields(board)
    if ganadorcio not in ("Usted", "Computadora") and not lstvacios:
        print("Empate!")
        game_over = True
        break
    DisplayBoard(board)
DisplayBoard(board)



