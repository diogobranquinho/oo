from abc import ABC, abstractmethod 

class Forma(ABC):
    def __init__(self, base, altura): 
        self.__base = base 
        self.__altura = altura

    def getAltura(self): 
        return self.__altura
    
    def setAltura(self, altura):
        self.__altura = altura
    
    def getBase(self):
        return self.__base

    def setBase(self, base): 
        self.__base = base

    @abstractmethod
    def calcularArea(self):
        pass

    @abstractmethod
    def calcularPerimetro(self):
        pass
    
    def __str__(self):
        return "Altura: " + str(self.__altura) + " Base: " + str(self.__base)