from abc import ABC, abstractmethod

'''
10. Classes Abstratas: Crie uma classe abstrata Funcionario com um método abstrato calcularSalario().
Implemente duas subclasses, FuncionarioHorista e FuncionarioMensalista, que implementam o cálculo
de salários de acordo com o tipo de funcionário.
'''

class Funcionario(ABC):
    @abstractmethod
    def calcularSalario():
        pass


class FuncionarioHorista(Funcionario):
    def __init__(self, horas_trabalhadas, valor_hora):
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora

    def calcularSalario(self):
        return self.horas_trabalhadas * self.valor_hora
    

class FuncionarioMensalista(Funcionario):
    def __init__(self, salario_mensal):
        self.salario_mensal = salario_mensal

    def calcularSalario(self):
        return self.salario_mensal
    

if __name__ == '__main__':
    horista = FuncionarioHorista(160, 20)
    mensalista = FuncionarioMensalista(3000)

    print(f'\n>> Salário Horista: {horista.calcularSalario()}')
    print(f'>> Salário Mensalista: {mensalista.calcularSalario()}')
        
        