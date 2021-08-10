numero = 0
while numero < 100:
    print(numero)
    numero += 1 

print(f'{numero} Acabou')


# exemplo 2

x = 0
while x < 10:
    y = 0
    while y < 5:
        print(f'({x},{y})')
        y += 1
    x += 1
print('Acabou')

# exemplo calculadora

while True:
    print()
    num_1 = input('Digite um número: ')
    operador = input('Digite um operador: ')
    num_2 = input('Digite um número: ')

    if not num_1.isnumeric or not num_2.isnumeric:
        print('Digite apenas números')
        continue
    
    num_1 = int(num_1)
    num_2 = int(num_2)

    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '/':
        print(num_1 / num_2)
    elif operador == '*':
        print(num_1 * num_2)
    else:
        print('Digite um operador válido')
    
    sair = input('Deseja sair? [s]im ou [n]ão ')
    if sair == 'S':
        break