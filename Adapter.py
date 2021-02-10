# Адаптеры для Алисы и Боба
import numpy
from GameTable import Coin
from Alice import *
from Bob import *


class AliceAdapter(Coin):
    def __init__(self, A: Alice):
        self.A = A

    def getSide(self):
        self.v = int(self.A.GetValue(), 2)

        if self.v <= 750:
            return 0
        else:
            return 1


class BobAdapter(Coin):
    def __init__(self, B: Bob):
        self.B = B

    def getSide(self):
        self.v = self.B.GetValue()

        if self.v < 0.5:
            return 0
        else:
            return 1