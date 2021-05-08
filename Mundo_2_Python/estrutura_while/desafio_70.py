tipo = 'S'
maior = 0
M= 0
F = 0
menor = 0
print('=-' * 20)
print("CADASTRE UMA PESSOA")
print('=-' * 20)

while tipo not in 'N':
    idade = int(input("Idade:"))
    sexo = str(input("Sexo: ")).upper()
    
    tipo = str(input("Quer continuar? [S/N]")).upper()
    
    if idade > 18:
        maior +=1
        sexo == M
        M +=1
        
    else:
        idade < 18
        menor +=1
        sexo == F
        print(f"Total de pessoas com mais de 18 anos: {maior}")
        print(f'Ao todo temos {M} homens cadastrados')
        print(f'E temos {menor} mulheres com menos de 20 anos')
       
print('=-' * 20)  
  

   
    
    