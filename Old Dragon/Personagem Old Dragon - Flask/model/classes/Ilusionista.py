from .Mago import Mago


class Ilusionista(Mago):
    def __init__(self):
        super().__init__()
        self.habilidades_classe.extend([
            'Magias Exclusivas', 
            'Ilusão Melhorada', 
            'Miragem', 
            'Ilusão Permanente'
        ])