from Forma import Forma

class Triangulo(Forma):
    
    def calcularArea(self):
        return (super().getBase() * super().getAltura()) / 2

    def calcularPerimetro(self):
        return super().getAltura() * 3