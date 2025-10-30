# Importando minhas funções
import jogo
# Importando a função randint para que eu possa gerar um número entre 0 e 10.
from random import randint
# Loop infinito.
while True:
    # Escolhendo o número de maneira aleátoria.
    numero_escolhido = randint(0, 10)
    # Contagem de erros do usúario.
    erro = 1
    # Menu
    print('-' * 50)
    print('ADVINHE O NÚMERO'.center(50))
    print('-' * 50)
    print('Acabei de pensar em um número entre 0 e 10.')
    print('Será que você consegue adivinhar qual foi?')
    print('-' * 50)
    # Loop infinito
    while True:
        # Chamando as funções.
        n = jogo.leiaInt('Qual é o seu palpite? ')
        usu_res = jogo.resultado(n, numero_escolhido, erro)
        # Quebra o primeiro loop.
        if usu_res in ('S', 'N'):
            break
        # Caso o usúario erre o contador de erros aumenta em 1.
        else:
            erro += 1
    # Quebra o segundo loop.
    if usu_res in 'N':
        break
# Fim
print('-' * 50)
print('OBRIGADO POR USAR O MEU ADIVINHADOR DE NÚMERO'.center(50))
print('-' * 50)
