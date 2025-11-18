import math
'''
8. Polimorfismo com Herança: Crie uma classe Forma com um método calcularArea(). Crie classes
Circulo e Quadrado que herdam de Forma e sobrescrevem o método para calcular a área específica de
cada forma. Pense em como o polimorfismo pode ajudar calcular áreas de diferentes formas em uma
lista de Formas.
'''

class Forma():
    def calcularArea():
        pass


class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio
        

    def calcularArea(self):
        return math.pi * (self.raio ** 2)
    

class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def calcularArea(self):
        return self.lado ** 2
    

if __name__ == '__main__':
    formas = [Circulo(3), Quadrado(4), Circulo(5)]

    for forma in formas:
        print(f'\n>> Área: {forma.calcularArea():.2f}')


