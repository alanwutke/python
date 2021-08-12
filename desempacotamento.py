"""
Desempacotamento de listas em Python
"""

lista = ['Luiz', 'Joao', 'Maria',1,2,3,4,5,6,7,8,9,100] 

n1, n2, n3, *lista2, ultimo_da_lista = lista
print(n1, n2, n3, lista2, ultimo_da_lista)

lista2 = ['Luiz', 'Joao', 'Maria',1,2,3,4,5,6,7,8,9,100]
*lista3, n4, n5, n6,  = lista2