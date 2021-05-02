import random

total_de_tentativas = 0
numero_computador = random.randrange(1,10)
p = 1
print("Sou seu computador...")
print("Acabei de pensar em um numero entre 0 e 10, Sera que voce consegue adivinhar qual foi ?")

acertou = False
while not acertou:
    total_de_tentativas += 1
    p = int(input("Digite seu palpite: "))

    if p == numero_computador:
        acertou = True

    else:
        if p < numero_computador:
            print('Mais... Tente mais uma vez')
        elif p > numero_computador:
         print('Menos... Tente mais uma vez')
print("Acertou com {} tentativas. Parabéns".format(total_de_tentativas))
