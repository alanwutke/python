nome = input('Qual o seu nome? ')

if nome:
    print(nome)
else:
    print('Digite alguma coisa')

# operador OR - menos linhas e mesmo resultado
print(nome or 'Digite alguma coisa')