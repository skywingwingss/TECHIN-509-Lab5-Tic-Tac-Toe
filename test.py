import unittest
import logic
import Board
from Gameandplayer import Human


class TestLogic(unittest.TestCase):

    def __init__(self,MethodName):
        super(TestLogic,self).__init__(MethodName)
        self.test_board=Board.Board()
        self.test_board.set(0,0,"X")
        self.test_board.set(1,1,"X")
        self.test_board.set(2,2,"X")
        self.test_board.set(0,2,"O")
        self.test_board.set(2,1,"O")

    def test_check_winner(self):
        self.assertEqual(logic.check_winner(self.test_board), 'X')

    def test_transferInput(self):
        input="2,3"
        self.assertEqual(logic.transferInput(input),(1,2))
    def test_checkInput(self):
        self.assertEqual(logic.checkInput(1,4,self.test_board),(-1,-1))

    def test_getInput(self):
        input="2,3"
        self.assertEqual(logic.getInput(input),(1,2))
    # TODO: Test all functions from logic.py!

    def test_board_movable(self):
        self.assertEqual(logic.board_movable(1,1,self.test_board),False)

    def test_roundadd(self):
        self.assertEqual(logic.roundadd(2,1,2),1)


if __name__ == '__main__':
    unittest.main()