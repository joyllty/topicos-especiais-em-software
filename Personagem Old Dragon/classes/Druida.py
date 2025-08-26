from .Clerigo import Clerigo


class Druida(Clerigo):
    def __init__(self):
        super().__init__()
        self.habilidades_classe.extend([
            'Herbalismo', 
            'Previdência', 
            'Transformação', 
            'Transformação Melhorada'
        ])