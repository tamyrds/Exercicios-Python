n = soma = media = maior = menor = quant =  0

continuar = "S"
div = 0
while  continuar != "N":
    n = int(input("Digite um número? "))
    soma += n 
    quant += 1
    if quant ==1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    continuar = str(input("Quer continuar? [S/N]")).upper()
media = soma / quant   
print(f"Voce digitou {quant} e a media foi {media}")
print(f"O maior valor foi {maior} e o menor foi {menor}")