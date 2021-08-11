l1 = ['Alan', 'Pri', 'Bia']

for valor in l1:
    if valor.startswith('A'):
        print(f'Começa com A: {valor}')
    else:
        print(f'Não começa com A: {valor}')

# for com else

for valor in l1:
    print(valor)
    if valor.lower().startswith('a'):
        break
else:
    print('Não existe palavra com A.')
