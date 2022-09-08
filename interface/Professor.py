from ICadastro import ICadastro

class Professor(ICadastro):
    
    def inserir(self):
        print("Inserindo dados do professor")

    def alterar(self):
        print("Alterar dados do professor")

    def excluir(self):
        print("Excluir dados do professor")

    def consultar(self):
        print("Os dados do professor são")

    def consultarNome(self, nome):
        print("Meu nome é...")