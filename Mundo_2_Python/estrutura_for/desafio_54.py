from datetime import datetime
now = datetime.now()
totmaior =0
totmenor =0

for cont in range(1,8):
    frase = int(input (f'Em que ano a {cont} pessoa nasceu ? '))

    idade = now.year - frase
    if idade >= 21:
        totmaior +=1
        
    else:
        totmenor +=1

print(f'Ao todo tivermos {totmaior} pessoas maiores de idade')
print(f'Ao todo tivermos {totmenor} pessoas menores de idade')