num = float(input('Digite o seu salario: '))
if num > 1250.00:
    aumento = num + (num / 100) * 10
    print(aumento)
else:
    aumento = num + (num / 100) * 15
    print(aumento)