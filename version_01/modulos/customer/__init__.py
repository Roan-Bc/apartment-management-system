from unittest import case

from version_01.modulos.tests import *
from version_01.modulos.interface import linha, cabecalho
import json

CAMINHO_JSON = "dados/lista_clientes.json"

def carregar_clientes():

    try:
        with open(CAMINHO_JSON, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def salvar_clientes(lista_clientes):

    with open(CAMINHO_JSON, "w", encoding="utf-8") as file:
        json.dump(lista_clientes, file, indent=4, ensure_ascii=False)


def cadastrar_cliente():
    lista_clientes = carregar_clientes()

    cliente = dict()

    cliente['nome'] = leiaStr("Digite o seu nome completo: ")
    cliente['pais'] = leiaStr("Digite seu pais: ")
    cliente['estado'] = leiaStr("Digite seu estado: ")
    cliente['endereco'] = leiaStr("Digite seu endereco: ")
    cliente['id_fiscal'] = verifica_idFiscal(cliente['pais'])
    cliente['numero_telefone'] = verifica_Telefone("Digite o seu número de telefone: ")
    cliente['numero_telefone_emergencia'] = verifica_Telefone("Digite o seu número de telefone de emergência: ")
    cliente['idade'] = leiaInt("Digite sua idade: ")
    cliente['email'] = verifica_Email("Digite sua email: ")

    lista_clientes.append(cliente)
    salvar_clientes(lista_clientes)
    print(linha())
    print('Cliente cadastrado com sucesso!')
    print(linha())


def exibir_clientes():
    lista_clientes = carregar_clientes()

    tamanho = len(lista_clientes[0]['nome'])
    for nome in lista_clientes:
        if len(nome['nome']) >= tamanho:
            tamanho = len(nome['nome']) + 4

    print(f'{"Numero":<{tamanho}}{"  Nome":<{tamanho}}{"  ID Fiscal":<{tamanho}}')
    print(linha())
    for pos, dado in enumerate(lista_clientes):
        id = ': '.join(lista_clientes[pos]["id_fiscal"])
        print(f'  {pos + 1:<{tamanho}}{dado["nome"]:<{tamanho}}{id:<{tamanho}}')


def exibir_detalhes_cliente(pos):
    lista_clientes = carregar_clientes()
    cliente = lista_clientes[pos]
    for chave, valor in cliente.items():
        if chave != 'id_fiscal':
            print(f'{chave}: {valor}')
        else:
            id = ': '.join(valor)
            print(id)


def editar_cliente(pos):
    lista_clientes = carregar_clientes()

    cliente = dict()
    cliente['nome'] = leiaStr("Digite o seu nome completo: ")
    cliente['pais'] = leiaStr("Digite seu pais: ")
    cliente['estado'] = leiaStr("Digite seu estado: ")
    cliente['endereco'] = leiaStr("Digite seu endereco: ")
    cliente['id_fiscal'] = verifica_idFiscal(cliente['pais'])
    cliente['numero_telefone'] = verifica_Telefone("Digite o seu número de telefone: ")
    cliente['numero_telefone_emergencia'] = verifica_Telefone("Digite o seu número de telefone de emergência: ")
    cliente['idade'] = leiaInt("Digite sua idade: ")
    cliente['email'] = verifica_Email("Digite sua email: ")

    lista_clientes[pos] = cliente.copy()
    salvar_clientes(lista_clientes)
    print(linha())
    print(f'Cliente {cliente["nome"]} Editado com sucesso!')
    print(linha())

def editar_dado_cliente(pos,chave,txt):
    lista_clientes = carregar_clientes()

    match chave:

            case 'nome':
                lista_clientes[pos][chave] = leiaStr(f'Digite o {txt}: ')
            case 'pais':
                lista_clientes[pos][chave] = leiaStr(f'Digite o {txt}: ')
            case 'estado':
                lista_clientes[pos][chave] = leiaStr(f'Digite o {txt}: ')
            case 'endereco':
                lista_clientes[pos][chave] = leiaStr(f'Digite o {txt}: ')
            case 'id_fiscal':
                lista_clientes[pos][chave] = verifica_idFiscal(lista_clientes[pos]['pais'])
            case 'numero_telefone':
                lista_clientes[pos][chave] = leiaInt(f'Digite o {txt}: ')
            case 'numero_telefone_emergencia':
                lista_clientes[pos][chave] = leiaInt(f'Digite o {txt}: ')
            case 'idade':
                lista_clientes[pos][chave] = leiaInt(f'Digite o {txt}: ')
            case 'email':
                lista_clientes[pos][chave] = leiaStr(f'Digite o {txt}: ')

    print(linha())
    print(f'{chave} do cliente editado com sucesso!')
    print(linha())
    salvar_clientes(lista_clientes)


def excluir_cliente(pos):
    lista_clientes = carregar_clientes()
    print(linha())
    print(f'Cliente {lista_clientes[pos]["nome"]} Removido com sucesso!')
    print(linha())
    lista_clientes.pop(pos)
    salvar_clientes(lista_clientes)