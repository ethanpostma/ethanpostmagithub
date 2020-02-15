

import sys

class newGame:
    
    def __init__(self):
        self.turn = 0
        self.player = "Red"
        self.piece = " x "
        self.winner = "   "
        
        self.board = [
            ["   ", "   ", "   ","   ", "   ", "   ", "   "],
            ["   ", "   ", "   ","   ", "   ", "   ", "   "],
            ["   ", "   ", "   ","   ", "   ", "   ", "   "],
            ["   ", "   ", "   ","   ", "   ", "   ", "   "],
            ["   ", "   ", "   ","   ", "   ", "   ", "   "],
            ["   ", "   ", "   ","   ", "   ", "   ", "   "]
            ]
        
            
    def _printBoard(self):
        print("\n\n (1) (2) (3) (4) (5) (6) (7) \n")
        for row in range(len(self.board)):
            print("|", end="")
            for collumn in range(len(self.board[row])):
                print(self.board[row][collumn], end="|")
            print("\n-----------------------------")

    def _playerMove(self):
        while True:
            userIn = input("Choose which collumn to drop your piece (1-7)\n")
            if ((len(userIn) != 1) or (userIn not in ["1","2","3","4","5","6","7"])):
                print("Please Enter a Number from 1-7\n")
                continue
            elif self.board[0][(int(userIn)-1)] != "   ":
                print("Can't Place There\n")
                continue
            else:    
                break
        
        drop = int(userIn) - 1
        for row in range((len(self.board) - 1), -1, -1):
            if self.board[row][drop] == "   ":
                self.board[row][drop] = self.piece
                break
            else:
                continue
    
    def _checkCheckWin(self, rTest, yTest):
        if (rTest == 4):
            self._printBoard()
            print("\n\nRed Wins")
            sys.exit(0)
        elif (yTest == 4):
            self._printBoard()
            print("\n\nYellow Wins")
            sys.exit(0)
        #Board Full
        elif "   " not in self.board[0]:
            self._printBoard()
            print("\n\nStalemate: Board is full")
            sys.exit(0)
    
    def _checkWin(self):
        #Horizontal
        for row in self.board:
            rTest = 0
            yTest = 0
            for collumn in row:
                if collumn == "   ":
                    rTest = 0
                    yTest = 0
                elif collumn == " x ":
                    rTest +=1
                    yTest = 0
                elif collumn == " o ":
                    yTest +=1
                    rTest = 0
                self._checkCheckWin(rTest, yTest)
        #Vertical
        for c in range(7):
            rTest = 0
            yTest = 0
            for r in range(6):
                if self.board[r][c] == "   ":
                    rTest = 0
                    yTest = 0
                elif self.board[r][c] == " x ":
                    rTest += 1
                    yTest = 0
                elif self.board[r][c] == " o ":
                    yTest += 1
                    rTest = 0
                self._checkCheckWin(rTest, yTest)
        #Diag Up
        for ru in range(4,6):
            rTest = 0
            yTest = 0
            for du in range(4):
                if self.board[(ru-du)][du] == "   ":
                    rTest = 0
                    yTest = 0
                elif self.board[(ru-du)][du] == " x ":
                    rTest += 1
                    yTest = 0
                elif self.board[(ru-du)][du] == " o ":
                    yTest += 1
                    rTest = 0
                self._checkCheckWin(rTest, yTest)
        #Diag down
        for rd in range(3):
            rTest = 0
            yTest = 0
            if self.board[4][3] == " x ":
                print("ahhhh")
            if self.board[4][3] == " o ":
                print("ahhhh")
            for dd in range(4):
                if self.board[(rd+dd)][dd] == "   ":
                    rTest = 0
                    yTest = 0
                elif self.board[(rd+dd)][dd] == " x ":
                    rTest += 1
                    yTest = 0
                elif self.board[(rd+dd)][dd] == " o ":
                    yTest += 1
                    rTest = 0
                self._checkCheckWin(rTest, yTest)
        
    def nextTurn(self):
        self._printBoard()
        if self.turn == 0:
            print()
            self.player = "Red"
            print(self.player, "Goes First (%s)" % self.piece[1])
        else:
            if (self.turn % 2) == 0:
                self.player = "\n\nRed"
                self.piece = " x "
            else:
                self.player = "\n\nYellow"
                self.piece = " o "
                
            print("\n%s's Turn (%s)\n" % (self.player, self.piece[1]))
            
        
        self._playerMove()
        self._checkWin()
        
        self.turn+=1
    


print("Welcome to Connect 4\n\nRed Pieces: x\nYellow Pieces: o\n\n\n")
game = newGame()

while True:
    game.nextTurn()

