from Game import GameState

class GameObservable:
    ObserverInterface: str

    def add(self, observer: ObserverInterface):
        pass
    def addPlayer(self, playerIdx: int,observer: ObserverInterface):
        pass
    def remove(self, observer: ObserverInterface):
        pass
    def notifyAll(self, message: GameState):
        pass


class GameObserver:
    def notify(self, message: str):
        return message
