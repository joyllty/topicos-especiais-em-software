from .Ladrao import Ladrao


class Bardo(Ladrao):
    def __init__(self):
        super().__init__()
        self.habilidades_classe.extend([
            'Influenciar', 
            'Inspirar', 
            'Fascinar', 
            'Usar Pergaminhos'
        ])
