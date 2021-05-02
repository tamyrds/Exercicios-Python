maior = 0
menor = 0

for cont in range(1,6):
    peso =float (input(f"Peso da {cont} pessoa: "))
    if cont ==1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso


print("Maior número da lista: {}".format(maior))
print("Menor número da lista: {}".format(menor))