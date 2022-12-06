from typing import List, Mapping, Set, Optional
import Card
from Card import Queen
from dataclasses import dataclass
from typing import Union
import random
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




class Game:
    def play(self, playerIdx: int, cards: List[Position]) -> Optional[GameState]:
        Cards = random.shuffle(Card.draw)
        pass



class GameFinishedStrategy:
    def isFinished(self) -> Optional[int]:
        pass

class GameFinished:
    if GameState.numberOfPlayers == 2 or GameState.numberOfPlayers == 3:
        name = 'winner'
        print("GAME OVER")
        print(f'Winner is {name}')
    elif GameState.numberOfPlayers == 4 or GameState.numberOfPlayers == 5:
        name = 'winner'
        print("GAME OVER")
        print(f'Winner is {name}')
    elif len(GameState.sleepingQueens) == 0:
        name = 'winner'
        print("GAME OVER")
        print(f'Winner is {name}')
