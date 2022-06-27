palavras = ['abacate', 'banana', 'limao', 'melancia', 'morango']
final = []


for item in palavras:
    palavra = ''
    inversa = []
    for cont in range(1, len(item)):
        inversa.append(item[(cont * -1)])
    inversa.append(item[0])
    for letra in inversa:
        palavra += letra
    final.append(palavra)


print(final)