from .Guerreiro import Guerreiro


class Barbaro(Guerreiro):
    def __init__(self):
        super().__init__()
        self.habilidades_classe.extend([
            'Vigor Bárbaro', 
            'Talentos Selvagens', 
            'Surpresa Selvagem', 
            'Força do Totem'
        ])