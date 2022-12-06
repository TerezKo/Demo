from Game import PlayerState
from Game import Position
from typing import List, Optional, Mapping
import Card
from Game import HandPosition


class Player:
    def play(self, cards: List[Position]):
        pass
    def getPlayerState(self):
        return PlayerState


class Hand:
    def __init__(self, cards, idX):
        self.card: List[Card] = cards
        self.playerIdx = idX
        self.drawing_and_trash_pile: bool

    def pickCards(self, positions: List[HandPosition]) -> Optional[List[Card]]:
        pass

    def removePickedCardsAndRedraw(self):
        Mapping[HandPosition, Card]

    def returnPicekdCards(self):
        return

    def hasCardOfType(self, card):
        return card.Card.type

    def getCards(self):
        return List[Card]
