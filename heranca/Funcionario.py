class Funcionario: 
    #construtor
    def __init__(self, nome, email, telefone, valorHora): 
        self.__nome = nome
        self.__email = email
        self.__telefone = telefone
        self.__valorHora = valorHora
        
        #métodos para acessar os valores 
    def getNome(self):
        return self.__nome
    def getEmail(self): 
        return self.__email
    def getTelefone(self): 
        return self.__telefone
    def getvalorHora(self): 
        return self.__valorHora

    #métodos para setar os valores 
    def setNome(self, nome):
        self.__nome = nome
    def setEmail(self, email): 
        self.__email = email
    def setTelefone(self, telefone): 
        self.__telefone = telefone
    def setvalorHora(self, valorHora): 
        self.__valorHora = valorHora

    #método para apresentar o objeto 
    def __str__(self):
        return self.__nome + ' ' + self.__email + ' ' + self.__telefone + ' ' + str(self.__valorHora) #outros métodos
    def calculasalario(self, horas): 
        return self.__valorHora * horas