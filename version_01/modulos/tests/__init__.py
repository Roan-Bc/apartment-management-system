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
    caracteres_invalidos = r"""!@#$%^&*()_+=[]{}|\/:;"'<>,.?`~"""
    while True:
        vT = str(input(txt))
        if not vT.isdecimal():
            if not any(c in caracteres_invalidos for c in vT):
                return vT
        else:
            print(f'{vT} Não é um nome válido, digite novamente!')


def verifica_Email(email):
    #Função no momento está incompleta, mas vai servir para fazer os testes minimos dentro das funções.
    while True:
        test_email = str(input(email))
        if "@" in test_email and "." in test_email.split("@")[-1]:
            return test_email
        else:
            print('E-mail inválido, digite novamente!')

def verifica_Telefone(telefone):
    # Função no momento está incompleta, mas vai servir para fazer os testes mínimos dentro das funções.
    formato = '54111512345678'
    while True:
        test_numero = str(input(telefone))
        if len(test_numero) <= len(formato) and test_numero.isdecimal():
            return test_numero
        else:
            print('Número de telefone inválido, digite novamente!')


def verifica_idFiscal(pais='Brasil'):

    match pais:

        case 'Brasil':
            id = 'CPF'
            doc = verificaDoc(id)
            return [id, doc]
        case 'Argentina':
            id = 'CUIT'
        case 'Uruguai':
            id = 'RUT'
        case 'Paraguai':
            id = 'RUC'
        case 'Chile':
            id = 'RUT '
        case 'Estados Unidos':
            id = 'SSN'
        case 'Alemanha':
            id ='IdNr'
        case 'Reino Unido':
            id = 'NIN'
        case 'França':
            id = 'NFR'
        case 'Itália':
            id = 'CF'



def verificaDoc(id):
    match id:

        case 'CPF':
            formato = '00000000000'
            while True:
               doc = str(input(f'Digite seu {id} nesse formato "{formato}": '))
               if doc.isdecimal() and len(doc) == len(formato):
                   return doc
               else:
                    print(f'{id} inválido, por favor, digite novamente!')


    """
        case 'CUIT':

        case 'RUT':

        case 'RUC':

        case 'RUT ':

        case 'SSN':

        case 'IdNr':

        case 'NIN':

        case 'NFR':

        case 'CF':
    """