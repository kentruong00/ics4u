from math import pi
'''
Create a circle class
    Attributes: radius, diameter
    Methods: getRadius, getDiameter, getCircumfrence, getArea    
'''

class Circle:
    def __init(self):
        self.__radius = self.setRadius
        self.__diameter = self.__radius * 2
        self.__circumfrence = self.setCircumfrence
        self.__area = self.setArea

    def __str__(self):
        return f'Cicle with a radius of {self.__radius}'
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def setRadius(self):
        userInput = ''
        while not userInput or not(userInput.isdigits()):
            userInput = input('Enter Radius:')
        self.__radius = float(userInput)

    def setCircumfrence(self):
        return pi * self.__diameter
    
    def setArea(self):
        return pi * self.__radius**2
    
    def getRadius(self):
        return self.__radius
    
    def getCircumfrence(self):
        return self.__circumfrence
    
    def getDiameter(self):
        return self.__diameter
    
    def getArea(self):
        return self.__area