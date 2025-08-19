'''
2. Métodos e Atributos: Crie uma classe Carro com os atributos marca, modelo e ano. Adicione
métodos para alterar e obter esses valores. Inclua também um método para exibir as informações do
carro.
'''

class Carro():
    
    def __init__(self):
        self._marca = None
        self._modelo = None
        self._ano = None

    @property
    def marca(self):
        return self._marca
    
    @marca.setter
    def marca(self, valor):
        self._marca = valor

    @property
    def modelo(self):
        return self._modelo
    
    @modelo.setter
    def modelo(self, valor):
        self._modelo = valor
    
    @property
    def ano(self):
        return self._ano
    
    @ano.setter
    def ano(self, valor):
        self._ano = valor

    def get_info(self):
        print('===== Informações do Carro =====')
        print(f'>> Marca: {self.marca}')
        print(f'>> Modelo: {self.modelo}')
        print(f'>> Ano: {self.ano}')

if __name__ == '__main__':
    carro1 = Carro()
    carro2 = Carro()

    carro1.marca = 'honda'
    carro2.marca = 'toyota'

    carro1.modelo = 'suv'
    carro2.modelo = 'sedan'

    carro1.ano = 2016
    carro2.ano = 2023

    carro1.get_info()
    carro2.get_info()
