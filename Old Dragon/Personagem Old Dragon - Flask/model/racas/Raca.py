from abc import ABC

class Raca(ABC):
    def __init__(self, movimento, infravisao, alinhamento, peso_base):
        self.movimento = movimento
        self.infravisao = infravisao
        self.alinhamento = alinhamento
        self.peso_base = peso_base
        self.habilidades = []

    def exibir_habilidades_raca(self):
        return self.habilidades
