# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from Gameandplayer import Tictactoe
from Gameandplayer import Human
from Gameandplayer import AI



if __name__ == '__main__':



    print("Welcome! Please select player number.\nEnter 1 to play with an AI.\nEnter 2 to play with a human.")
    playerNum=int(input("Enter:"))
    if playerNum==1:
        playerX = Human("X")
        playerO = AI("O")
    elif playerNum==2:
        playerX = Human("X")
        playerO=Human("O")
    else:
        print("Error input! Exit...")
        exit(0)
    Game=Tictactoe(playerX,playerO)
    Game.run()

    # while Game.get_winner() == None:
    #     print("TODO: take a turn!")
    #     # TODO: Show the board to the user.
    #     print(Tictactoe.getprintBoard())
    #     # TODO: Input a move from the player.
    #     instream = input("Player{} please choose a position in format x,y to place chess:".format(player))
    #     x,y=Game.getInput(instream)
    #     if (x, y) == (-1, -1):
    #         print("Wrong input, please input coordinate in format x,y!")
    #         continue
    #     # TODO: Update the board.
    #     Game.moveChess(x,y)
    #     # TODO: Update who's turn it is.
    #     player=other_player(player)
    #     Turn+=1
    #     if Turn==9:
    #         break
    # print(getprintBoard(board))
    # if winner==None:
    #     print("Draw!")
    # else:
    #     player = other_player(player)
    #     print("Player{} win the game!".format(player))