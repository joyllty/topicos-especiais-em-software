from abc import ABC, abstractmethod


class Classe(ABC):
    def __init__(self, vida, ataque, protecao):
        self.vida = vida
        self.ataque = ataque
        self.protecao = protecao
        self.habilidades_classe = []
        self.nivel = 1
    
    @abstractmethod
    def subir_de_nivel(self):
        pass
    
    @abstractmethod
    def exibir_habilidades_classe():
        pass

