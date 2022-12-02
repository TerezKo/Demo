from dataclasses import dataclass

class CardType:
    listOfCards = ["Number", "King","Knight", "SleepingPotion", "Dragon", "MagicWand"]

@dataclass
class Card:
    type: CardType
    value: int

@dataclass
class Queen:
    def getPoints(self):
        numberOfPoints: int
