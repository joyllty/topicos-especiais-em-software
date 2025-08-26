from .Classe import Classe
from Dado import Dado


class Mago(Classe):
    def __init__(self):
        super().__init__(vida=4, ataque=0, protecao=5)
        self.dado = Dado(4)
        self.habilidades_classe = ['Magias Arcanas', 'Ler Magias', 'Detectar Magias']
        self.magias_arcanas = {1: 1, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}

    def subir_de_nivel(self):
        # sem implementação do aumento de proteção e ataque
        self.vida += self.dado.rolar()
        self.nivel += 1
        # ===== MAGIAS Arcanas =====
        if self.nivel == 2:
            self.magias_arcanas[1] = 2
        elif self.nivel == 3:
            self.magias_arcanas[2] = 1
        elif self.nivel == 4:
            self.magias_arcanas[2] = 2
        elif self.nivel == 5:
            self.magias_arcanas[3] = 1
        elif self.nivel == 6:
            self.magias_arcanas[1] = 3
            self.magias_arcanas[3] = 2
        elif self.nivel == 7:
            self.magias_arcanas[4] = 1
        elif self.nivel == 8:
            self.magias_arcanas[2] = 3
            self.magias_arcanas[4] = 2
        elif self.nivel == 9:
            self.magias_arcanas[5] = 1
        elif self.nivel == 10:
            self.magias_arcanas[3] = 3
            self.magias_arcanas[5] = 2


    def exibir_habilidades_classe(self):
        print('\n=================== HABILIDADES DE CLASSE ===================')
        print('>> Armas: apenas pequenas. Armas grandes ou médias geram \nataques difíceis para Magos.')
        print('>> Armaduras: nenhuma. Usar escudos ou armaduras impede a \nconjuração de magias e protegem apenas metade da CA normal. ')
        print('>> Itens Mágicos: podem usar todos os tipos.')
        print(f'\n---------- Habilidades ---------')
        for h in self.habilidades_classe:
            print(f'>> {h}')
        print('=============================================================\n')