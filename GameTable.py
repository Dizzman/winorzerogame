import numpy
class Coin:
    def getSide(self):
        return numpy.random.randint(0,200)


class GameTable:
    def __init__(self):
        self.scorea=0
        self.scoreb=0


    def Comare(self,a:Coin,b:Coin):
        aa=a.getSide()
        bb=b.getSide()
        if aa>bb:
            self.scorea=self.scorea+0.01
            self.scoreb = self.scoreb - 0.015
        elif aa<bb:
            self.scoreb=self.scoreb+0.01
            self.scorea = self.scorea - 0.015
        else:

            self.scorea = self.scorea + 0.415
            self.scoreb = self.scoreb + 0.415

    def getscores_a(self):
        return  self.scorea

    def getscores_b(self):
        return  self.scoreb

    def resetGame(self):
        self.scorea = 0
        self.scoreb = 0