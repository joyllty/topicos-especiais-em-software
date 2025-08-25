from abc import ABC, abstractmethod
from Dado import Dado
from utils import limpar_tela

class Personagem():
    def __init__(self):
        self.nome = None
        self.forca = 0
        self.destreza = 0
        self.constituicao = 0
        self.inteligencia = 0
        self.sabedoria = 0
        self.carisma = 0 
        self.raca = None
        self.classe = None
        self.dado = Dado(6)
        
    # def habilidades_raca(): ?

    # ===== INFORMAÇÕES =====
    def exibir_atributos(self):
            print('\n======= SEUS ATRIBUTOS =======')
            print(f'>> Força: {self.forca}')
            print(f'>> Destreza: {self.destreza}')
            print(f'>> Constituição: {self.constituicao}')
            print(f'>> Inteligência: {self.inteligencia}')
            print(f'>> Sabedoria: {self.sabedoria}')
            print(f'>> Carisma: {self.carisma}')
            print('==============================\n')
    
    def exibir_info(self):
        print('\n========= INFORMAÇÕES =========')
        print(f'>> Nome: {self.nome}')
        print(f'>> Raça: {self.raca.__class__.__name__}')
        print(f'>> Classe: {self.classe}')
        print(f'>> Peso-Base: {self.raca.peso_base}')
        print(f'>> Vida: {self.classe}')
        print(f'>> Ataque: {self.classe}')
        print(f'>> Defesa: {self.classe}')
        print('================================\n')

    # ====== ESTILOS =====
    def estilo_classico(self):
        valores_gerados = []

        for i in range(6):
            acumulado = 0
            for j in range(3):
                acumulado += self.dado.rolar()
            valores_gerados.append(acumulado)

        atributos = ['forca', 'destreza', 'constituicao', 'inteligencia', 'sabedoria', 'carisma']

        # zip -> junta cada elemento de listas em pares (tuplas)
        # setattr -> atribuir um valor a um atributo de um objeto 
        for nome, valor in zip(atributos, valores_gerados):
            setattr(self, nome, valor)
            # exemplo: self.forca = valor_gerado[0]

    def estilo_aventureiro(self):
        valores_gerados = []

        for i in range(6):
            acumulado = 0
            for j in range(3):
                acumulado += self.dado.rolar()
            valores_gerados.append(acumulado)

        atributos = ['forca', 'destreza', 'constituicao', 'inteligencia', 'sabedoria', 'carisma']

        for nome, valor in zip(atributos, valores_gerados):
            setattr(self, nome, valor)
            
        limpar_tela()    
        self.distribuir_atributos(valores_gerados)

    def estilo_heroico(self):
        valores_gerados = []

        for i in range(6):
            rolagens = []

            for j in range(4):
                dado = self.dado.rolar()
                rolagens.append(dado)

            menor = min(rolagens)
            soma = sum(rolagens) - menor

            valores_gerados.append(soma)

        limpar_tela()
        self.distribuir_atributos(valores_gerados)
        
    def distribuir_atributos(self, valores_gerados):
        print('=========== Escolha seus Atributos ===========')
        print(f'>> Valores gerados pelos dados: {valores_gerados}')

        dicionario_atributos = {
            '1': 'forca',
            '2': 'destreza',
            '3': 'constituicao',
            '4': 'inteligencia',
            '5': 'sabedoria',
            '6': 'carisma',
        }

        escolhidos = []

        for valor in valores_gerados:
            escolha_valida = False
            while escolha_valida == False:
                print(f'\n>> Qual atributo você escolhe para receber: {valor}?')

                for chave, nome in dicionario_atributos.items():
                    if chave not in escolhidos:
                        print(f'[{chave}] {nome.capitalize()}')

                try:
                    escolha = (input('>> '))
                except Exception as e:
                    print('>> |ERRO {e}| Tente novamente: ')
                    continue

                if escolha in dicionario_atributos and escolha not in escolhidos:
                        setattr(self, dicionario_atributos[escolha], valor)
                        escolhidos.append(escolha)
                        escolha_valida = True
                else: 
                    print('\n>> Opção inválida ou já escolhida! Tente novamente.')