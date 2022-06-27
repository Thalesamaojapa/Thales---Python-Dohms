lista = [1, 6, 8, 0, 10, 2, 5, 7, 3, 9, 4]
lista.sort()
c = 0
for n in range(0, len(lista)):
    c += 1
    if  n == 0:
        print(f'A {c}º soma é {lista[n]}')
    else:
        print(f'A {c}º soma é {lista[n] + lista[n - 1]}')