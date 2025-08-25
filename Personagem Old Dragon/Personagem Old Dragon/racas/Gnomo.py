from racas.Raca import Raca


class Gnomo(Raca):
    def __init__(self):
        super().__init__(movimento=6, infravisao=18, alinhamento='Neutro', peso_base=40)

    def habilidades(self):
        return self.habilidades['Avaliadores', 'Sagazes e Vigorosos', 'Restrições']