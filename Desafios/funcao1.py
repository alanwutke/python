# Crie uma função que exibe uma saudação, com os parâmetros saudação e nome.

def saudacao(s, n):
    print(s,n)

saudacao('Bom dia', 'Alan')

# Crie uma função que recebe 3 números como parametros, e exiba a soma entre eles

def soma(n1, n2, n3):
    print(n1 + n2 + n3)
    
soma(2, 2, 0)
    
# Crie uma função que receba 2 numeros. O primeiro é um valor e o segundo é %. 
# Retorne o valor do primeiro número somado do aumento do percentual do mesmo

def numeros(n1, n2):
    return ((n2/100) * n1)+ n1

valor = numeros(3256,15.5)

print(valor)

# Se o parametro da função for divisível por 3, retorne fizz
# Se o parametro da função for divisivel por 5, retorn buzz
# Se o parametro da função for divisivel por 5 e por 3, retorne FizzBuzz
# Caso contrário, retorno o número enviado

# Alan fez:

def numero(n1):
    if n1 % 5 == 0 and n1 % 3 == 0:
        return 'FizzBuzz'
    elif n1 % 5 == 0:
        return 'Buzz'
    elif n1 % 3 == 0:
        return 'Fizz'
    else:
        return n1

print(numero(15))

# Orientação professor:

def numero(n1):
    if n1 % 5 == 0 and n1 % 3 == 0:
        return f'{n1} é divisível por 5 e 3.'
    if n1 % 5 == 0:
        return f'{n1} é divisível por 5.'
    if n1 % 3 == 0:
        return f'{n1} é divisível por 3.'
    return f'{n1} não é divisível.' 

#gerando números aleatórios para teste:

from random import randint

for i in range(100):
    aleatorio = randint(0,100)
    print(numero(aleatorio))