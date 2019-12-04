#Kim Phung
#S1102710
#PaardenSprong Opdracht 3, week 2
#---------------------------------

#Maak een schaakboard aan 8*8
chessBoard = [[1, 1, 1, 1, 1, 1, 1, 1] for i in range(8)]

#Hernoem de posities
chess_map_from_alpha_to_index = {
   "a" : 0,
   "b" : 1,
   "c" : 2,
   "d" : 3,
   "e" : 4,
   "f" : 5,
   "g" : 6,
   "h" : 7
}

chess_map_from_index_to_alpha = {
   0: "a",
   1: "b",
   2: "c",
   3: "d",
   4: "e",
   5: "f",
   6: "g",
   7: "h"
}

#Functie voor waar het paard heen kan
def getKnightMoves(pos, chessBoard):#geef hier de positie en het bord
    
    #Hier defineren wat de row en columns zijn
    column, row = list(pos.strip().lower())
    row = int(row) - 1
    column = chess_map_from_alpha_to_index[column]
    i,j = row, column
    solutionMoves = []
    try:
        #mogelijkheid poging 1: 1 rij omhoog en 2 kolom naar links
        temp = chessBoard[i + 1][j - 2]
        solutionMoves.append([i + 1, j - 2])
    except:
        pass
    try:
        temp = chessBoard[i + 2][j - 1]
        solutionMoves.append([i + 2, j - 1])
    except:
        pass
    try:
        temp = chessBoard[i + 2][j + 1]
        solutionMoves.append([i + 2, j + 1])
    except:
        pass
    try:
       temp = chessBoard[i + 1][j + 2]
       solutionMoves.append([i + 1, j + 2])
    except:
        pass
    try:
        temp = chessBoard[i - 1][j + 2]
        solutionMoves.append([i - 1, j + 2])
    except:
        pass
    try:
        temp = chessBoard[i - 2][j + 1]
        solutionMoves.append([i - 2, j + 1])
    except:
        pass
    try:
        temp = chessBoard[i - 2][j - 1]
        solutionMoves.append([i - 2, j - 1])
    except:
        pass
    try:
        temp = chessBoard[i - 1][j - 2]
        solutionMoves.append([i - 1, j - 2])
    except:
        pass

    #filteren van negatieve waarden
    temp = [i for i in solutionMoves if i[0] >=0 and i[1] >=0]
    global allPossibleMoves
    allPossibleMoves = ["".join([chess_map_from_index_to_alpha[i[1]], str(i[0] + 1)]) for i in temp]
    allPossibleMoves.sort()
    return allPossibleMoves

#Vraag input
pos = (input("Wat is je positie? "))
#Activate function
getKnightMoves(pos, chessBoard)

#print("Je kan naar:",getKnightMoves(pos, chessBoard)) <---- deze printline om te laten zien wat mogelijk is vanaf die positie

#Vraag bestemming
newPos = (input("Waar wil je heen? "))

#zet input in lowercases om fouten te voorkomen
newPos = newPos.lower()

#if else checkt of de nieuwe positie binnen de functie zit en print de juiste statement uit
if newPos in allPossibleMoves:
    print ("het paard kan springen van",pos,"naar",newPos)
else:
    print ("het paard kan niet springen van",pos,"naar",newPos)

