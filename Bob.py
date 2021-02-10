# Боб не знает, что такое дискретное пространство.
# Он действует в пространстве вещественных чисел от 0 до 1.
import random


class Bob:
    "This is a person class"

    @staticmethod
    def GetValue():
        return random.random()

# x = Bob()
# print(x.GetValue())
