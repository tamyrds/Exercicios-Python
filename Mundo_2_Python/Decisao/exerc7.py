list_values = []
for i in range(1, 5):
    value = int(input(f"valor {i}: "))
list_values.append(value)

maior = menor = 0
for i, value in enumerate(list_values):

    if i == 0:
        maior = menor = value

    if value > maior:
        maior = value
        maxpos = i
        
    if value < menor:
        menor = value
        minPos = i
print("Lista: ", list_values)
print("Maior: ", maior, "posição", maxpos)
print("Menor: ", menor,"posição", minPos)