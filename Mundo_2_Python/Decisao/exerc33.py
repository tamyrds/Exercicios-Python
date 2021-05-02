num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
num3 = int(input('Digite o terceiro valor: '))
#Testando o maior
maior = num1
if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3
  

#Testado menor

m = num1
if num2 < m:
    m = num2
if num3 < m:
    m = num3

print(f'O numero maior é {maior}')
print(f'O número menor é {m}')