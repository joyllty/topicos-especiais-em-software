'''
7. Usando super(): Modifique o exercício anterior para que Carro e Esportivo usem o método super()
no construtor (da classe base), para inicializar atributos da classe Veiculo.
'''

class Veiculo():
    def __init__(self, tipo, rodas):
        self.tipo = tipo
        self.rodas = rodas

    def mover(self):
        print('\n>> O veículo começou a se mover... ')


class Carro(Veiculo):
    def __init__(self, tipo, rodas):
        super().__init__(tipo, rodas)

    def abastecer(self):
        print('\n>> Carro está abastecendo...')


class Esportivo(Carro):
    def __init__(self, tipo, rodas):
        super().__init__(tipo, rodas)

    def turbo(self):
        print('\n>> Ativando turbo...')


if __name__ == '__main__':
    carro = Carro('Carro', True)
    carro_sport = Esportivo('Carro', True)

    carro.mover()
    carro_sport.mover()

    carro.abastecer()
    carro_sport.abastecer()

    carro_sport.turbo()