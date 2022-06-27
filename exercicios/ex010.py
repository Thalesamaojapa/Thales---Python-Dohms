limite = int(input('Digite o limite: '))
tot = 0
primos = []


for num in range(1, limite + 1):
    for cont in range(1, num + 1):
        if num % cont == 0:
            tot += 1
    if tot == 2:
        primos.append(num) 
    tot = 0
print(primos)