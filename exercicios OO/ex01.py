'''
1. Classe Básica: Crie uma classe Pessoa com atributos nome e idade. Adicione um construtor para
inicializar esses valores e um método para exibir as informações da pessoa
'''

class Pessoa():

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def exibir_info(self):
        print(f'>> Nome: {self.nome}')
        print(f'>> Idade: {self.idade}')


# python sempre define o nome do arquivo que eu vou executar como "__main__"
if __name__ == '__main__':
    pessoa = Pessoa('Bruna', 19)
    pessoa.exibir_info()
