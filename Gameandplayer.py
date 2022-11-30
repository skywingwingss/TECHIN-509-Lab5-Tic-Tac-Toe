import logic
import Board
import random
import pandas as pd
import os

class Tictactoe():
    def __init__(self,playerX,playerO):
        self.CHESS=[None,"X","O"]
        self.board=Board.Board()
        self.winner=None
        self.playerX=playerX
        self.playerO=playerO
        self.currentplayer=self.playerX
        self.turn=0
        self.database=Database()

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
            self.turn+=1
            if self.is_draw():
                break
        self.end()

    def is_draw(self):
        if self.turn==9:
            return True
        else:
            return False

    def end(self):
        print(self.board)
        winnerName =None
        if self.winner==None:
            print("Draw!")
        else:
            self.other_player()
            print("Player{} win the game!".format(self.currentplayer.get_name()))
            if self.winner=="X":
                winnerName=self.playerX.name
            elif self.winner=="0":
                winnerName=self.playerO.name
        self.database.record_game(self.playerX.name,self.playerO.name,winnerName)
        print(self.database.get_globalrank())


    def other_player(self):
        """Given the character for a player, returns the other player."""
        if self.currentplayer==self.playerX:
            self.currentplayer=self.playerO
        elif self.currentplayer==self.playerO:
            self.currentplayer=self.playerX

class Human():
    def __init__(self,chess,name):
        self.chess=chess
        self.name=name

    def get_move(self,board):
        instream = input("Player{} please choose a position in format x,y to place chess:".format(self.chess))
        return logic.getInput(instream,board)

    def get_chess(self):
        return self.chess

    def get_name(self):
        return self.name

class AI():
    def __init__(self,chess):
        self.chess=chess
        self.name="AI"

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

    def get_name(self):
        return self.name

class Database():
    def __init__(self):
        self.datapath="./data/database.csv"
        self.check_localfile()
        self.df=self.load_data()


    def check_localfile(self):
        #check existing local file and create one if failed to find.
        if not os.path.exists("./data"):
            os.mkdir("./data")
        if not os.path.exists(self.datapath):
            data={"player":["test"],
                  "win":[1],
                  "lose":[0],
                  "draw":[0],
                  "score":[1]}
            df=pd.DataFrame(data)
            df.set_index(["player"],inplace=True)
            df.to_csv(self.datapath)

    def load_data(self):
        df=pd.read_csv(self.datapath,index_col=0)
        return df

    def write_data(self):
        self.df.to_csv(self.datapath)

    def add_record(self,player,result):
        if not( player in self.df.index):
            self.df.loc[player]=[0,0,0,0]
        self.df.loc[player][result]+=1#update data
        #calculate score
        playerinfo=self.df.loc[player]
        win=playerinfo["win"]
        lose=playerinfo["lose"]
        score=win-lose
        self.df.loc[player]["score"]=score

        #self.df.loc[len(self.df)]=[player1,player2,winner]
    def record_game(self,player1,player2,winner):
        if player1==winner:
            self.add_record(player1,"win")
            self.add_record(player2,"lose")
        elif player2==winner:
            self.add_record(player1,"lose")
            self.add_record(player2,"win")
        else:
            self.add_record(player1,"draw")
            self.add_record(player2,"draw")
        self.sort_record()
        self.write_data()

    def sort_record(self):
        self.df.sort_values(by=["score"],ascending=False,inplace=True)

    def get_globalrank(self):
        output_df=self.df
        output_df.reset_index(inplace=True)
        rank=[i+1 for i in range(len(self.df))]
        output_df.insert(0,"rank",rank)
        return output_df.to_string(index=False)

    def get_record(self,player):
        if not player in self.df.index:
            return None
        return self.df[player]

    def delete_record(self,player):
        self.df.drop(index=player,inplace=True)

    def clear_database(self):
        data = {"player": ["test"],
                "win": [1],
                "lose": [0],
                "draw": [0],
                "score": [1]}
        df = pd.DataFrame(data)
        df.set_index(["player"], inplace=True)
        self.df=df
        self.write_data()



if __name__ == '__main__':
    database=Database()
    database.record_game("a","c","c")
    print(database.get_globalrank())



