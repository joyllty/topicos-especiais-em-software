from racas.Raca import Raca


class Humano(Raca):
    def __init__(self):
        super().__init__(movimento=9, infravisao=0, alinhamento='Qualquer', peso_base=80)

    def habilidades(self):
        return self.habilidades['Aprendizado', 'Adaptabilidade']
    