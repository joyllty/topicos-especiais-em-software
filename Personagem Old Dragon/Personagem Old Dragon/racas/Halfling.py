from racas.Raca import Raca


class Halfling(Raca):
    def __init__(self):
        super().__init__(movimento=6, infravisao=0, alinhamento='Neutro', peso_base=35)

    def habilidades(self):
        return self.habilidades['Furtivos', 'Destemidos', 'Bons de Mira', 'Pequenos', 'Restrições']