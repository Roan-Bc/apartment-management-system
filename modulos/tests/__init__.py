def leiaInt(valor):
    """
    -> Função para validar o input de um número do tipo inteiro
    :param valor: uma string digitada pelo usuário
    :return: um valor int ou 3 se o programa for iterrompido
    """
    while True:
        try:
            v = int(input(valor))
        except (ValueError, TypeError):
            print(f'ERRO: por favor, digite um número interio válido.')
            continue
        except KeyboardInterrupt:
            print(f'\nO usuário preferiu não informar os dados.')
            return 3
        else:
            return v