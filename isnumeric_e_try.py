"""
num1 = input('Digite um Número: ')
num2 = input('Digite outro Número: ')

# isnumeric, isdigit, isdecimal - estas funções retornam se o valor da variável é um numero

print()
print(num1.isnumeric())
print(num2.isdecimal())
"""

#exemplo de calculadora, verificando se é digitado apenas numeros

num1 = input('Digite um Número: ')
num2 = input('Digite outro Número: ')

#try = tenta executar o bloco, se ocorrer erro ele pula para o except
try:
    num1 = float(num1)
    num2 = float(num2)

    print(num1 + num2)
except:
    print('Digite apenas números')