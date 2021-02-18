import time
from collections import deque
import numpy as np
import matplotlib.pyplot as plt  # $ pip install matplotlib
import matplotlib.animation as animation
from Bob import *
from Alice import *
from Adapter import *
from GameTable import Coin
from GameTable import GameTable
#from GameTable_without_Adapter import GameTable
from sys import stdout


class Game:
    def __init__(self, ACoin: Coin, BCoin: Coin):
        self.GT = GameTable()
        self.ACoin = ACoin
        self.BCoin = BCoin

    def start_game(self):
        # time.sleep(5)

        while True:
            # not ((self.GT.getscores_a() < 2*self.GT.getscores_b()) or (self.GT.getscores_b() < 2*self.GT.getscores_a())):
            self.GT.Comare(self.ACoin, self.BCoin)
            print('Gamer A: {} Gamer B: {}'.format(self.GT.getscores_a(), self.GT.getscores_b()))
            # a =0 b = 0
            # a =1 b =0


            if (self.GT.getscores_a() - self.GT.getscores_b() >= 2) or (
                    self.GT.getscores_b() - self.GT.getscores_a() >= 2):
                print('Winner is {}'.format('Gamer A' if self.GT.getscores_a() > self.GT.getscores_b() else 'Gamer B'))
                break

        print()

# for game with adapter
if __name__ == '__main__':
    print('Lose or Win (c)')
    A = Alice()
    B = Bob()
    alice = AliceAdapter(A)
    bob = BobAdapter(B)
    G = Game(alice, bob)
    G.GT.resetGame()
    G.start_game()

# for game without adapter
if __name__ == '__main__':
    print('Lose or Win (c)')
    A = Alice()
    B = Bob()
    G = Game(A, B)
    G.GT.resetGame()
    G.start_game()
