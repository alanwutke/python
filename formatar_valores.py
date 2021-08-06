# formatando valores numericos

# :s - Texto (string)
# :d - Inteiro (int)
# :f - Numeros de ponto flutuante
# :.(numero)f - Quantidade de casas decimais (float)
# :(caracter) (> ou < ou ^)(quantidade)(tipo - s, d ou f) 


num1 = 10
num2 = 3
divisao = num1 / num2

print( '{:.2f}'.format(divisao) )
print( f'{divisao:.2f}')

# formatando strings

nome = 'Alan Patrick Wutke'
print(f'{nome:s}')

print()
print('-------------------')

num1 = 1
print(f'{num1:0>10}')

num2 = 1150
print(f'{num2:0>10}')