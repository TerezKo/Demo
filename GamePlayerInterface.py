import Player, QueenCollection

class GamePlayerInterface:
    def play(self, player: str, cards: str):
        return f'h{Player.CardType} a{len(QueenCollection.getQueens()+1)}'

