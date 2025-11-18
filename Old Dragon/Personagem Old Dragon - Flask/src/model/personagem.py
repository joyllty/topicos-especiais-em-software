from model.dado import Dado

class Personagem:
    def __init__(self):
        self.nome = None
        self.forca = 0
        self.destreza = 0
        self.constituicao = 0
        self.inteligencia = 0
        self.sabedoria = 0
        self.carisma = 0
        self.raca = None
        self.classe = None
        self.dado = Dado(6)
        self.valores_gerados = []

    # ======= ESTILOS =======
    def estilo_classico(self):
        valores_gerados = []
        for i in range(6):
            acumulado = sum(self.dado.rolar() for _ in range(3))
            valores_gerados.append(acumulado)

        atributos = ['forca', 'destreza', 'constituicao', 'inteligencia', 'sabedoria', 'carisma']

        for nome, valor in zip(atributos, valores_gerados):
            setattr(self, nome, valor)

        self.valores_gerados = valores_gerados

        return valores_gerados

    def estilo_aventureiro(self):
        valores_gerados = []
        for i in range(6):
            acumulado = sum(self.dado.rolar() for _ in range(3))
            valores_gerados.append(acumulado)
        
        self.valores_gerados = valores_gerados

        return valores_gerados

    def estilo_heroico(self):
        valores_gerados = []
        for i in range(6):
            rolagens = [self.dado.rolar() for _ in range(4)]
            menor = min(rolagens)
            soma = sum(rolagens) - menor
            valores_gerados.append(soma)

        self.valores_gerados = valores_gerados
        
        return valores_gerados

    # ======= DISTRIBUIR ATRIBUTOS =======
    def distribuir_atributos(self, distribuicao):
        for attr, valor in distribuicao.items():
            if hasattr(self, attr):
                setattr(self, attr, valor)

    # ======= EXPORTAR PRO JSON =======
    def to_dict(self):
        return {
            "nome": self.nome,
            "forca": self.forca,
            "destreza": self.destreza,
            "constituicao": self.constituicao,
            "inteligencia": self.inteligencia,
            "sabedoria": self.sabedoria,
            "carisma": self.carisma,
            "raca": self.raca.__class__.__name__ if self.raca else None,
            "classe": self.classe.__class__.__name__ if self.classe else None,
            "valores_gerados": self.valores_gerados
        }
