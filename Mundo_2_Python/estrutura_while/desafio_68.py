
while True:   
    num = int(input("Quer ver a tabuado de qual número ?"))
    if num <0:
        break
    
    for cont in range(1,11):
    
        print(f'{num} X {cont} = {num*cont}')
print('NUMERO INVALIDO')
    
     
