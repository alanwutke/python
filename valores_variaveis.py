# invertendo valores de variáveis
# modo padrão:

x = 10
y = 'Luiz'

z = x
x = y
y = z

print(f'x={x} e y={y}')

# no Python

x = 10
y = 'Luiz'

x, y = y, x
print(f'x={x} e y={y}')