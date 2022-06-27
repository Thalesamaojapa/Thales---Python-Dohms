from time import sleep

def linha(num, cor):
    print(f'{cor}=-\033[m' * num)

def clearConsole(): #função que limpa o terminal, peguei da net delftstack.com
    import os
    comando = 'clear'
    if os.name in ('nt', 'dos'):
        comando = 'cls'
    os.system(comando)

def posição(msg, jogador):
    while True:
        try:
            valor = int(input(f'{msg}, {jogador}: '))
        except:
            print('Só são aceitos valores entre 1 e 10, tente novamente!')
        else:
            if valor <= 0 or valor > 10:
                print('Só são aceitos valores entre 1 e 10, tente novamente!')
            else:
                print(f'Posição definida! Sua posição: {valor}')
                return valor

def ataque(jogador):
    while True:
        alvo = int(input(f'{jogador}, escolha uma posição de -2 até 13 para disparar uma flecha: '))
        if alvo < -2 or alvo > 13:
            print('Só são aceitos valores entre -2 e 13, tente novamente!')
        else:
            print(f'Alvo definido! Atirando no alvo...')
            sleep(1)
            return alvo