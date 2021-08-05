num1 = input('Digite um número inteiro: ')


if num1.isnumeric():
    
    num1 = int(num1)
    
    if (num1%2) == 0:
        print('Este número é par')
    else:
        print('Número impar')
else:
    print('Digite apenas números inteiros')

print()
print('-----------------')
print()

