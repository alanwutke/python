"""
Operador ternário 
"""

# if padrão

logged_user = False

if logged_user:
    msg = 'Usuário logado'
else:
    msg = 'Usuário precisa fazer login'

print(msg)

# Operador ternário
logged_user = True
msg = 'Usuário logado.' if logged_user else 'Usuário precisa fazer login.'

print(msg)

##################################
idade = 18

# modo padrao
if idade >= 18:
    print('Acesso OK.')
else:
    print('Acesso negado.')

# ternario
maior = (idade >= 18)
msg = 'Acesso OK.' if maior else 'Acesso negado.'
print(msg)

idade = input('Digite a idade: ')
if not idade.isnumeric:
    print('Digite apenas numeros')
else:
    idade = int(idade)
    maior = (idade >= 18)
    msg = 'Acesso OK.' if maior else 'Acesso negado.'
    print(msg)