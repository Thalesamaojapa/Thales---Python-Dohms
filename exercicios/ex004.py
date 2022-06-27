listas = [[1, 2, 3, 4, 5, 7], [1, 3, 65, 1]]
for lista in listas:
    if lista[0] == lista[-1]:
       print('Os últimos números são iguais')
       print(lista[0], lista[-1])
    else:
        print('Os últimos números são diferentes')
        print(lista[0], lista[-1])
