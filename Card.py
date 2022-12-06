from dataclasses import dataclass
from typing import List
from QueenCollection import SleepingQueens


# @dataclass
# class CardType:
#     name: str
    # listOfCards = ["Number", "King", "Knight", "SleepingPotion", "Dragon", "MagicWand", "Queen"]

@dataclass(frozen=True)
class Queen:
    name: str
    getPoints: int

@dataclass(frozen=True)
class Card:
    type: str
    value: int


class DrawingAndTrashPile:
    def __init__(self):
        self.draw = None
        self.trash = None
        self.draw: List[Card]
        self.trash: List[Card]
        for i in range(12):
            if i < 10:
                for j in range(4):
                    self.draw.append(Card("Number", i))
            if i < 8:
                self.draw.append(Card("King", 0))
            if i < 4:
                self.draw.append(Card("Knight", 0))
                self.draw.append(Card("SleepingPotion", 0))
            if i < 3:
                self.draw.append(Card("Dragon", 0))
                self.draw.append(Card("MagicWand", 0))

    def discardAndDraw(self, discard: List[Card]):
        for i in discard:
            self.draw.pop(i)
            self.trash.append(i)
        return discard

    def newTurn(self):
        pass
    getCardsDiscardedThisTurn: List[Card]

#listOfCards = ["Number", "King", "Knight", "SleepingPotion", "Dragon", "MagicWand", "Queen"]



# GAME_CARD_TYPE_QUEEN1: Queen = Queen("Queen1", 5)
# GAME_CARD_TYPE_QUEEN2: Queen = Queen("Queen2", 5)
# GAME_CARD_TYPE_QUEEN3: Queen = Queen("Queen3", 5)
# GAME_CARD_TYPE_QUEEN4: Queen = Queen("Queen4", 5)
# GAME_CARD_TYPE_QUEEN5: Queen = Queen("Queen5", 10)
# GAME_CARD_TYPE_QUEEN6: Queen = Queen("Queen6", 10)
# GAME_CARD_TYPE_QUEEN7: Queen = Queen("Queen7", 10)
# GAME_CARD_TYPE_QUEEN8: Queen = Queen("Queen8", 10)
# GAME_CARD_TYPE_QUEEN9: Queen = Queen("Queen9", 15)
# GAME_CARD_TYPE_QUEEN10: Queen = Queen("Queen10", 15)
# GAME_CARD_TYPE_QUEEN11: Queen = Queen("Queen11", 15)
# GAME_CARD_TYPE_QUEEN12: Queen = Queen("Queen12", 20)
#
# GAME_CARD_TYPE_KING1: Card = Card("King", 10)
# GAME_CARD_TYPE_KNIGHT: Card = Card("Knight", 10)
# GAME_CARD_TYPE_SLEEPING_POTION: Card = Card("SleepingPotion", 10)
# GAME_CARD_TYPE_DRAGON: Card = Card("Dragon", 10)
# GAME_CARD_TYPE_MAGICWAND: Card = Card("MagicWand", 10)
# GAME_CARD_TYPE_NUMBER: Card = Card("Number", 10)

