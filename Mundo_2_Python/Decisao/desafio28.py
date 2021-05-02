import random
num = int(input('Digite um número: '))
print("PROCESSANDO...")
adv = random.randint(0,5)

if num == adv:
    print('Voce acertou o número')
else:
    print(f'Voce não acertou e o número correto é {adv}')