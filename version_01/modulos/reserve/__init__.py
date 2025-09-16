from version_01.modulos.tests import *
from version_01.modulos.interface import linha, cabecalho
from version_01.modulos.customer import *
from version_01.modulos.apartment import *
from datetime import datetime
import json

CAMINHO_JSON = "dados/lista_reservas.json"

def carregar_reservas():

    try:
        with open(CAMINHO_JSON, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def salvar_reservas(lista_reservas):

    with open(CAMINHO_JSON, "w", encoding="utf-8") as file:
        json.dump(lista_reservas, file, indent=4, ensure_ascii=False)


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


def calculaDiarias(checkin, checkout):

    formato = "%d/%m/%Y"

    checkin = datetime.strptime(checkin, formato)
    checkout = datetime.strptime(checkout, formato)

    diarias = (checkout - checkin).days
    return diarias

def verificaDiarias(checkin, checkout):

    formato = "%d/%m/%Y"

    checkin = datetime.strptime(checkin, formato)
    checkout = datetime.strptime(checkout, formato)

    if checkin < checkout:
        return True
    else:
        return False


def cadastrar_reserva():

    lista_reservas = carregar_reservas()

    reserva = dict()

    reserva['nome_apartamento'] = nome_apartamentos()
    reserva['nome_cliente'] = nome_clientes()
    reserva['plataforma'] = leiaStr('Digite a plataforma de reserva (Airbnb/Whatsapp): ')

    if reserva['plataforma'].lower() == 'whatsapp':
        reserva['forma_de_pagamento'] = leiaStr('Digite a forma de pagamento: ')

    reserva['valor'] = leiaInt('Digite o valor do reserva: ')
    reserva['check-in'] = verificaData('Digite a data de Check-in: ')

    while True:
        checkout = verificaData('Digite a data de Check-out: ')
        if verificaDiarias(reserva['check-in'], checkout):
            reserva['check-out'] = checkout
            break
        else:
            print('Check-out inválido, digite novamente!')
    reserva['quantidade_diarias'] = calculaDiarias(reserva['check-in'], reserva['check-out'])
    reserva['quantidade_hospedes'] = leiaInt('Digite a quantidade de hospedes: ')
    reserva['quantidade_animais'] = leiaInt('Digite a quantidade de animais: ')
    reserva['observacao'] = leiaStr('Digite o observacao: ')

    lista_reservas.append(reserva)
    salvar_reservas(lista_reservas)
    print(linha())
    print('Reserva cadastrada com sucesso!')
    print(linha())


def exibir_reservas():

    lista_reservas = carregar_reservas()

    tamanho = len(lista_reservas[0]['nome_cliente'])
    for nome in lista_reservas:
        if len(nome['nome_cliente']) >= tamanho:
            tamanho = len(nome['nome_cliente']) + 4

    if tamanho < 20:
        tamanho = 20

    print(f'{"Numero":<{tamanho}}{"  Nome apartamento":<{tamanho}}{"  Nome Cliente":<{tamanho}}')
    print(linha())
    for pos, dado in enumerate(lista_reservas):
        print(f'  {pos + 1:<{tamanho}}{dado["nome_apartamento"]:<{tamanho}}{dado["nome_cliente"]:<{tamanho}}')



def exibir_reservas_nomeApartamento(nomeApartamento):

    lista_reservas = carregar_reservas()

    tamanho = len(lista_reservas[0]['nome_cliente'])
    for nome in lista_reservas:
        if len(nome['nome_cliente']) >= tamanho:
            tamanho = len(nome['nome_cliente']) + 4

    if tamanho < 20:
        tamanho = 20

    print(f'{"Numero":<{tamanho}}{"  Nome apartamento":<{tamanho}}{"  Nome Cliente":<{tamanho}}')
    print(linha())

    verifica_nome = len(lista_reservas)

    for pos, dado in enumerate(lista_reservas):

        if dado['nome_apartamento'] == nomeApartamento:
            print(f'  {pos + 1:<{tamanho}}{dado["nome_apartamento"]:<{tamanho}}{dado["nome_cliente"]:<{tamanho}}')
        else:
            verifica_nome -= 1
            if verifica_nome == 0:
                print(f'Não há reservas associadas ao apartamento {nomeApartamento}')


def exibir_reservas_nomeCliente(nomeCliente):

    lista_reservas = carregar_reservas()

    tamanho = len(lista_reservas[0]['nome_cliente'])
    for nome in lista_reservas:
        if len(nome['nome_cliente']) >= tamanho:
            tamanho = len(nome['nome_cliente']) + 4

    if tamanho < 20:
        tamanho = 20

    print(f'{"Numero":<{tamanho}}{"  Nome apartamento":<{tamanho}}{"  Nome Cliente":<{tamanho}}')
    print(linha())

    verifica_nome = len(lista_reservas)

    for pos, dado in enumerate(lista_reservas):
        if dado['nome_cliente'] == nomeCliente:
            print(f'  {pos + 1:<{tamanho}}{dado["nome_apartamento"]:<{tamanho}}{dado["nome_cliente"]:<{tamanho}}')
        else:
            verifica_nome -= 1
            if verifica_nome == 0:
                print(f'Não há reservas no nome do cliente {nomeCliente}')


def exibir_detalhes_reserva(pos):

    lista_reservas = carregar_reservas()
    reserva = lista_reservas[pos]

    for chave, valor in reserva.items():
        if '_' in chave:
            nova_chave = chave.replace('_',' ')
            print(f'{nova_chave}: {valor}')
        elif chave == 'valor':
            print(f'{chave}: R${valor:.2f}')
        else:
            print(f'{chave}: {valor}')


def editar_toda_reserva(pos):

    lista_reservas = carregar_reservas()

    reserva = dict()

    reserva['nome_apartamento'] = nome_apartamentos()
    reserva['nome_cliente'] = nome_clientes()
    reserva['plataforma'] = leiaStr('Digite a plataforma de reserva (Airbnb/Whatsapp): ')

    if reserva['plataforma'].lower() == 'whatsapp':
        reserva['forma_de_pagamento'] = leiaStr('Digite a forma de pagamento: ')

    reserva['valor'] = leiaInt('Digite o valor do reserva: ')
    reserva['check-in'] = verificaData('Digite a data de Check-in: ')

    while True:
        checkout = verificaData('Digite a data de Check-out: ')
        if verificaDiarias(reserva['check-in'], checkout):
            reserva['check-out'] = checkout
            break
        else:
            print('Check-out inválido, digite novamente!')

    reserva['quantidade_diarias'] = calculaDiarias(reserva['check-in'], reserva['check-out'])
    reserva['quantidade_hospedes'] = leiaInt('Digite a quantidade de hospedes: ')
    reserva['quantidade_animais'] = leiaInt('Digite a quantidade de animais: ')
    reserva['observacao'] = leiaStr('Digite o observacao: ')

    lista_reservas[pos] = reserva.copy()
    salvar_reservas(lista_reservas)

    print(linha())
    print('Reserva Editada com sucesso!')
    print(linha())

def editar_dado_reserva(pos,chave):
    lista_reservas = carregar_reservas()

    match chave:

        case 'nome_apartamento':
            lista_reservas[pos][chave] = nome_apartamentos()
        case 'nome_cliente':
            lista_reservas[pos][chave] = nome_clientes()
        case 'plataforma':
            lista_reservas[pos][chave] = leiaStr('Digite a plataforma de reserva (Airbnb/Whatsapp): ')
        case 'forma_de_pagamento':
           lista_reservas[pos][chave] = leiaStr('Digite a forma de pagamento: ')
        case 'valor':
            lista_reservas[pos][chave] = leiaInt('Digite o valor do reserva: ')
        case 'check-in':
            checkin = verificaData('Digite a data de Check-in: ')
            if verificaDiarias(checkin, lista_reservas[pos]['check-out']):
                lista_reservas[pos][chave] = checkin
                lista_reservas[pos]['quantidade_diarias'] = calculaDiarias(lista_reservas[pos]['check-in'], lista_reservas[pos]['check-out'])
            else:
                return print('Não é possivel inserir um check-in que seja após o check-out')
        case 'check-out':
            checkout = verificaData('Digite a data de Check-out: ')
            if verificaDiarias(lista_reservas[pos]['check-in'], checkout):
                lista_reservas[pos][chave] = checkout
                lista_reservas[pos]['quantidade_diarias'] = calculaDiarias(lista_reservas[pos]['check-in'],lista_reservas[pos]['check-out'])
            else:
                return print('Não é possivel inserir um check-out que seja antes do check-int')
        case 'quantidade_hospedes':
            lista_reservas[pos][chave] = leiaInt('Digite a quantidade de hospedes: ')
        case 'quantidade_animais':
            lista_reservas[pos][chave] = leiaInt('Digite a quantidade de animais: ')
        case 'observacao':
            lista_reservas[pos][chave] = leiaStr('Digite o observacao: ')

    salvar_reservas(lista_reservas)

    print(linha())
    print(f'{chave} da reserva editada com sucesso!')
    print(linha())

def excluir_reserva(pos):
    lista_reservas = carregar_reservas()
    print(linha())
    print(f'Reserva no nome de {lista_reservas[pos]["nome_cliente"]} Removido com sucesso!')
    print(linha())
    lista_reservas.pop(pos)
    salvar_reservas(lista_reservas)




