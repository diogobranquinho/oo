from Funcionario import Funcionario

class Gerente(Funcionario): 
    #construtor
    def __init__(self, nome, email, telefone, valorHora, valorhoraExtra): 
        super().__init__(nome, email, telefone, valorHora) 
        self.__valorhoraExtra = valorhoraExtra

    #métodos para acessar os valores
    def getvalorhoraExtra(self): 
        return self.__valorhoraExtra

    #métodos para setar os valores
    def setvalorhoraExtra(self, valorhoraExtra): 
        self.__valorhoraExtra = valorhoraExtra

    #método para apresentar o objeto 
    def __str__(self):
        return super().getNome() + ' ' + str(self.__valorhoraExtra)