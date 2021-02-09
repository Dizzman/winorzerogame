# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
from collections import deque

import matplotlib.pyplot as plt  # $ pip install matplotlib
import matplotlib.animation as animation
from Bob import *
from GameTable import Coin
from GameTable import GameTable

npoints = 30
x = deque([0], maxlen=npoints)
y = deque([0], maxlen=npoints)
fig, ax = plt.subplots()
[line] = ax.step(x, y)

def update(dy):
    x.append(x[-1] + 1)  # update data
    y.append(y[-1] + dy)

    line.set_xdata(x)  # update plot data
    line.set_ydata(y)

    ax.relim()  # update axes limits
    ax.autoscale_view(True, True, True)
    return line, ax


def data_gen():
    while True:
        yield 1 if random.random() < 0.5 else -1

def start_game(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_game('Zero or Win (c)')
    ani = animation.FuncAnimation(fig, update, data_gen)
    plt.show()
   # GT = GameTable()
   # A = Coin()
   # B = Coin()

    #GT.Comare(A,B)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
