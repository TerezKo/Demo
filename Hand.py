import Player, Card
from typing import List, Optional, Mapping
from Card import CardType
import DrawingAndTrashPile
from Position import HandPosition

class Hand(DrawingAndTrashPile):
    playerIdx: int

    def pickCards(self, positions: List[HandPosition]) -> Optional[List[Card]]:
        pass

    def removePickedCardsAndRedraw(self):
        Mapping[HandPosition, Card]

    def returnPicekdCards(self):
        return

    def hasCardOfType(self, type: CardType):
        return HandPosition

    def getCards(self):
        return List[Card]

