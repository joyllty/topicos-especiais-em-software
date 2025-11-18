from .Mago import Mago


class Necromante(Mago):
    def __init__(self):
        super().__init__()
        self.habilidades_classe.extend([
            'Magias Exclusivas', 
            'Criar Mortos-Vivos', 
            'Drenas Vida', 
            'Magia da Morte'
        ])