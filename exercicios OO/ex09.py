'''
9. Polimorfismo com Sobrecarga: Crie uma classe Calculadora com dois métodos somar, um que
recebe dois inteiros e outro que recebe dois double. Teste os métodos chamando somar com diferentes
tipos de argumentos.
'''

class Calculadora():
    def __init__(self):
        pass

    def somar(self, num1, num2):
        return num1 + num2
    

if __name__ == '__main__':
    calc = Calculadora()
    print(calc.somar(5, 9))
    print(calc.somar(1.5, 7.5))

    