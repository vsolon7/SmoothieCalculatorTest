from Item import *
from enum import Enum
class SIZE(Enum):
    NULL = -1
    KIDS = 9
    SMALL = 14
    MEDIUM = 18
    LARGE = 24

class Smoothie:

    def __init__(self):
        self.itemList = []
        self.size = SIZE.NULL

    def changeSize(self, newSize):
        self.size = newSize

    def getSize(self):
        return self.size

    def addItem(self, item):
        self.itemList.append(item)

    def getItemList(self):
        return self.itemList
