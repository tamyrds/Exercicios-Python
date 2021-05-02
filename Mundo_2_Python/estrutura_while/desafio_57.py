sexo = str(input('Digite seu sexo: ')).upper()
while sexo not in 'FfMm':
    sexo = str(input('Dados invalidos.  Por favor, digite seu sexo correto: ')).upper().strip()
print('Sexo {} registrado com sucesso'.format(sexo))   