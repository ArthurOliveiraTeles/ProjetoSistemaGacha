"""
@author Arthur Oliveira Teles

Data da última modificação : 16/12/2020

"""

from GenshinImpact.sistema import funcoes1


def linha():
    l = '-' * 20
    return l


def linha2(pool):
    l = f'----------Você deu {pool} tiros!----------'
    return l


print(f'\033[7;30;44m{linha()}SISTEMA DE GACHA (V.1){linha()}')

print("""Bem vindo ao simulador de Gacha do Genshin Impact.
Aqui você poderá simular tiros infinitos nessa primeira versão...
Bons tiros e boa sorte !
""")

print('Escolha um dos banners abaixo para atirar: ')

print("""
1 - Venti Banner ( 50%+ chance de vir o Venti! )\033[m 
""")

cont = 0
valido = True
while valido == True:
    choice = 0
    quest = ' '
    while choice != 1:

        print(linha())
        choice = int(input('Digite a opção desejada: '))
        print(linha())
        if choice != 1:
            print('\n\033[31mOpção inválida, digite novamente.\033[m\n')

        else:
            from time import sleep

            tiros = int(input('Quantos tiros deseja dar? '))
            cont += tiros

            print('Calculando...')
            sleep(1)
            print(f'\033[34m{linha2(tiros)}\033[m')
            funcoes1.banner(tiros, choice)
            funcoes1.contadorTiros(cont)

            if cont >= 15:  # Aqui preciso mexer para fazer o pit no 15° tiro. Preciso criar um outro arquivo
                cont *= 0  # e chamar a função contadorTiros em um arquivo "funcoes2", e criar o pit por lá.
                funcoes1.contadorTiros(15, True)

            # funcoes1.banner()
            quest = str(input('\nDeseja continuar?? [S/N]')).upper()[0]

        if quest == 'N':
            print('Volte sempre!')
            valido = False
