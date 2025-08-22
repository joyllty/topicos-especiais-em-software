from Classico import Classico
from Heroico import Heroico
from Aventureiro import Aventureiro


print('\nBEM VINDO A CRIAÇÃO DE PERSONAGEM OLD DRAGON!')
escolha_valida = False

while True: 
    print('\n>> Selecione a forma de distribuição de atributos: ')
    print('=======================\n[1] Estilo Clássico\n[2] Estilo Aventureiro\n[3] Estilo Heróico \n[0] Sair\n=======================')

    try:
        opcao = int(input('>> '))
    except ValueError:
        print('>> |ERRO| Digite apenas números!(0 a 3)')
        continue
        
    if opcao == 0:
        print('>> Encerrando programa...')
        exit()
    elif opcao == 1:
        personagem = Classico()
    elif opcao == 2:
        personagem = Aventureiro()
    elif opcao == 3:
        personagem = Heroico()
    else:
        print('>> |ERRO| Digite apenas um número entre 0 e 3!')
        continue
        
    personagem.gerar_atributos()
    break

while True:
    print('\n>> O que deseja fazer agora? ')
    print('=======================\n[1] Ver atributos\n[0] Sair\n=======================')

    try:
        acao = int(input('>> '))
    except ValueError:
        print('>> |ERRO| Digite apenas números! (0 ou 1)')

    if acao == 0:
        print('>> Encerrando programa...')
        exit()
    elif acao == 1:
        personagem.exibir_atributos()
        break
    else:
        print('\n>> |ERRO| Digite apenas 0 ou 1!')
