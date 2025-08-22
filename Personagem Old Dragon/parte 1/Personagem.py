from abc import ABC, abstractmethod


class Personagem(ABC):
    def __init__(self):
        self.forca = 0
        self.destreza = 0
        self.constituicao = 0
        self.inteligencia = 0
        self.sabedoria = 0
        self.carisma = 0 

    def exibir_atributos(self):
        print('\n======= SEUS ATRIBUTOS =======')
        print(f'>> Força: {self.forca}')
        print(f'>> Destreza: {self.destreza}')
        print(f'>> Constituição: {self.constituicao}')
        print(f'>> Inteligência: {self.inteligencia}')
        print(f'>> Sabedoria: {self.sabedoria}')
        print(f'>> Carisma: {self.carisma}')
        print('==============================')

    @abstractmethod
    def gerar_atributos(self):
        pass
        
    def distribuir_atributos(self, valores_gerados):
        print('\n=========== Escolha seus Atributos ===========')
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