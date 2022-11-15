import logic
import Board
import random

class Tictactoe():
    def __init__(self,playerX,playerO):
        self.CHESS=[None,"X","O"]
        self.board=Board.Board()
        self.winner=None
        self.playerX=playerX
        self.playerO=playerO
        self.currentplayer=self.playerX
        self.turn=0

    def game_not_over(self):
        self.winner=logic.check_winner(self.board)
        if self.winner==None:
            return True
        else:
            return False

    def get_current_player(self):
        return self.currentplayer

    def run(self):
        while self.game_not_over():
            if not logic.moveChess(self.board,self.get_current_player()):
                continue
            self.winner=logic.check_winner(self.board)
            self.other_player()
        self.end()



    def end(self):

        print(self.board)
        if self.winner==None:
            print("Draw!")
        else:
            self.other_player()
            print("Player{} win the game!".format(self.currentplayer.get_chess()))

    def other_player(self):
        """Given the character for a player, returns the other player."""
        if self.currentplayer==self.playerX:
            self.currentplayer=self.playerO
        elif self.currentplayer==self.playerO:
            self.currentplayer=self.playerX

class Human():
    def __init__(self,chess):
        self.chess=chess

    def get_move(self,board):
        instream = input("Player{} please choose a position in format x,y to place chess:".format(self.chess))
        return logic.getInput(instream,board)

    def get_chess(self):
        return self.chess

class AI():
    def __init__(self,chess):
        self.chess=chess

    def get_move(self,board):
        x=random.randint(0,2)
        y=random.randint(0,2)
        round=0
        while not logic.board_movable(x,y,board):
            if round%2==0:
                x=logic.roundadd(x,0,2)
            else:
                y=logic.roundadd(y,0,2)
            round+=1
        return x,y

    def get_chess(self):
        return self.chess

