from abc import ABC, abstractmethod 

class ICadastro(ABC):
    @abstractmethod
    def inserir(self):
        pass
    
    @abstractmethod
    def alterar(self):
        pass
    
    @abstractmethod
    def excluir(self):
        pass
    
    @abstractmethod
    def consultar(self, codigo):
        pass
    
    @abstractmethod
    def consultarNome(self, nome):
        pass