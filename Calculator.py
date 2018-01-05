from Smoothie import *
from Item import *

class Calculator:
    def run(self):
        s = Smoothie()
        s.changeSize(SIZE.LARGE)

        s.addItem(Banana)
        s.addItem(AppleJuice)
        s.addItem(Strawberry)

        s.printInfo()