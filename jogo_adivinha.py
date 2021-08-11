secreto = 'perfume'
digitadas = []
chance = 10


while True:
    if chance <= 0:
        print('Suas chances terminaram')
        break
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Digite apenas uma letra')
        continue
    
    digitadas.append(letra)

    if letra in secreto:
        print(f'Ok, a letra {letra} existe')
    else:
        print(f'A letra {letra} não existe! Tente novamente')
        chance -= 1
        digitadas.pop()
    
    secreto_temp = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temp += letra_secreta
        else:
            secreto_temp += '*'
        
    if secreto_temp == secreto:
        print(f'Parabens!! Você acertou a palavra, que era {secreto_temp}')
        break
    else:
        print(secreto_temp)
    
    if chance > 0:
        print(f'Você ainda tem {chance} chances.')