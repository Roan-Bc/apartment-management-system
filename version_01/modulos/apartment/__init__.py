from version_01.modulos.tests import leiaInt, leiaStr


def cadastrar_apartamento(list):
    dado_ap = dict()
    dado_ap['nome_ap'] = leiaStr('Digite o nome do apartamento: ')
    dado_ap['quant_quarto'] = leiaInt('Digite a quantidade de quartos: ')
    dado_ap['quant_cozinha'] = leiaInt('Digite a quantidade de cozinhas: ')
    dado_ap['quan_banheiro'] = leiaInt('Digite a quantidade de banheiros: ')
    dado_ap['quan_cama'] = leiaInt('Digite a quantidade de camas ')
    if dado_ap['quan_cama'] > 0:
        for i in range(dado_ap['quan_cama']):
            dado_ap['tipo_cama'] = leiaStr(f'Digite o tipo da {i+1} cama: ')
    list.append(dado_ap.copy())
    return list

def exibir_apartamentos(list):
    print(f'{"Numero":<3}{"Nome Apartamento":>20}')
    for pos, dado in enumerate(list):
        print(f'{pos + 1:<3}{dado["nome_ap"]:>20}')

"""
def excluir_apartamento():
"""