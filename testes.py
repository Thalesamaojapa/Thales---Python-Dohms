from random import randint

vento = randint(0, 3)
direção = randint(1, 2)
if direção == 1:
    vento = vento * -1

print(vento, direção)