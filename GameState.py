from typing import List, Mapping, Set, Optional
from dataclasses import dataclass
from Position import SleepingQueenPosition, AwokenQueenPosition, HandPosition
import Card
from Card import Queen

@dataclass
class GameState:
    numberOfPlayers: int
    onTurn: int
    sleepingQueens: Set[SleepingQueenPosition]
    cards: Mapping[HandPosition, Optional[Card]]
    awokenQueens: Mapping[AwokenQueenPosition, Queen]
    cardsDiscardedLastTurn: List[Card]

@dataclass
class PlayerState:
    cards: Mapping[int, Optional[Card]]
    awokenQueens: Mapping[int, Queen]
