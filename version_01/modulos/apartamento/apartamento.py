from version_01.modulos.testes import leiaInt, leiaStr
from version_01.modulos.interface import linha, cabecalho
import json

CAMINHO_JSON = "dados/lista_apartamentos.json"

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

    apartamento = dict()

    apartamento['nome_ap'] = leiaStr('Digite o nome do apartamento: ')
    apartamento['quant_quarto'] = leiaInt('Digite a quantidade de quartos: ')
    apartamento['quant_cozinha'] = leiaInt('Digite a quantidade de cozinhas: ')
    apartamento['quant_banheiro'] = leiaInt('Digite a quantidade de banheiros: ')
    apartamento['quant_cama'] = leiaInt('Digite a quantidade de camas: ')

    if apartamento['quant_cama'] > 0:
        modelo = []
        for i in range(apartamento['quant_cama']):
            modelo.append(leiaStr(f'Digite o modelo da {i + 1}ª cama: '))
        apartamento['tipo_cama'] = modelo

    lista_apartamentos.append(apartamento)
    salvar_apartamentos(lista_apartamentos)

    print(linha())
    print(f'{apartamento["nome_ap"]} cadastrado com sucesso!')
    print(linha())


def exibir_apartamentos():

    lista_apartamentos = carregar_apartamentos()

    tamanho = len(lista_apartamentos[0]['nome_ap'])
    for nome in lista_apartamentos:
        if len(nome['nome_ap']) >= tamanho:
            tamanho = len(nome['nome_ap']) + 4

    print(f'{"Numero":<{tamanho}}{"Apartamento":<{tamanho}}')
    print(linha())
    for pos, dado in enumerate(lista_apartamentos):
        print(f'{pos + 1:<{tamanho}}{dado["nome_ap"]:<{tamanho}}')


def exibir_detalhes_apartamento(pos):

    lista_apartamentos = carregar_apartamentos()
    apartamento = lista_apartamentos[pos]


    tamanho = len(lista_apartamentos[0]['nome_ap'])
    for nome in lista_apartamentos:
        if len(nome['nome_ap']) >= tamanho:
            tamanho = len(nome['nome_ap']) + 4

    if apartamento['quant_cama'] > 0:
        tipos = ', '.join(apartamento["tipo_cama"])
    else:
        tipos = 'N/A'

    cabecalho(f'Informações detalhadas do apartamento {apartamento["nome_ap"]}')
    print(f'{"Nome":<{tamanho}}{"Quarto":<{tamanho}}{"Cozinha":<{tamanho}}{"Banheiro":<{tamanho}}{"Camas":<{tamanho}}{"Modelo Cama":<{tamanho}}')
    print(linha())
    print(f'{apartamento["nome_ap"]:<{tamanho}}{apartamento["quant_quarto"]:<{tamanho}}{apartamento["quant_cozinha"]:<{tamanho}}{apartamento["quant_banheiro"]:<{tamanho}}{apartamento["quant_cama"]:<{tamanho}}{tipos:<{tamanho}}')


def editar_todo_apartamento(pos):

    lista_apartamentos = carregar_apartamentos()

    apartamento = dict()

    apartamento['nome_ap'] = leiaStr('Digite o nome do apartamento: ')
    apartamento['quant_quarto'] = leiaInt('Digite a quantidade de quartos: ')
    apartamento['quant_cozinha'] = leiaInt('Digite a quantidade de cozinhas: ')
    apartamento['quant_banheiro'] = leiaInt('Digite a quantidade de banheiros: ')
    apartamento['quant_cama'] = leiaInt('Digite a quantidade de camas: ')

    if apartamento['quant_cama'] > 0:
        modelo = []
        for i in range(apartamento['quant_cama']):
            modelo.append(leiaStr(f'Digite o modelo da {i + 1}° cama: '))
        apartamento['tipo_cama'] = modelo[:]

    lista_apartamentos[pos] = apartamento.copy()
    salvar_apartamentos(lista_apartamentos)

    print(linha())
    print(f'{apartamento["nome_ap"]} editado com sucesso!')
    print(linha())

def editar_dado_apartamento(pos, chave, txt):

    lista_apartamentos = carregar_apartamentos()
    apartamento = lista_apartamentos[pos]

    match chave:

        case 'nome_ap':
            apartamento[chave] = leiaStr(f'Digite o nome do apartamento: ')
        case 'quant_quarto':
            apartamento[chave] = leiaInt(f'Digite a quantidade de quartos: ')
        case 'quant_cozinha':
            apartamento[chave] = leiaInt(f'Digite a quantidade de quartos: ')
        case 'quant_banheiro':
            apartamento[chave] = leiaInt(f'Digite a quantidade de banheiro: ')
        case 'quant_cama':
            apartamento[chave] = leiaInt('Digite a quantidade de camas: ')
            if  apartamento[chave] > 0:
                modelo = []
                for i in range(apartamento[chave]):
                    modelo.append(leiaStr(f'Digite o modelo da {i + 1}° cama: '))
                lista_apartamentos[pos]['tipo_cama'] = modelo[:]
        case 'tipo_cama':
            if  apartamento['quant_cama'] > 0:
                modelo = []
                for i in range(apartamento['quant_cama']):
                    modelo.append(leiaStr(f'Digite o modelo da {i + 1}° cama: '))
                apartamento[chave] = modelo[:]


    lista_apartamentos[pos][chave] = apartamento[chave]
    salvar_apartamentos(lista_apartamentos)

    print(linha())
    print(f'{txt} do apartamento editado com sucesso!')
    print(linha())

def excluir_apartamento(pos):

    lista_apartamentos = carregar_apartamentos()

    print(linha())
    print(f'{lista_apartamentos[pos]["nome_ap"]} removido com sucesso!')
    print(linha())

    lista_apartamentos.pop(pos)
    salvar_apartamentos(lista_apartamentos)

