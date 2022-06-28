''''''
#escreva um programa que calcule o preço a pagar pelo fornecimento de energia eletrica.
#pergunte a quantidade de kWa consumido eo tipo de instalação: r para resendencial, i para industria e c para comercio.
#calcule o preço a pagar de acordo com a tabela a seguir

consumo = int(input('quantos foi consumido de kWa: '))
tipo = input('qual é tipo de instalação(r,c ou i): ')

if tipo == 'r':
     if consumo <= 500:
        preço = 0.40
     else:
        preço = 0.65

elif tipo == 'c':
    if consumo <= 1000:
        preço =   0.55
    else:
        preço =   0.60

elif tipo == 'i':
    if consumo <= 5000:
        preço =  0.60
    else:
        preço =   0.65
else:
    preço = 0
    print('resultado não encontrado: ')

custo = consumo * preço
print(f'valor a pagar da conta será de:  {custo:7.2f}')

