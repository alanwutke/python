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
print('--------------------')

num1 = 1
print(f'{num1:0>10}') # Adiciona 0 a esquerda para completar 10 numeros

num2 = 1150
print(f'{num2:0<10}') # adiciona 0 a direita para completar 10 numeros

num2 = 1150
print(f'{num2:0^10}') # adiciona 0 a direita e esquerda para completar 10 numeros e o numero fica no centro

num2 = 1150
print(f'{num2:.2f}') # Convertendo inteiro para float no print

num2 = 1150
print(f'{num2:0>10.2f}') # Convertendo inteiro para float no print e adicionando 0 a esquerda

print(nome.lower()) # tudo minusculo
print(nome.upper()) # tudo maiusculo
print(nome.title()) # Primeiras letras maiusculas