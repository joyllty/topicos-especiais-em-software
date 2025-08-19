from abc import ABC, abstractmethod
'''
11. Interface Básica: Crie uma interface Imprimivel com o método imprimir(). Implemente esta
interface nas classes Documento e Foto. Cada implementação deve exibir uma mensagem indicando o
tipo de impressão.
'''

class Imprimivel(ABC):
    @abstractmethod
    def imprimir(self):
        pass


class Documento(Imprimivel):
    def __init__(self, titulo):
        self.titulo = titulo

    def imprimir(self):
        print(f'Imprimindo documento: {self.titulo}...')


class Foto(Imprimivel):
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo

    def imprimir(self):
        print(f'Imprimindo foto: {self.nome_arquivo}...')


if __name__ == '__main__':
    itens = [Documento("Relatório"), Foto("Foto102.jpg")]

for item in itens:
    item.imprimir()



