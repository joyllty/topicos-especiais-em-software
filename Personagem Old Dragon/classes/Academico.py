from .Clerigo import Clerigo


class Academico(Clerigo):
    def __init__(self):
        super().__init__()
        self.habilidades_classe.extend([
            'Conhecimento Acadêmico', 
            'Decifrar Linguagens', 
            'Lendas e Tradições', 
            'Identificar Itens'
        ])
