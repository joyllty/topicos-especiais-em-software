from Personagem import Personagem
from Dado import Dado


class Heroico(Personagem):
    def __init__(self):
        super().__init__()
        self.dado = Dado(6)

    def gerar_atributos(self):
        valores_gerados = []

        for i in range(6):
            rolagens = []

            for j in range(4):
                dado = self.dado.rolar()
                rolagens.append(dado)

            menor = min(rolagens)
            soma = sum(rolagens) - menor

            valores_gerados.append(soma)

        self.distribuir_atributos(valores_gerados)

    

    