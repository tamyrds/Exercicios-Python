num1 = int(input("Primeiro valor: "))
num2 = int(input("Segundo valor: "))
escolha = 0

while escolha != 5:

    #Opções do menu
    escolha = int(input(">>>>>>> " "Qual é a sua opção: "))
    print("[1] somar")
    print("[2] multiplicar")
    print("[3] maior")
    print("[4] novos numeros")
    print("[5] sair do programa")

    if escolha == 1:
        escolha = num1 + num2
        print(f"A soma entre {num1} + {num2} é {escolha} ")
    elif escolha == 2:
        escolha = num1 * num2
        print (f"A multiplicação do {num1} * {num2} é {escolha}")
    elif escolha == 3:
        escolha = max(num1,num2)
        print(f"O número maior entre {num1} e {num2} é {escolha}" )
    elif escolha == 4:
        num1 = int(input("Primeiro valor: "))
        num2 = int(input("Segundo valor: "))
    elif escolha == 5:
        print("Você saiu do programa")
    else:
        print("Opção invalida. Tente novamente")

    print("=-==" * 10)
