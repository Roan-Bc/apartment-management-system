from version_01.modulos.tests import leiaInt, leiaStr
from version_01.modulos.interface import linha, cabecalho


def cadastrar_apartamento(list):
    dado_ap = dict()
    dado_ap['nome_ap'] = leiaStr('Digite o nome do apartamento: ')
    dado_ap['quant_quarto'] = leiaInt('Digite a quantidade de quartos: ')
    dado_ap['quant_cozinha'] = leiaInt('Digite a quantidade de cozinhas: ')
    dado_ap['quant_banheiro'] = leiaInt('Digite a quantidade de banheiros: ')
    dado_ap['quant_cama'] = leiaInt('Digite a quantidade de camas: ')
    if dado_ap['quant_cama'] > 0:
        tipos = []
        for i in range(dado_ap['quant_cama']):
            tipos.append(leiaStr(f'Digite o modelo da {i+1} cama: '))
        dado_ap['tipo_cama'] = tipos[:]
    list.append(dado_ap.copy())
    print(linha())
    print('Apartamento cadastrado com sucesso!')
    print(linha())
    return list

def exibir_apartamentos(list):
    print(f'{"Numero"}{"Apartamento":>20}')
    print(linha())
    for pos, dado in enumerate(list):
        print(f'  {pos + 1:<13}{dado["nome_ap"]:<26}')


def exibir_detalhes_apartamento(list, pos):
    dado = list[pos]
    tamanho = (len(dado['nome_ap'])) + 4
    if dado['quant_cama'] > 0:
        tipos = ', '.join(dado["tipo_cama"])
    else:
        tipos = 'N/A'
    cabecalho('Informações detalhadas do apartamento')
    print(f'{"Nome":<{tamanho}}{"Quarto":<7} {"Cozinha":<7} {"Banheiro":<7} {"Camas":<7} {"Modelo_Cama":<7}')
    print(linha())
    print(f'{dado["nome_ap"]:<{tamanho}} {dado["quant_quarto"]:<7} {dado["quant_cozinha"]:<7} {dado["quant_banheiro"]:<7} {dado["quant_cama"]:<7} {tipos:<7}')

def excluir_apartamento(list):
    exibir_apartamentos(list)
    opcao = leiaInt("Digite o número do apartamento que deseja excluir: ")
    opcao -= 1
    for pos, dado in enumerate(list):
        if opcao == pos:
            print(linha())
            print(f'Apartamento {dado["nome_ap"]} Removido com sucesso!')
            list.pop(opcao)
            break
    return list


def editar_todo_apartamento(list, posicao):
    dado_ap = dict()
    dado_ap['nome_ap'] = leiaStr('Digite o nome do apartamento: ')
    dado_ap['quant_quarto'] = leiaInt('Digite a quantidade de quartos: ')
    dado_ap['quant_cozinha'] = leiaInt('Digite a quantidade de cozinhas: ')
    dado_ap['quant_banheiro'] = leiaInt('Digite a quantidade de banheiros: ')
    dado_ap['quant_cama'] = leiaInt('Digite a quantidade de camas: ')
    if dado_ap['quant_cama'] > 0:
        tipos = []
        for i in range(dado_ap['quant_cama']):
            tipos.append(leiaStr(f'Digite o modelo da {i + 1}° cama: '))
        dado_ap['tipo_cama'] = tipos[:]
    list[posicao] = dado_ap.copy()
    print(linha())
    print('Apartamento Editado com sucesso!')
    print(linha())
    return list

def editar_dado_apartamento(list, pos, key, txt):

    if key == 'quant_cama':
        list[pos][key] = leiaInt('Digite a quantidade de camas: ')
        if list[pos][key] > 0:
            tipos = []
            for i in range(list[pos][key]):
                tipos.append(leiaStr(f'Digite o modelo da {i + 1}° cama: '))
            list[pos]['tipo_cama'] = tipos[:]

    elif key == 'tipo_cama':
        tipos = []
        for i in range (list[pos]['quant_cama']):
            tipos.append(leiaStr(f'Digite o modelo da {i + 1}° cama: '))
        list[pos][key] = tipos[:]

    elif key == 'nome_ap':
        list[pos][key] = leiaStr(f'Digite o {txt}: ')
    else:
        list[pos][key] = leiaInt(f'Digite a {txt}: ')

    print(linha())
    print('Apartamento editado com sucesso!')
    print(linha())
    return list
