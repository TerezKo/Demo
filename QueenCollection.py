from Game import Position, SleepingQueenPosition
from Card import Queen
from typing import List, Tuple, Mapping, Optional


class QueenCollection:
    def addQueen(self, queen: Queen):
        pass

    def removeQueen(self, position: SleepingQueenPosition) -> Optional[Queen]:
        pass

    def getQueens(self):
        return Mapping[Position, Queen]


class AwokenQueens(QueenCollection):
    Awoken_queens = []


class SleepingQueens(QueenCollection):
    Sleeping_queens = []
    for i in range(4):
        Sleeping_queens.append(Queen("Queen", 5))
    for i in range(4):
        Sleeping_queens.append(Queen("Queen", 10))
    for i in range(3):
        Sleeping_queens.append(Queen("Queen", 15))
    Queen("Queen", 20)


class MoveQueen:
    def play(self, targetQueen: Position):
        return bool
