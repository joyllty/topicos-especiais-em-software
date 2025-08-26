from .Ladrao import Ladrao


class Ranger(Ladrao):
    def __init__(self):
        super().__init__()
        self.habilidades_classe.extend([
            'Inimigo Mortal', 
            'Combativo', 
            'Previdência', 
            'Companheiro Animal'
        ])
