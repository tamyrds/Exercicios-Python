total = custa = cont = menor = 0
barato = ' '
print('=-' * 20)
print("LOJA SUPER BARATAO")
print('=-' * 20)

while True:
    nome_prod = str(input("Nome do Produto: "))
    preco = float(input("Preço: "))
    cont += 1
    total += preco 
        
    if preco >= 1000:
        custa +=1
    
    if cont == 1 or preco < menor:
        menor = preco
        barato = nome_prod
              
    resp = '  '
    while resp not in 'SN':
        resp= str(input("Quer continuar? [S/N]")).upper()[0]
    if resp == 'N':
        break
print('-'*10,"FIM DO PROGRAMA",'-' * 10)
print(f'O total da compra foi R$ {total:.2f}')
print(f'temos {custa} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi a {barato} que custa {menor}')