frase = str(input('Digite uma frase: '))
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto) - 1,-1,-1):
    inverso += junto[letra]
print(junto,inverso)

if inverso == junto:
    print('Temos um palindromo')
else:
    print('A frase digitada não é um palindromo')