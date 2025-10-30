def leiaInt(msg):
    # Ler um número inteiro, caso não seja, exibe uma mensagem de erro.
    while True:
        try:
            num = int(input(msg))
        except:
            print('ERRO! DIGITE UM VALOR VÁLIDO.')
            print('-' * 50)
        else:
            # Caso seja um número menor do que 0 ou maior do que 10, também será exibido uma mensagem de erro.
            if num < 0 or num > 10:
                print('ERRO! DIGITE UM VALOR VÁLIDO.')
                print('-' * 50)
            else:
                # Retornar a variável caso nenhum erro ocorra.
                return num


def resultado(num_usu, num_com, cont_erros):
    res = ''
    # Verifica se o usúario acertou ou errou. Caso tenha errado o programa irá dizer se é maior que o valor digitado ou menor que o valor digitado.
    if num_usu < num_com:
        print('Mais... Tente mais uma vez.')
        print('-' * 50)
    elif num_usu > num_com:
        print('Menos... Tente mais uma vez.')
        print('-' * 50)
    else:
        # Caso acerte, uma mensagem de comemoração será exibida junto com as tentativas necessárias para o acerto.
        if cont_erros == 1:
            print(f'Acertou com {cont_erros} tentativa. Parabéns!')
        else:
            print(f'Acertou com {cont_erros} tentativas. Parabéns!')
        print('-' * 50)
        # Pergunta se usúario quer continuar, se sim, o programa continua, se não, ele termina.
        while res not in ('S', 'N'):
            res = str(input('Quer continuar [S/N]? ')).strip().upper()
            if res not in ('S', 'N'):
                print('ERRO! OPÇÃO INVÁLIDA.')
                print('-' * 50)
            else:
                return res
