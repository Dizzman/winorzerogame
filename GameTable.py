import numpy
class Coin:
    def getSide(self):
        return numpy.random.randint(0,20)


class GameTable:
    def __init__(self):
        self.scorea=0
        self.scoreb=0


    def Comare(self,a:Coin,b:Coin):
        if a.getSide()>b.getSide():
            self.scorea=self.scorea+0.01
        elif a.getSide()<b.getSide():
            self.scoreb=self.scoreb+0.01
        else:
            self.scorea = self.scorea - 0.01
            self.scoreb = self.scoreb - 0.01

    def getscores_a(self):
        return  self.scorea

    def getscores_b(self):
        return  self.scoreb

    def resetGame(self):
        self.scorea = 0
        self.scoreb = 0