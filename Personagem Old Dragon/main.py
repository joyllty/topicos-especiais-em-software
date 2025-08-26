from Personagem import Personagem
from racas import Humano, Elfo, Anao, Gnomo, Halfling, MeioElfo
from classes import Barbaro, Paladino, Druida, Academico, Ranger, Bardo, Ilusionista, Necromante
from utils import limpar_tela
import time


def main():
    limpar_tela()
    personagem = Personagem()

    print('\nBEM VINDO A CRIAÇÃO DE PERSONAGEM OLD DRAGON!')

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

    # =========== ESCOLHER RAÇA ===========
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
    # =========== ESCOLHER CLASSE ===========
    while True:
        print('>> Selecione a classe do seu personagem: ')
        print('========= Classes =========')
        print('[1] Guerreiro\n[2] Clérigo\n[3] Ladrão\n[4] Mago')
        print('===========================')

        try:
            op_classes = int(input('>> '))
        except ValueError:
            print('>> |ERRO| Digite apenas números! (1 a 4)\n')
            continue

        if op_classes == 1:
            limpar_tela()
            print('>> Selecione a subclasse: ')
            print('====== Guerreiro =====')
            print('[1] Bárbaro\n[2] Paladino')
            print('======================')
            try:
                op_subclasse = int(input('>> '))
            except ValueError:
                print('>> |ERRO| Digite apenas números! (1 ou 2)\n')
                continue

            if op_subclasse == 1:
                personagem.classe = Barbaro()
            elif op_subclasse == 2:
                personagem.classe = Paladino()
            else:
                print('\n>> |ERRO| Digite apenas 1 ou 2!\n')
                continue

        elif op_classes == 2:
            limpar_tela()
            print('>> Selecione a subclasse: ')
            print('======= Clérigo ======')
            print('[1] Druida\n[2] Acadêmico')
            print('======================')
            try:
                op_subclasse = int(input('>> '))
            except ValueError:
                print('>> |ERRO| Digite apenas números! (1 ou 2)\n')
                continue

            if op_subclasse == 1:
                personagem.classe = Druida()
            elif op_subclasse == 2:
                personagem.classe = Academico()
            else:
                print('\n>> |ERRO| Digite apenas 1 ou 2!\n')
                continue

        elif op_classes == 3:
            limpar_tela()
            print('>> Selecione a subclasse: ')
            print('====== Ladrão ======')
            print('[1] Ranger\n[2] Bardo')
            print('====================')
            try:
                op_subclasse = int(input('>> '))
            except ValueError:
                print('>> |ERRO| Digite apenas números! (1 ou 2)\n')
                continue

            if op_subclasse == 1:
                personagem.classe = Ranger()
            elif op_subclasse == 2:
                personagem.classe = Bardo()
            else:
                print('\n>> |ERRO| Digite apenas 1 ou 2!\n')
                continue
            
        elif op_classes == 4:
            limpar_tela()
            print('>> Selecione a subclasse: ')
            print('======== Mago =======')
            print('[1] Ilusionista\n[2] Necromante')
            print('=====================')
            try:
                op_subclasse = int(input('>> '))
            except ValueError:
                print('>> |ERRO| Digite apenas números! (1 ou 2)\n')
                continue

            if op_subclasse == 1:
                personagem.classe = Ilusionista()
            elif op_subclasse == 2:
                personagem.classe = Necromante()
            else:
                print('\n>> |ERRO| Digite apenas 1 ou 2!\n')
                continue
        else:
            print('\n>> |ERRO| Digite apenas um número entre 1 e 4!\n')
            continue
        
        break

    limpar_tela()
    # =========== ESCOLHER DISTRIBUIÇÃO DE ATRIBUTOS ===========
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
    # =========== MENU PRINCIPAL ===========
    while True:
        print('>> O que deseja fazer agora?')
        print('=================================\n[1] Exibir Atributos\n[2] Informações do Personagem\n[3] Exibir Habilidades de Classe\n[4] Exibir Habilidades da Raça\n[0] Sair\n=================================')

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
        elif op_acao == 3:
            personagem.classe.exibir_habilidades_classe()
        elif op_acao == 4:
            personagem.raca.exibir_habilidades_raca()
        else:
            print('>> |ERRO| Digite apenas um número entre 0 a 4!\n')
            continue
        
        
        
if  __name__ == '__main__':
    main()        