def banner(pool, banner):  # aqui é a função do banner ( tiros, choice )
    """
    :param pool: Quantos tiros a pessoa escolheu
    :param banner: Qual banner é para rodar
    :return:
    """
    lista = ['Venti']  # venti na pos 0

    for i, v in enumerate(lista):
        upChar = lista[banner - 1]

    if upChar == 'Venti':  # se for == 0 é o banner do Venti
        return nat5(pool, upChar)  # passei os param de qnt de tiro e o personagem do banner
        # que terá um up no banner


def nat5(pool, upChar=''):
    """

    :param pool: qnt. tiros da função banner
    :param upChar: Aqui o param upChar será trabalhado diversas vezes pelas funções
    :return: O return dessa função varia de acordo com o que o usuário
    tirou no banner em seus tiros, se ele não tirou o personagem do banner (nesse caso o Venti),
    ele PRECISA tirar o 'Venti' ('doBanner1 retorna o Venti para o usuário').
    """

    if upChar == 'doBanner1':  # Obrigação de tirar o Venti
        return personagens(pool, 'Venti')  # Manda para a lista o Venti e encerra a função.

    chars5 = [upChar, 1]  # 50% de chance de tirar o Venti (personagem do Banner).

    import random

    magica = random.randint(0, 1)
    decisao = chars5[magica]

    if decisao == 'Venti':  # var decisao NÃO pega o indice '0' nesse caso.
        upChar = 'Venti'
    else:  # Se não for o Venti, a máquina irá sortear outro nat-5.
        lista = ['Keqing', 'Diluc', 'Mona', 'Jean', 'QiQi']
        magica2 = random.randint(0, len(lista) - 1)
        upChar = lista[magica2]

    return personagens(pool, upChar)  # Aqui a função faz a chamada para a def personagens que possui
    # a lista de personagens.


def personagens(pool, upChar=''):
    lista = ['Fischl', 'Barbara', 'Xiangling', 'Bennet', 'Xingqiu', 'Ningguang',
             'Razor', 'Sucrose', 'Beidou', 'Chongyun', 'Kaeya',
             'Lisa', 'Noelle', 'Amber', upChar]

    return tiro(pool, lista)  # Manda os param para a def tiro.


def tiro(pool=0, chars=[], garantido=False):  # chars é a LISTA ( lembra!!! )
    """

    :param garantido:
    :param pool: quantidade de tiros que o usuário escolheu.
    :param chars: LISTA de personagens ( vem da def personagens() ).
    :return: retorna o Venti como obrigação se o tiro for diferente de Venti.
             Ou pode retornar outro personagem no 50/50.
    """
    import random
    from time import sleep

    cont = 0  # contador para calcular os tiros dados.

    #  pool > 10:
    #   print('\033[31mVocê não pode dar mais que 10 tiros.\033[m')
    #  return

    if garantido:
        print(chars[14])

    for c in range(0, pool):
        tiro = random.randint(0, (len(chars) - 1))  # tem que fazer -1 porque o tamanLista == 15

        sleep(0.5)

        if tiro == 14:
            personagem = cores(1)
        else:
            personagem = cores(0)

        print(f'tirou: ', end=f'{personagem}')
        print(f'{chars[tiro]}\033[m')

        if tiro == 14:
            if chars[tiro] != 'Venti':
                newPool = pool - cont - 1  # Para ele realizar os tiros que faltam, subtraí do pool, o cont.
                return nat5(newPool, 'doBanner1')  # Manda o parâm 'doBanner1' para a def nat5().
            else:
                newPool = pool - cont - 1  # O -1 eu adicionei pois ele estava dando um tiro a mais...
                return nat5(newPool, 'Venti')

        cont += 1  # a cada novo tiro, o contador é adicionado em 1.

    # if cont > 10:
    #   return


def contadorTiros(cont=0, pit=False):
    if pit:
        return tiro(0, True) # Aqui preciso retornar em uma futura função em outro arquivo
                                    # para conseguir fazer o pit

    print(f'Contador de tiros: {cont}')


def cores(name):
    if name == 0:
        cor = '\033[35m'
    else:
        cor = '\033[33m'

    return cor
