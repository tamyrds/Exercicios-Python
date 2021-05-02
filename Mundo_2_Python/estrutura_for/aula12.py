nome = str(input('Qual é seu nome? '))
if nome == 'Tamires':
    print('Que nome bonito')
elif nome == 'Kaique' or nome == 'Ana' or nome =='Ivonete' or nome =='Pedro':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Belo nome feminino')
else:
    print(f'Seu nome é normal!')
    print(f'tenha um bom dia {nome}!!')
