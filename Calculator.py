from Smoothie import *
from Item import *

class Calculator:

    # conversion from ounces to milliliters
    OZ2ML = 29.57

    def __init__(self):
        self.smoothieList = []
        # the ratio of frozen fruit to total smoothie volume in an ideal smoothie
        # the ideal smoothie is made up of 5/9ths fruit, 4/9ths juice (discovered through testing)
        # can change if someone wants a thicker smoothie
        self.fruitVR = (5 / 9)
        self.juiceVR = (1 - self.fruitVR)

    def run(self):
        s = Smoothie()
        s2 = Smoothie()

        self.smoothieList.append(s)
        self.smoothieList.append(s2)

        s.changeSize(SIZE.MEDIUM)
        s2.changeSize(SIZE.LARGE)

        s2.addItem(Strawberry())
        s2.addItem(AppleJuice())

        s.addItem(Banana())
        s.addItem(AppleJuice())
        s.addItem(Strawberry())

        self.totalCals = 0
        self.totalSug = 0
        for smoothie in self.smoothieList:
            self.smoothieNut = self.printInfo(smoothie)
            self.totalCals += self.smoothieNut[0]
            self.totalSug += self.smoothieNut[1]

            print('==================================')

        print('Total kCal: ', self.totalCals, 'kCal, Total Sugar: ', self.totalSug, 'g', sep='')



    # this is a complicated smoothie calculation based on the composition of the smoothie
    # it takes the ratio of fruit/juice to total smoothie, uses that to get the volume of fruit/juice,
    # then multiplies that by the density of fruit/juice. Using nutrition data it then calculates the nutritional information
    # of the smoothie based on the info of the parts that make it up.
    def printInfo(self, smoothie):
        self.totalCal = 0
        self.totalSugar = 0

        self.fruitNumber = 0
        self.juiceNumber = 0
        # finds the number of fruits and juices in the smoothie
        for item in smoothie.getItemList():
            self.theType = item.getType()
            if self.theType == TYPE.FRUIT:
                self.fruitNumber += 1
            elif self.theType == TYPE.JUICE:
                self.juiceNumber += 1

        # this is the amount of volume each type of fruit/juice takes up.
        # if there are 4 fruits/juices then each one only takes up a fourth of the volume ratio
        self.adjustedFVR = self.fruitVR / self.fruitNumber
        self.adjustedJVR = self.juiceVR / self.juiceNumber

        # the milliliters of fruit in a smoothie
        sSize = smoothie.getSize()
        self.fruitML = (sSize.value * self.OZ2ML) * self.adjustedFVR
        self.juiceML = (sSize.value * self.OZ2ML) * self.adjustedJVR

        # basically looping through all the items in the item list
        # then calculating the nutrition data using the fruits weight in grams out of 100
        # (the nutrition data in the .csv is based on 100g)
        for item in smoothie.getItemList():
            self.tempNut = item.getNutInfo()
            self.tempDensity = item.getDensity()

            if item.getType() == TYPE.FRUIT:
                self.weightR = (self.tempDensity * self.fruitML) / 100
            elif item.getType() == TYPE.JUICE:
                self.weightR = (self.tempDensity * self.juiceML) / 100

            print(item.getName(), ': ', (self.tempNut[0] * self.weightR), ' kCal, ',
                  (self.tempNut[1] * self.weightR), 'g of sugar', sep='')

            self.totalCal += (self.tempNut[0] * self.weightR)
            self.totalSugar += (self.tempNut[1] * self.weightR)

        print('Total kCal: ', self.totalCal, ', Total Sugar: ', self.totalSugar, 'g', sep='')

        return [self.totalCal, self.totalSugar]