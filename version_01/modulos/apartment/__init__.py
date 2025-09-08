from version_01.modulos.tests import leiaInt, leiaStr
from version_01.modulos.interface import linha


def cadastrar_apartamento(list):
    dado_ap = dict()
    dado_ap['nome_ap'] = leiaStr('Digite o nome do apartamento: ')
    dado_ap['quant_quarto'] = leiaInt('Digite a quantidade de quartos: ')
    dado_ap['quant_cozinha'] = leiaInt('Digite a quantidade de cozinhas: ')
    dado_ap['quan_banheiro'] = leiaInt('Digite a quantidade de banheiros: ')
    dado_ap['quan_cama'] = leiaInt('Digite a quantidade de camas: ')
    if dado_ap['quan_cama'] > 0:
        for i in range(dado_ap['quan_cama']):
            dado_ap['tipo_cama'] = leiaStr(f'Digite o tipo da {i+1} cama: ')
    list.append(dado_ap.copy())
    print('Apartamento cadastrado com sucesso!')
    return list

def exibir_apartamentos(list):
    print(f'{"Numero"}{"Apartamento":>20}')
    print(linha())
    for pos, dado in enumerate(list):
        print(f'  {pos + 1:<13}{dado["nome_ap"]:<26}')


def excluir_apartamento(list):
    exibir_apartamentos(list)
    opcao = leiaInt("Digite o número do apartamento que deseja excluir: ")
    opcao -= 1
    for pos, dado in enumerate(list):
        if opcao == pos:
            list.pop(opcao)
            print(f'Apartamento {dado["nome_ap"]} Removido com sucesso!')
            break


def editar_apartamento_completo(list, posicao):
    dado_ap = dict()
    dado_ap['nome_ap'] = leiaStr('Digite o nome do apartamento: ')
    dado_ap['quant_quarto'] = leiaInt('Digite a quantidade de quartos: ')
    dado_ap['quant_cozinha'] = leiaInt('Digite a quantidade de cozinhas: ')
    dado_ap['quan_banheiro'] = leiaInt('Digite a quantidade de banheiros: ')
    dado_ap['quan_cama'] = leiaInt('Digite a quantidade de camas: ')
    if dado_ap['quan_cama'] > 0:
        for i in range(dado_ap['quan_cama']):
            dado_ap['tipo_cama'] = leiaStr(f'Digite o tipo da {i + 1} cama: ')
    list[posicao] = dado_ap.copy()
    print('Apartamento Editado com sucesso!')
    return list