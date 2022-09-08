from ICadastro import ICadastro

class Aluno(ICadastro):
    
    def inserir(self):
        print("Inserindo dados do aluno")

    def alterar(self):
        print("Alterar dados do aluno")

    def excluir(self):
        print("Excluir dados do aluno")

    def consultar(self):
        print("Os dados do aluno são")

    def consultarNome(self, nome):
        print("Meu nome é...")