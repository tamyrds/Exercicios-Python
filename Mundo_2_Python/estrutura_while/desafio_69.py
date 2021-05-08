import random


v = 0

print('=-' * 20)
print("VAMOS JOGAR PAR OU IMPAR")
print('=-' * 20)

print('-' * 20)

while True:
    num = int(input("Digite um valor: "))
    numero_computador = random.randrange(0,10)
    soma = num + numero_computador
    tipo = '  '
while tipo not in 'PI':
        tipo = str(input("Par ou ímpar? [P/I]")).strip().upper()[0]
print(f'Você jogou {num} e o computador {numero_computador}. Total de {soma}')
print('DEU PAR' if total % 2 ==0 else 'DEU IMPAR')        
if tipo == 'P':
    if total % 2 == 0:
        print("Voce VENCEU!")
        v +=1
    else:
        print('Voce PERDEU')
        break   
elif tipo == 'I':
    if total % 2 == 1:
        print("Voce VENCEU")
        v += 1
    else:
        print('Voce PERDEU')
        break
    print('Vamos jogar novamente')    
print(f'GAME OVER! Voce venceu {v} vezes')     
        
            
