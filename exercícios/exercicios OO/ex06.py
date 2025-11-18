'''
6. Herança em Cadeia: Crie uma classe Veiculo com um método mover(). Crie uma classe Carro que
herda de Veiculo e adiciona o método abastecer(). Em seguida, crie uma classe Esportivo que herda de
Carro e adiciona o método turbo().
'''

class Veiculo():
    def __init__(self):
        pass

    def mover(self):
        print('\n>> O veículo começou a se mover... ')


class Carro(Veiculo):
    def __init__(self):
        super().__init__()

    def abastecer(self):
        print('\n>> Carro está abastecendo...')


class Esportivo(Carro):
    def __init__(self):
        super().__init__()

    def turbo(self):
        print('\n>> Ativando turbo...')


if __name__ == '__main__':
    carro = Carro()
    carro_sport = Esportivo()

    carro.mover()
    carro_sport.mover()

    carro.abastecer()
    carro_sport.abastecer()

    carro_sport.turbo()