v = float(input('Digite a velocidade que esta agora: '))

if v >= 81:
    print(f'Voce esta acima do limite permitido ')
km = (v - 80) * 7
print(f'Você esta recebendo uma multa de {km}')

