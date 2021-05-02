dis = int(input('Digite a distancia da sua viagem ? '))
if dis <= 200:
    km = dis * 0.50
else:
    km = dis * 0.45
print(f'Calculando o km {dis} que você digitou, a viagem vai custar {km} reais')
