from Forma import Forma

class Retangulo(Forma):
    
    def calcularArea(self):
        return super().getAltura() * super().getBase() 

    def calcularPerimetro(self):
        return (super().getBase()*2) + (super().getAltura()*2)