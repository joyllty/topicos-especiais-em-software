from racas.Raca import Raca


class MeioElfo(Raca):
    def __init__(self):
        super().__init__(movimento=9, infravisao=9, alinhamento='Caos', peso_base=65)

    def habilidades(self):
        return self.habilidades['Aprendizado', 'Gracioso e Vigoroso', 'Idioma Extra', 'Imunidades']
    