from random import randint
lista = []
num = str(randint(10000, 99999))
for cont in range(1, 6):
    lista.append(num[(cont) * (-1)])

print(num)
for i in lista:
    print(f'{i}', end='')