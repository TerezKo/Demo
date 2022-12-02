from Position import Position, SleepingQueenPosition
from Card import Queen
from typing import List, Tuple, Mapping, Optional

class QueenCollection:
    def addQueen(self, queen: Queen):
        ...
    def removeQueen(self, position: SleepingQueenPosition) -> Optional[Queen]:
        pass
    def getQueens(self):
        return Mapping[Position, Queen]
