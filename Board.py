class Board():
    def __init__(self):
        self.board=[
            [" "," "," "],
            [" "," "," "],
            [" "," "," "]
        ]

    def __str__(self):
        s="----------\n"
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                s+="|"+self.board[i][j]
            s+="|\n"
        s+="----------\n"
        return s

    def set(self,x,y,value):
        self.board[y][x]=value

    def get(self,x,y):
        return self.board[y][x]

    def get_wholeboard(self):
        return self.board
