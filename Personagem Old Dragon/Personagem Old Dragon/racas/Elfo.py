from racas.Raca import Raca


class Elfo(Raca):
    def __init__(self):
        super().__init__(movimento=9, infravisao=18, alinhamento='Neutro', peso_base=60)

    def habilidades(self):
        return self.habilidades['Percepção Natural', 'Graciosos', 'Arma Racial', 'Imunidades']