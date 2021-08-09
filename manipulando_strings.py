# positivos     [012345678]
texto       =   'Python s2'
# negativos     [987654321]

nova_string = texto[2:6] # vai imprimir o registro 2 ao 5
print(nova_string)

nova_string = texto[:6] # vai imprimir do primeiro registro ao 5
print(nova_string)

nova_string = texto[7:] # vai imprimir do 7º registro ate o final da frase
print(nova_string)

nova_string = texto[-1] # vai imprimir o último registro
print(nova_string)

nova_string = texto[0:7:2] # vai imprimir até o registro 7, pulando de 2 em 2
print(nova_string)

nova_string = texto[0::3] # vai imprimir todos os registros da frase, pulando de 3 em 3
print(nova_string)