from .Classe import Classe
from Dado import Dado


class Ladrao(Classe):
    def __init__(self):
        super().__init__(vida=6, ataque=1, protecao=5)
        self.dado = Dado(6)
        self.habilidades_classe = ['Ataque Furtivo', 'Ouvir Ruídos', 'Talentos de Ladrão']

    def subir_de_nivel(self):
        # sem implementação do aumento de proteção e ataque
        self.vida += self.dado.rolar()
        self.nivel += 1

    def exibir_habilidades_classe(self):
        print('\n=================== HABILIDADES DE CLASSE ===================')
        print('>> Armas: apenas pequenas ou médias. Armas grandes geram \nataques difíceis para Ladrões. ')
        print('>> Armaduras: apenas as leves. Escudos, Armaduras Média ou \nPesadas, impedem o uso das suas habilidades e protegem apenas \na metade da CA normal. ')
        print('>> Itens Mágicos: não podem usar cajados, varinhas e \npergaminhos mágicos com exceção dos pergaminhos de proteção.')
        print(f'\n---------- Habilidades ---------')
        for h in self.habilidades_classe:
            print(f'>> {h}')
        print('=============================================================\n')
