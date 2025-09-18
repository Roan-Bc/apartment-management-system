from version_01.modulos.cliente import *
from version_01.modulos.apartamento import *


def nome_apartamentos():

    lista_apartamentos = carregar_apartamentos()
    cabecalho('Nome dos apartamentos')
    for pos, valor in enumerate(lista_apartamentos):
        if valor['nome_ap']:
            print(f'{pos+1}  {valor["nome_ap"]}')


    while True:
        pos = leiaInt('Digite o número do apartamento que deseja adicionar: ')
        pos -= 1
        if 0 <= pos < len(lista_apartamentos):
            print()
            return lista_apartamentos[pos]['nome_ap']
        else:
            print('Número inválido, digite novamente.')


def nome_clientes():

    lista_clientes = carregar_clientes()
    cabecalho('Nome do clientes')
    for pos, valor in enumerate(lista_clientes):
        if valor['nome']:
            print(f'{pos + 1}   {valor["nome"]}')

    while True:
        pos = leiaInt('Digite o número do cliente que deseja adicionar: ')
        pos -= 1
        if 0 <= pos < len(lista_clientes):
            print()
            return lista_clientes[pos]['nome']
        else:
            print('Número inválido, digite novamente.')