from typing import List, Tuple, Optional
from dataclasses import dataclass
from typing import Union
#variant??

@dataclass
class SleepingQueenPosition:
    def getCardIndex(self):
        return int

@dataclass
class AwokenQueenPosition:
    def getCardIndex(self):
        return int
    def getPlayerIndex(self):
        return int

@dataclass
class HandPosition:
    def getCardIndex(self):
        return int
    def getPlayerIndex(self):
        return int

@dataclass
class Position:
    variant: {Union[SleepingQueenPosition,AwokenQueenPosition, HandPosition]}
