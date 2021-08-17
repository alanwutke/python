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
    calculo = ((n2/100) * n1)+ n1
    return calculo

valor = numeros(3256,15.5)

print(valor)

# Se o parametro da função for divisível por 2, retorne fizz
# Se o parametro da função for divisivel por 5, retorn buzz
# Se o parametro da função for divisivel por 5 e por 3, retorne FizzBuzz
# Caso contrário, retorno o número enviado


def numero(n1):
    if n1 % 2 == 0:
        resultado = 'Fizz'
        return resultado
    elif n1 % 5 == 0:
        resultado = 'Buzz'
        return resultado
    elif n1 % 5 == 0 and n1 % 3 == 0:
        resultado = 'FizzBuzz'
        return resultado
    else:
        resultado = n1
        return resultado



n1 = numero(2577)

print(n1)

