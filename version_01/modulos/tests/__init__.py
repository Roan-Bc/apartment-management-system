def leiaInt(valor):
    """
    -> Função para validar o input de um número do tipo inteiro
    :param valor: uma string digitada pelo usuário
    :return: um valor int
    """
    while True:
        try:
            v = int(input(valor))
        except (ValueError, TypeError):
            print(f'ERRO: por favor, digite um número interio válido.')
            continue
        except KeyboardInterrupt:
            print(f'\nO usuário preferiu não informar os dados.')
        else:
            return v

def leiaStr(txt):
    caracteres_invalidos = """!@#$%^&*()_+=[]{}|\/:;"'<>,.?`~"""
    while True:
        vT = str(input(txt))
        if not vT.isdecimal():
            if not any(c in caracteres_invalidos for c in vT):
                return vT
        else:
            print(f'{vT} Não é um nome válido, digite novamente!')