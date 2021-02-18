import numpy
from Alice import *
from Bob import *


class Coin:
    def getSide(self):
        return numpy.random.randint(0, 2)


class GameTable:
    def __init__(self):
        self.scorea = 0
        self.scoreb = 0

    def Comare(self, a, b):
        try:
            self.aa = a.getSide()
            self.bb = b.getSide()

        except Exception:

            if isinstance(a, Alice):
                self.a_value = int(a.GetValue(), 2)
                if self.a_value <= 750:
                    self.aa = 0
                else:
                    self.aa = 1

            elif isinstance(a, Bob):
                self.a_value = a.GetValue()
                if self.a_value < 0.5:
                    self.aa = 0
                else:
                    self.aa = 1

            if isinstance(b, Alice):
                self.b_value = int(b.GetValue(), 2)
                if self.b_value <= 750:
                    self.bb = 0
                else:
                    self.bb = 1

            elif isinstance(b, Bob):
                self.b_value = b.GetValue()
                if self.b_value < 0.5:
                    self.bb = 0
                else:
                    self.bb = 1

        finally:
            if self.aa > self.bb:
                self.scorea = self.scorea + 1
                self.scoreb = self.scoreb
            elif self.aa < self.bb:
                self.scoreb = self.scoreb + 1
                self.scorea = self.scorea




    def getscores_a(self):
        return self.scorea

    def getscores_b(self):
        return self.scoreb

    def resetGame(self):
        self.scorea = 0
        self.scoreb = 0
