N = 0
digitou = 0
soma = 0
N = int(input("Digite um número [999 para parar]: "))
while N != 999:
        if N == 999:
                break        
        soma += N
        digitou += 1
        N = int(input("Digite um número [999 para parar]: "))
print(f"Você digitou {digitou} números e a  soma entre eles foi {soma}")