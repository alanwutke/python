"""
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
--aceitos:

booleanos = True
inteiros = 10
flutuante = 10.0
string = 'Texo'
"""

# lista = [1,2,3,4, 'Alan', True, '10.0']

lista = ['A', 'B', 'C', 'D', 'E']
print(lista[:3])
print("#####")
print(lista[1:5])
print('#######')
print(lista[-1]) # -1 irá trazer o último registro da lista
print('#######')
print(lista[::-1]) # irá inverter a lista e mostrar do último registro para o primeiro 
print()
print('#######')
print()

l1 = [1,2,3,4,5,6]
l2 = [7,8,9,10]
l3 = l1 + l2 # concatena as listas
l1.extend(l2)
l2.extend(['A', 'B'])
l2.append('C') # adiciona um registro no final da lista
l2.insert(2, 'Z') # adiciona um registro a lista, na indice informado - no caso o indice 2
l2.pop() # deleta o último registro da lista
del(l1[1:4]) # deleta registro de range de indices ou indice específico
print(l1)
print(l2)
print(l3)
print('Maximo: ', max(l1))
print('Minimo: ', min(l1))