import numpy


class Coin:
    def getSide(self):
        return numpy.random.randint(0, 2)


class GameTable:
    def __init__(self):
        self.scorea = 0
        self.scoreb = 0

    def Comare(self, a: Coin, b: Coin):
        self.aa = a.getSide()
        self.bb = b.getSide()
        if self.aa > self.bb:
            self.scorea = self.scorea + 0.01
            self.scoreb = self.scoreb - 0.015
        elif self.aa < self.bb:
            self.scoreb = self.scoreb + 0.01
            self.scorea = self.scorea - 0.015
        else:
            self.scorea = self.scorea + 0.415
            self.scoreb = self.scoreb + 0.415

    def getscores_a(self):
        return self.scorea

    def getscores_b(self):
        return self.scoreb

    def resetGame(self):
        self.scorea = 0
        self.scoreb = 0
