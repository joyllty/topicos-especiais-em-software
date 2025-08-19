'''
3. Construtor com Sobrecarga: Crie uma classe Produto com atributos nome e preco. Adicione dois
construtores: um que recebe ambos os atributos e outro que inicializa apenas o nome (sobrecarga de
construtores, em python, gambiarra).
'''

class Produto():
    def __init__(self, nome, preco=None):
        self.nome = nome
        self.preco = preco


if __name__ == '__main__':
    p1 = Produto('Celular', 2000)
    p2 = Produto('Notebook')

    print(f'>> {p1.nome}, preço: {p1.preco}')
    print(f'>> {p2.nome}, preço: {p2.preco}')