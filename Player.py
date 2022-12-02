import AwokenQueens
import Hand
import Game
from GameState import PlayerState
from Position import Position, SleepingQueenPosition
from Card import Queen
from typing import List, Tuple, Optional


class Player(Game):
    def play(self, cards: List[Position]):
        pass
    def getPlayerState(self):
        return PlayerState
