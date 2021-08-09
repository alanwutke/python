"""
Faça um programa que peça ao usuáriopara digitar um número inteiro, informe se o número é par ou ímpar.
Caso o usuário não digite un número inteiro, informe que não é um número inteiro.
"""
print()
num1 = input('Digite um número inteiro: ')
print()

if num1.isnumeric():
    num1 = int(num1)
    if (num1%2) == 0:
        print(f'O número {num1} é par')
    else:
        print(f'O número {num1} é impar')
else:
    print('Digite apenas números inteiros')
print()
print('------------------')
print()
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada. Ex Bom dia 0-11, Boa tarde 12-17 e Boa Noite 18-23
"""
hora = input('Informe a Hora atual: ')
if hora.isnumeric():
    hora = int(hora)
    if (hora < 0 or hora > 23):
        print('Digite um horario entre 0-23')
    elif (hora >= 0 and hora <= 11):
        print('Bom dia')
    elif (hora >= 12 and hora <=17):
        print('Boa tarde!')
    else:
        print('Boa Noite!')
else:
    print('Digite um horario entre 0-23')
print()

print()
print('-----------------')
print()

"""
Faça programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto", se tiver entre 5 e 6 letras escreva "Seu nome é normal".
Se tiver 6 letras ou mais escreva "Seu nome é grande"
"""

nome = input('Digite seu nome: ')

if (len(nome) <= 4):
    print('Seu nome é curto!')
elif (len(nome) >= 5 and len(nome) <= 6):
    print('Seu nome é normal')
else:
    print('Seu nome é Muito grande!')
print()