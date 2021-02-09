# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
import time
from collections import deque
import numpy as np
import matplotlib.pyplot as plt  # $ pip install matplotlib
import matplotlib.animation as animation
from Bob import *
from GameTable import Coin
from GameTable import GameTable


class Graph:
    def data_gen(self):
        t = self.t
        cnt = 0
        while cnt < 1000:
            cnt+=1
            t += 0.05

            self.GT.Comare(self.ACoin,self.BCoin)
            y1 = self.GT.getscores_a()
            print(y1)

            y2 = self.GT.getscores_b()
            #y1 = np.sin(2*np.pi*t) * np.exp(-t/10.)
            #y2 = np.cos(2*np.pi*t) * np.exp(-t/10.)
            # adapted the data generator to yield both sin and cos

            yield t, y1, y2

    def __init__(self):
        self.t = 0
        self.GT = GameTable()
        self.ACoin = Coin()
        self.BCoin = Coin()
        print(self.t)


    # create a figure with two subplots
        self.fig, (self.ax1, self.ax2) = plt.subplots(2,1)

    # intialize two line objects (one in each axes)
        self.line1, = self.ax1.plot([], [], lw=2)

        self.line2, = self.ax2.plot([], [], lw=2, color='r')
        self.line = [self.line1, self.line2]

    # the same axes initalizations as before (just now we do it for both of them)
        for ax in [self.ax1, self.ax2]:
            ax.set_ylim(-1.1, 1.1)
            ax.set_xlim(0, 5)
            ax.grid()
            ax

        self.xdata, self.y1data, self.y2data = [], [], []
        time.sleep(5)
    def run(self,  data):
        # update the data
        t, y1, y2 = data

        self.xdata.append(t)
        self.y1data.append(y1)
        self.y2data.append(y2)

        # axis limits checking. Same as before, just for both axes
        for ax in [self.ax1, self.ax2]:
            xmin, xmax = ax.get_xlim()
            if t >= xmax:
                ax.set_xlim(xmin, 2*xmax)
                ax.figure.canvas.draw()

        # update the data of both line objects
        self.line[0].set_data(self.xdata, self.y1data)
        self.line[1].set_data(self.xdata, self.y2data)

        return self.line


def start_game(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_game('Zero or Win (c)')
    G = Graph()
    ani = animation.FuncAnimation(G.fig, G.run, G.data_gen, blit=True, interval=10,
                                  repeat=False)


    plt.show()
    #ani = animation.FuncAnimation(fig, update, data_gen)
    #plt.show()
    #GT = GameTable()
#A = Coin()
#B = Coin()

# A = Coin()
   # B = Coin()

    #GT.Comare(A,B)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
