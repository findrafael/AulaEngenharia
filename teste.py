numero_texto = 50
numero = int(numero_texto)

print('-------------------------')
nome = input('Vamos ao teste, antes de comecarmos, insira seu nome: ')

print('Olá', nome, ', tudo bem?')
print('Tenho um número guardado em minha memória, tente adivinhar.')
chute = int(input('Para isso, digite um número: '))
print('-------------------------')
print("Você digitou o número:",chute)
if chute == numero:
    print('Show de bola', nome,', você acertou o número secreto!')
else:
    print('Poxa vida', nome, ', infelizmente você errou')
print('Obrigado por participar. Tchau!')
