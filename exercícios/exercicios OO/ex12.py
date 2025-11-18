from abc import ABC, abstractmethod

'''
12. Interface com Várias Classes: Crie duas interfaces, Voador e Nadador, com métodos voar() e
nadar(). Implemente essas interfaces em classes Pato, Aguia e Peixe para simular um comportamento
específico (obs.: Pato voa e nada, Peixe só nada, Aguia só voa).
'''

class Voador(ABC):
    @abstractmethod
    def voar(self):
        pass


class Nadador(ABC):
    @abstractmethod
    def nadar(self):
        pass


class Pato(Voador, Nadador):
    def voar(self):
        print('O pato está voando...')

    def nadar(self):
        print('O pato está nadando...')


class Aguia(Voador):
    def voar(self):
        print('A águia está voando...')


class Peixe(Nadador):
    def nadar(self):
        print('O peixe está nadando...')



if __name__ == '__main__':
    animais = [Pato(), Aguia(), Peixe()]

    for animal in animais:
        if isinstance(animal, Voador):  
            animal.voar()
        if isinstance(animal, Nadador): 
            animal.nadar()
    