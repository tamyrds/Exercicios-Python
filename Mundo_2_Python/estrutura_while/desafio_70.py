maior  = totH = totM = 0
print('=-' * 20)
print("CADASTRE UMA PESSOA")
print('=-' * 20)

while True:
    idade = int(input("Idade:"))
    sexo = str(input("Sexo: ")).upper()
    
    if idade >= 18:
         maior +=1
    if sexo == 'M':
        totH += 1
                
    if  idade < 20 and sexo == 'F':
        totM +=1
        
    tipo = ' '
    while tipo not in 'SN':
            tipo = str(input("Quer continuar? [S/N]")).upper()
    if tipo == 'N':
        break
print(f"Total de pessoas com mais de 18 anos: {maior}")
print(f'Ao todo temos {totH} homens cadastrados')
print(f'E temos {totM} mulheres com menos de 20 anos')
       
print('=-' * 20)  
  

   
    
    