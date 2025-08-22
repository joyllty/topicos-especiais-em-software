from Personagem import Personagem
from Dado import Dado


class Classico(Personagem):
    def __init__(self):
        super().__init__()
        self.dado = Dado(6)

    def gerar_atributos(self):
        valores_gerados = []

        for i in range(6):
            acumulado = 0
            for j in range(3):
                acumulado += self.dado.rolar()
            valores_gerados.append(acumulado)

        atributos = ['forca', 'destreza', 'constituicao', 'inteligencia', 'sabedoria', 'carisma']

        # zip -> junta cada elemento de listas em pares (tuplas)
        # setattr -> atribuir um valor a um atributo de um objeto 
        for nome, valor in zip(atributos, valores_gerados):
            setattr(self, nome, valor)
            # exemplo: self.forca = valor_gerado[0]
                    