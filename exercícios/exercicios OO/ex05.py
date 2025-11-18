'''
5. Sobrescrita de Métodos: Crie uma classe Animal com o método som() que imprime "O animal faz
um som". Crie classes Cachorro e Gato que herdam de Animal e sobrescreva o método som() para
imprimir sons específicos para cada animal
'''

class Animal():
    def __init__(self):
        pass

    def som(self):
        print('O animal faz um som')


class Cachorro(Animal):
    def __init__(self):
        super().__init__()

    def som(self):
        print('au au')


class Gato(Animal):
    def __init__(self):
        super().__init__()


    def som(self):
        print('meow')


if __name__ == '__main__':
    dog = Cachorro()
    cat = Gato()

    dog.som()
    cat.som()