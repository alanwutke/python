# Split - Dividir um string 


string = 'O Brasil é o Pais do futebol, o Brasil é penta.'
lista1 = string.split(' ')
lista2 = string.split(',')

print(lista1)
print(lista2)

# contando as palavras:
for valor in lista1:
    print(f'A palavra {valor} apareceu {lista1.count(valor)}x na frase.' )

palavra = ''
contagem = 0
for valor in lista1:
    qtd_vezes = lista1.count(valor)
    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor
print(f'A palavra que apareceu mais vezes é "{palavra}" ({contagem}x)')

for valor in lista2:
    print(valor.strip().capitalize()) # strip() tira espaços em branco no começo e fim, capitalize() a 1ª letra fica maiúscula