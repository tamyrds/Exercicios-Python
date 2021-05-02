valor_casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o seu salario: '))
quantos_anos = int(input('Digite em quantos anos você quer pagar a casa: '))


prestacao = valor_casa /(quantos_anos * 12)
minimo = salario * 30 / 100
print(f'Para pagar uma casa de R$ {valor_casa:.2f} em {quantos_anos} a prestação sera de R$ {prestacao:.2f}')
if prestacao <= minimo:
    print('Emprestimo pode ser concedido')
else:
    print('Emprestimo NEGADO')


