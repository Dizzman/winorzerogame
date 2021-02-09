import numpy
class Coin:
    def GetSide(self):
        return numpy.random.randint(0,2)


class GameTable:
    def __init__(self):
        self.scorea=0
        self.scoreb=0

    @classmethod
    def Comare(self,a:Coin,b:Coin):
        if a.getSide()>b.getSide():
            self.scorea=self.scorea+1
        elif a.getSide()<b.getSide():
            self.scoreb=self.scoreb+1
        else:
            self.scoreb = self.scoreb + 100
            self.scoreb = self.scoreb + 100

    def getscores_a(self):
        return  self.scorea

    def getscores_b(self):
        return  self.scoreb
