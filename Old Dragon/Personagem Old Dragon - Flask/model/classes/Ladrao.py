from .Classe import Classe
from model.dado import Dado


class Ladrao(Classe):
    def __init__(self):
        super().__init__(vida=6, ataque=1, protecao=5)
        self.dado = Dado(6)
        self.habilidades_classe = ['Ataque Furtivo', 'Ouvir Ruídos', 'Talentos de Ladrão']

    def subir_de_nivel(self):
        # sem implementação do aumento de proteção e ataque
        self.vida += self.dado.rolar()
        self.nivel += 1

