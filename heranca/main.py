from funcionario import Funcionario
from Gerente import Gerente

obj1 = Funcionario('Ana',  'anapaula@teste.com', '189965656', 40.6)
print(obj1.getNome())
obj1.setNome('Paula')
print(obj1.getNome())
print(obj1)
print(obj1.calculasalario(40))
obj2 = Gerente('Jose',  'Jose@teste.com', '18998898', 50.6, 10)
print(obj2.getNome())
obj2.setNome('Paulo')
print(obj2.getNome())
print(obj2)
print(obj2.calculasalario(40))