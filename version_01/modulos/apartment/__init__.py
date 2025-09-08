from version_01.modulos.tests import leiaInt, leiaStr
from version_01.modulos.interface import linha, cabecalho
import json

CAMINHO_JSON = "dados/cadastro.json"

def carregar_apartamentos():

    try:
        with open(CAMINHO_JSON, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def salvar_apartamentos(lista_apartamentos):

    with open(CAMINHO_JSON, "w", encoding="utf-8") as file:
        json.dump(lista_apartamentos, file, indent=4, ensure_ascii=False)



def cadastrar_apartamento():
    lista_apartamentos = carregar_apartamentos()

    dado_ap = dict()
    dado_ap['nome_ap'] = leiaStr('Digite o nome do apartamento: ')
    dado_ap['quant_quarto'] = leiaInt('Digite a quantidade de quartos: ')
    dado_ap['quant_cozinha'] = leiaInt('Digite a quantidade de cozinhas: ')
    dado_ap['quant_banheiro'] = leiaInt('Digite a quantidade de banheiros: ')
    dado_ap['quant_cama'] = leiaInt('Digite a quantidade de camas: ')

    if dado_ap['quant_cama'] > 0:
        tipos = []
        for i in range(dado_ap['quant_cama']):
            tipos.append(leiaStr(f'Digite o modelo da {i + 1}ª cama: '))
        dado_ap['tipo_cama'] = tipos

    lista_apartamentos.append(dado_ap)
    salvar_apartamentos(lista_apartamentos)
    print(linha())
    print('Apartamento cadastrado com sucesso!')
    print(linha())


def exibir_apartamentos():
    lista_apartamentos = carregar_apartamentos()

    print(f'{"Numero"}{"Apartamento":>20}')
    print(linha())
    for pos, dado in enumerate(lista_apartamentos):
        print(f'  {pos + 1:<13}{dado["nome_ap"]:<26}')


def exibir_detalhes_apartamento(pos):
    lista_apartamentos = carregar_apartamentos()
    dado = lista_apartamentos[pos]
    tamanho = (len(dado['nome_ap'])) + 4
    if dado['quant_cama'] > 0:
        tipos = ', '.join(dado["tipo_cama"])
    else:
        tipos = 'N/A'
    cabecalho('Informações detalhadas do apartamento')
    print(f'{"Nome":<{tamanho}}{"Quarto":<7} {"Cozinha":<7} {"Banheiro":<7} {"Camas":<7} {"Modelo_Cama":<7}')
    print(linha())
    print(f'{dado["nome_ap"]:<{tamanho}} {dado["quant_quarto"]:<7} {dado["quant_cozinha"]:<7} {dado["quant_banheiro"]:<7} {dado["quant_cama"]:<7} {tipos:<7}')



def excluir_apartamento(pos):
    lista_apartamentos = carregar_apartamentos()
    print(linha())
    print(f'Apartamento {lista_apartamentos[pos]["nome_ap"]} Removido com sucesso!')
    print(linha())
    lista_apartamentos.pop(pos)
    salvar_apartamentos(lista_apartamentos)





def editar_todo_apartamento(posicao):
    lista_apartamentos = carregar_apartamentos()
    apartamento = dict()
    apartamento['nome_ap'] = leiaStr('Digite o nome do apartamento: ')
    apartamento['quant_quarto'] = leiaInt('Digite a quantidade de quartos: ')
    apartamento['quant_cozinha'] = leiaInt('Digite a quantidade de cozinhas: ')
    apartamento['quant_banheiro'] = leiaInt('Digite a quantidade de banheiros: ')
    apartamento['quant_cama'] = leiaInt('Digite a quantidade de camas: ')

    if apartamento['quant_cama'] > 0:
        tipos = []
        for i in range(apartamento['quant_cama']):
            tipos.append(leiaStr(f'Digite o modelo da {i + 1}° cama: '))
        apartamento['tipo_cama'] = tipos[:]

    lista_apartamentos[posicao] = apartamento.copy()
    print(linha())
    print('Apartamento Editado com sucesso!')
    print(linha())
    salvar_apartamentos(lista_apartamentos)

def editar_dado_apartamento(pos, chave, txt):
    lista_apartamentos = carregar_apartamentos()
    if chave == 'quant_cama':
        lista_apartamentos[pos][chave] = leiaInt('Digite a quantidade de camas: ')
        if lista_apartamentos[pos][chave] > 0:
            tipos = []
            for i in range(lista_apartamentos[pos][chave]):
                tipos.append(leiaStr(f'Digite o modelo da {i + 1}° cama: '))
            lista_apartamentos[pos]['tipo_cama'] = tipos[:]

    elif chave == 'tipo_cama':
        tipos = []
        for i in range (lista_apartamentos[pos]['quant_cama']):
            tipos.append(leiaStr(f'Digite o modelo da {i + 1}° cama: '))
        lista_apartamentos[pos][chave] = tipos[:]

    elif chave == 'nome_ap':
        lista_apartamentos[pos][chave] = leiaStr(f'Digite o {txt}: ')
    else:
        lista_apartamentos[pos][chave] = leiaInt(f'Digite a {txt}: ')

    print(linha())
    print('Apartamento editado com sucesso!')
    print(linha())
    salvar_apartamentos(lista_apartamentos)
