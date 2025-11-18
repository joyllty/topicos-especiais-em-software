from .Classe import Classe
from model.dado import Dado


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