'''
4. Herança Simples: Crie uma classe Funcionario com atributos nome e salario. Em seguida, crie uma
classe Gerente que herda de Funcionario e adicione o atributo departamento. Adicione um método para
exibir as informações do gerente.
'''

class Funcionario():
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario


class Gerente(Funcionario):
    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario)
        self.departamento = departamento

    def get_info(self):
        print(f'===== Informações do Gerente =====')
        print(f'>> Nome: {self.nome}')
        print(f'>> Salário: {self.salario}')
        print(f'>> Departamento: {self.departamento}')


if __name__ == '__main__':
    gerente1 = Gerente('Bruna', 10000, 'TI')
    gerente1.get_info()