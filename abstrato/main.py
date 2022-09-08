from Retangulo import Retangulo
from Triangulo import Triangulo

ret = Retangulo(10,30)
print("Meu retângulo", ret)
print("Área ", ret.calcularArea())
print("Perímetro ", ret.calcularPerimetro())

tri = Triangulo(4,16)
print("Meu triângulo", tri)
print("Área ", tri.calcularArea())
print("Perímetro ", tri.calcularPerimetro())