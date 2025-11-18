from .Classe import Classe
from Dado import Dado


class Guerreiro(Classe):
    def __init__(self):
        super().__init__(vida=10, ataque=1, protecao=5)
        self.dado = Dado(10)
        self.habilidades_classe = ['Aparar', 'Maestria em Arma', 'Ataque Extra']

    def subir_de_nivel(self):
        # sem implementação do aumento de proteção
        self.vida += self.dado.rolar()
        self.ataque += 1
        self.nivel += 1

    def exibir_habilidades_classe(self):
        print('\n=================== HABILIDADES DE CLASSE ===================')
        print('>> Armas: pode usar todas as armas.')
        print('>> Armaduras: pode usar todas as armaduras.')
        print('>> Itens Mágicos: não pode usar cajados, varinhas e \npergaminhos mágicos com exceção dos pergaminhos de proteção')
        print(f'\n---------- Habilidades ---------')
        for h in self.habilidades_classe:
            print(f'>> {h}')
        print('=============================================================\n')
