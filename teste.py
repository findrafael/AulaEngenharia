numero_texto = 50
numero = int(numero_texto)

print('-------------------------')
print('Olá, Vamos ao teste')
print('Tenho um número guardado em minha memória, tente adivinhar.')
chute = int(input('Para isso, digite um número: '))
print('-------------------------')
print("Você digitou o número:",chute)
if chute == numero:
    print('Show de bola, você acertou o número secreto!')
else:
    print('Poxa vida, infelizmente você errou')
print('Obrigado por participar. Tchau!')
