#neste jogo, os jogadores deverão escolher suas posições no início, sem que o outro veja, e depois trocar turnos tentando adivinhar a posição do outro. eles poderam escolher entre trocar de lugar ou atacar. cada jogador tem 100 pontos de vida, e cada flecha acertada tira 50 destes pontos do oponente

from time import sleep
from funções_ex3 import clearConsole, posição, ataque, linha
from random import randint

hp1 = 100
hp2 = 100

cores = {    #cores normais

         'vermelho':'\033[31m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'branco':'\033[30m',
         'verde claro':'\033[91m',
         'verde':'\033[32m',
         'ciano':'\033[36m',
         'limpa':'\033[m',
         'preto e branco':'\033[7;97;m',

                #cores em negrito

         'vermelho em negrito':'\033[1;31m',
         'azul em negrito':'\033[1;34m' ,
         'amarelo em negrito':'\033[1;33m' ,
         'branco em negrito':'\033[1;97m',
         'roxo em negrito':'\033[1;35m',
         'verde em negrito':'\033[1;32m',
         'ciano em negrito':'\033[1;36m',

               #cores sublinhadas

         'vermelho sublinhado':'\033[4;31m',
         'azul sublinhado':'\033[4;34m',
         'amarelo sublinhado':'\033[4;33m',
         'branco sublinhado':'\033[4;97m',
         'roxo sublinhado':'\033[4;35m',
         'verde sublinhado':'\033[4;32m',
         'ciano sublinhado':'\033[4;36m'
         }

clearConsole()
linha(30, '\033[1;32m')
print(f'{cores["branco em negrito"]}Bem-vindo ao jogo, jogador 1! Pressione qualquer tecla para continuar!{cores["limpa"]}')
linha(30, '\033[1;32m')
a = input()
nome1 = input('Primeiro, digite seu nome: ')
sleep(1)
p1 = posição('Muito bem! Agora, escolha uma posição de 1 até 10', nome1)
sleep(1.5)
print('Passando agora para o próximo jogador...')
sleep(2.5)

clearConsole()

linha(30, '\033[1;32m')
print(f'{cores["branco em negrito"]}Bem-vindo ao jogo, jogador 2! Pressione qualquer tecla para continuar!{cores["limpa"]}')
linha(30, '\033[1;32m')
a = input()
nome2 = input('Primeiro, digite seu nome: ')
sleep(1)
p2 = posição('Muito bem! Agora, escolha uma posição de 1 até 10', nome2)
sleep(1.5)
print('Preparando os ataques!...')
sleep(3)
clearConsole()

while True:
    vento = randint(0, 3)
    direção = randint(1, 2)
    if direção == 1:
        vento = vento * -1
    print(f'{cores["azul em negrito"]}É a sua vez de jogar, {nome1}{cores["limpa"]}')
    if vento < 0:
        print(f'{cores["azul em negrito"]}O vento está {vento} posições para a esquerda{cores["limpa"]}\n')
    elif vento > 0:
        print(f'{cores["azul em negrito"]}O vento está {vento} posições para a direita{cores["limpa"]}\n')
    else:
        print(f'{cores["azul em negrito"]}Não há vento!{cores["limpa"]}\n')
    print(f'{cores["azul em negrito"]}Seu HP: {hp1}{cores["limpa"]}\n')
    print('O que você gostaria de fazer?\nDigite 1 para atacar\nDigite 2 para mudar de posição')
    while True:
        try:
            escolha = int(input('Sua escolha: '))
        except:
            print('Escolha uma opção válida!')
        else:
            if escolha > 2 or escolha < 1:
                print('Escolha uma opção válida!')
            else:
                break
    sleep(1)
    if escolha == 1:
        tiro = ataque(nome1)
        if tiro + vento == p2:
            print(f'{cores["verde em negrito"]}Muito bem {nome1}! Você acertou o alvo!{cores["limpa"]}')
            sleep(1)
            hp2 = hp2 - 50
            if hp2 == 0:
                print('Uau! Você é bom mesmo! O HP dele agora é igual a 0, você venceu!')
                break
            else: 
                print('O HP dele agora é igual a 50!\n')
                sleep(1.9)
        else:
            print(f'{cores["vermelho em negrito"]}Ops! Você errou, vez do outro jogador{cores["limpa"]}')
            sleep(1.9)
    else:
        p1 = posição('Ok! Escolha sua nova posição: ', nome1)
    sleep(2)
    clearConsole()
    vento = randint(0, 3)
    direção = randint(1, 2)
    if direção == 1:
        vento = vento * -1
    print(f'{cores["azul em negrito"]}É a sua vez de jogar, {nome2}{cores["limpa"]}')
    if vento < 0:
        print(f'{cores["azul em negrito"]}O vento está {vento} posições para a esquerda{cores["limpa"]}\n')
    elif vento > 0:
        print(f'{cores["azul em negrito"]}O vento está {vento} posições para a direita{cores["limpa"]}\n')
    else:
        print(f'{cores["azul em negrito"]}Não há vento!{cores["limpa"]}\n')
    print(f'{cores["azul em negrito"]}Seu HP: {hp2}{cores["limpa"]}\n')
    print('O que você gostaria de fazer?\nDigite 1 para atacar\nDigite 2 para mudar de posição')
    while True:
        try:
            escolha = int(input('Sua escolha: '))
        except:
            print('Escolha uma opção válida!')
        else:
            if escolha < 1 or escolha > 2:
                print('Escolha uma opção válida!')
            else:
                break
    sleep(1)
    if escolha == 1:
        tiro = ataque(nome2)
        if tiro + vento == p1:
            print(f'{cores["verde em negrito"]}Muito bem {nome2}! Você acertou o alvo!{cores["limpa"]}')
            sleep(1)
            hp1 = hp1 - 50
            if hp1 == 0:
                print('Uau! Você é bom mesmo! O HP dele agora é igual a 0, você venceu!')
                break
            else: 
                print('O HP dele agora é igual a 50!\n')
                sleep(1.9)
        else:
            print(f'{cores["vermelho em negrito"]}Ops! Você errou, vez do outro jogador{cores["limpa"]}')
            sleep(1.9)
    else:
        p2 = posição('Ok! Escolha sua nova posição: ', nome2)
    sleep(2)
    clearConsole()
