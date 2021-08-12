# Enumerate - Enumerar elementos da lista

string = 'O Brasil é penta.'
lista = string.split(' ')

for indice, valor in enumerate(lista):
    print(indice, valor)

lista = [
    [1,2],
    [3,4],
    [5,6],
    ]

for v in lista:
    print(v[0], v[1])

# enumrate - forma manual
lista2 = [
    [1,'Luiz'],
    [2,'Joao'],
    [3,'Maria'],
    ]

for indice, valor in lista2:
    print(indice, valor)

# forma enumerate
lista3 = ['Luiz', 'Joao', 'Maria']
for v1, v2 in enumerate(lista3):
    print(v1, v2)

l1 = [
    ['Edu', 'João', 'Maria'],
    ['Maria', 'Aline', 'Joana'],
    ['Helena', 'Ed', 'Lu'],
]
print()
# mostrar valor de lista dentro de lista
print(l1[1][2])
enumerada = enumerate(l1)
print(list(enumerada))