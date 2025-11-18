from .Classe import Classe
from model.dado import Dado


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
    
        