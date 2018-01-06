from enum import Enum
import csv

class TYPE(Enum):
    NULL = -1
    FRUIT = 0
    JUICE = 1
    ADD_IN = 2

class Item:
    def __init__(self):
        self._type = TYPE.ERROR
        self._name = 'NULL'
        #calories, sugar, and blank because i dunno what else yet
        self._nutritionInfo = [0.0, 0.0, 0.0, 0.0 ,0.0]
        self._density = None

    def getName(self):
        return self._name

    def getType(self):
        return self._type

    def getNutInfo(self):
        return self._nutritionInfo

    def getDensity(self):
        return self._density

    def readNutData(self, name):
        self.tempnut = []
        with open('Nutrition Data/data.csv') as csvFile:
            readCsv = csv.reader(csvFile, delimiter = ',')
            for row in readCsv:
                if row[0] == name:
                    self.tempnut.append(float(row[1]))
                    self.tempnut.append(float(row[2]))

        return self.tempnut

#Specific items that inherit from a generic item class
class Banana(Item):
    def __init__(self):
        self._type = TYPE.FRUIT
        self._name = 'Banana'
        self._density = 0.95
        self._nutritionInfo = self.readNutData(self._name)

class Strawberry(Item):
    def __init__(self):
        self._type = TYPE.FRUIT
        self._name = 'Strawberry'
        self._density = 0.93
        self._nutritionInfo = self.readNutData(self._name)

class AppleJuice(Item):
    def __init__(self):
        self._type = TYPE.JUICE
        self._name = 'Apple Juice'
        self._density = 1.04
        self._nutritionInfo = self.readNutData(self._name)