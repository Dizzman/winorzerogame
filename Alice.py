# Алиса действует в двоичной системе счисления и может называть числа от 0b111110101  до 0b1111101000
# (от 501 до 1000)
import random

class Alice:
    "This is a person class"

    @staticmethod
    def GetValue():
        return bin(random.randint(501, 1000))


# x = Alice()
# h = x.GetValue()
# print(h)
# print(0 if int(h, 2) <= 750 else 1)

