from random import randint

rand = randint(1, 10)
escolha = 0
while escolha != rand: 
    escolha = int(input('Escolha um número de um até dez: '))
    if rand == escolha:
        print('Parabéns! Você acertou o número!\n')
        exit()
    else:
        print('Você errou, tente novamente!\n')