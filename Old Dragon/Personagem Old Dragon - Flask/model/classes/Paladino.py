from .Guerreiro import Guerreiro


class Paladino(Guerreiro):
    def __init__(self):
        super().__init__()
        self.habilidades_classe.extend([
            'Imunidades a Doenças', 
            'Cura pelas Mãos', 
            'Aura de Proteção', 
            'Espada Sagrada'
        ])