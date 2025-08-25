from racas.Raca import Raca


class Anao(Raca):
    def __init__(self):
        super().__init__(movimento=6, infravisao=18, alinhamento='Ordem', peso_base=75)
    
    def habilidades(self):
        return self.habilidades['Mineradores', 'Vigoroso', 'Arma Grande', 'Inimigos']