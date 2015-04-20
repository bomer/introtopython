#Tic Tac Toe
Board=["0","1","2","3","4","5","6","7","8","9"]
Players=['O','X']
Turn=True
def DisplayBoard(Board):
    print
    print Board[1]," | ",Board[2]," | ", Board[3]
    print "-------------"
    print Board[4]," | ",Board[5]," | ", Board[6]
    print "-------------"
    print Board[7]," | ",Board[8]," | ", Board[9]
    print "-------------"

def handleInput():
    global Board,Players,Turn

    position=input("Which position:? ")    
    #validate if valid or not in board, if not valid, re-ask questions
    while position<1 or position>9:
        position= input("Invalid Input! Which position:? ")
    #check not already taken
    print 'checking...'
    print Board[position] 
    while (Board[position]=='X' or Board[position]=='Y'):
        position= input("Position already taken! Which position:? ")
    Board[position]=Players[Turn]
    Turn=not Turn
    return position
    

def checkWinner(Board):
    #check board co-ordinates for winning combinations
    return False

DisplayBoard(Board)

#Main Game Loop
while not checkWinner(Board):
    position=handleInput()
    DisplayBoard(Board)
    

