from .Classe import Classe
from Dado import Dado


class Clerigo(Classe):
    def __init__(self):
        super().__init__(vida=8, ataque=1, protecao=5)
        self.dado = Dado(8)
        self.habilidades_classe = ['Magias Divinas', 'Afastar Mortos-Vivos', 'Cura Milagrosa']
        self.magias_divinas = {1: 1, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}

    def subir_de_nivel(self):
        # sem implementação do aumento de proteção e ataque
        self.vida += self.dado.rolar()
        self.nivel += 1
        # ===== MAGIAS DIVINAS =====
        if self.nivel == 3:
            self.magias_divinas[1] = 2
            self.magias_divinas[2] = 1
        elif self.nivel == 4:
            self.magias_divinas[2] = 2
        elif self.nivel == 5:
            self.magias_divinas[3] = 1
        elif self.nivel == 6:
            self.magias_divinas[1] = 3
        elif self.nivel == 7:
            self.magias_divinas[3] = 2
            self.magias_divinas[4] = 1
        elif self.nivel == 8:
            self.magias_divinas[2] = 3
        elif self.nivel == 9:
            self.magias_divinas[4] = 2
            self.magias_divinas[5] = 1
        elif self.nivel == 10:
            self.magias_divinas[1] = 4
            self.magias_divinas[3] = 3
    

    def exibir_habilidades_classe(self):
        print('\n=================== HABILIDADES DE CLASSE ===================')
        print('>> Armas: só podem usar armas impactantes. Usar armas \ncortantes ou perfurantes faz o Clérigo perder suas magias até \nrealizar uma penitência para restaurar o abalo na sua fé.')
        print('>> Armaduras: podem usar todas as armaduras.')
        print('>> Itens Mágicos: o Clérigo é capaz de usar todos os tipos de\nitens mágicos desde que sejam ordeiros.')
        print(f'\n---------- Habilidades ---------')
        for h in self.habilidades_classe:
            print(f'>> {h}')
        print('=============================================================\n')
