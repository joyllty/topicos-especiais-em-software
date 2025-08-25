from Personagem import Personagem
from racas.Humano import Humano
from racas.Elfo import Elfo
from racas.Anao import Anao
from racas.Gnomo import Gnomo
from racas.Halfling import Halfling
from racas.Meio_Elfo import MeioElfo
from utils import limpar_tela
import time


def main():
    limpar_tela()
    personagem = Personagem()

    print('\nBEM VINDO A CRIAÇÃO DE PERSONAGEM OLD DRAGON!')
    escolha_valida = False

    print('\n>> Qual é o nome do seu personagem? ')
    personagem.nome = input('>> ')

    limpar_tela()

    print('\n>> Para criar o seu personagem, deverá passar por três etapas: ')
    print('==============================')
    time.sleep(1)
    print('• Escolha da Raça')
    time.sleep(1)
    print('• Escolha da Classe')
    time.sleep(1)
    print('• Distribuição dos Atributos')
    print('==============================')
    time.sleep(2)
    limpar_tela()

    while True: 
        print('>> Selecione a forma de distribuição de atributos: ')
        print('=======================\n[1] Estilo Clássico\n[2] Estilo Aventureiro\n[3] Estilo Heróico \n[0] Sair\n=======================')

        try:
            op_atributos = int(input('>> '))
        except ValueError:
            print('>> |ERRO| Digite apenas números! (0 a 3)\n')
            continue

        if op_atributos == 0:
            print('>> Encerrando programa...')
            exit()
        elif op_atributos == 1:
            personagem.estilo_classico()
        elif op_atributos == 2:
            personagem.estilo_aventureiro()
        elif op_atributos == 3:
            personagem.estilo_heroico()
        else:
            print('>> |ERRO| Digite apenas um número entre 0 e 3!\n')
            continue
            
        break


    limpar_tela()

    while True:
        print('>> Selecione a raça do seu personagem: ')
        print('=========== Raças ==========')
        print('[1] Humano\n[2] Elfo\n[3] Anão\n[4] Halfling\n[5] Gnomo\n[6] Meio-Elfo')
        print('============================')

        try:
            op_racas = int(input('>> '))
        except ValueError:
            print('>> |ERRO| Digite apenas números! (1 a 6)\n')
            continue

        if op_racas == 1:
            personagem.raca = Humano()
        elif op_racas == 2:
            personagem.raca = Elfo()
        elif op_racas == 3:
            personagem.raca = Anao()
        elif op_racas == 4:
            personagem.raca = Halfling()
        elif op_racas == 5:
            personagem.raca = Gnomo()
        elif op_racas == 6:
            personagem.raca = MeioElfo()
        else:
            print('\n>> |ERRO| Digite apenas 0 ou 1!\n')
            continue
        

        break

    limpar_tela()

    while True:
        print('>> O que deseja fazer agora?')
        print('==============================\n[1] Exibir Atributos\n[2] Informações do Personagem\n[0] Sair\n==============================')

        try:
            op_acao = int(input('>> '))
        except ValueError:
            print('>> |ERRO| Digite apenas números! (0 a 3)\n')
            continue
            
        if op_acao == 0:
            break
        elif op_acao == 1:
            personagem.exibir_atributos()
        elif op_acao == 2:
            personagem.exibir_info()
        else:
            print('>> |ERRO| Digite apenas um número entre 0 a 3!\n')
            continue

        
        
if  __name__ == '__main__':
    main()        