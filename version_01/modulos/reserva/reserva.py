from version_01.modulos.testes import *
from version_01.modulos.interface import linha, cabecalho
from .nomes import *
from .diarias import *
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



def cadastrar_reserva():

    lista_reservas = carregar_reservas()

    reserva = dict()

    reserva['nome_apartamento'] = nome_apartamentos()
    reserva['nome_cliente'] = nome_clientes()
    reserva['plataforma'] = leiaStr('Digite a plataforma de reserva (Airbnb/Whatsapp): ')

    if reserva['plataforma'].lower() == 'whatsapp':
        reserva['forma_de_pagamento'] = leiaStr('Digite a forma de pagamento: ')

    reserva['valor'] = leiaInt('Digite o valor da reserva: ')
    reserva['check-in'] = verificaData('Digite a data de Check-in: ')

    while True:
        checkout = verificaData('Digite a data de Check-out: ')
        if verificaDiarias(reserva['check-in'], checkout):
            reserva['check-out'] = checkout
            break
        else:
            print('Check-out inválido, digite novamente!')
    reserva['quant_diarias'] = calculaDiarias(reserva['check-in'], reserva['check-out'])
    reserva['quant_hospedes'] = leiaInt('Digite a quantidade de hospedes: ')
    reserva['quant_animais'] = leiaInt('Digite a quantidade de animais: ')
    reserva['observacao'] = leiaStr('Digite o observacao: ')

    lista_reservas.append(reserva)
    salvar_reservas(lista_reservas)

    print(linha())
    print(f'Reserva {len(lista_reservas)} cadastrada no nome do cliente {reserva["nome_cliente"]} com sucesso!')
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
    for pos, reserva in enumerate(lista_reservas):
        print(f'  {pos + 1:<{tamanho}}{reserva["nome_apartamento"]:<{tamanho}}{reserva["nome_cliente"]:<{tamanho}}')



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

    for pos, reserva in enumerate(lista_reservas):

        if reserva['nome_apartamento'] == nomeApartamento:
            print(f'  {pos + 1:<{tamanho}}{reserva["nome_apartamento"]:<{tamanho}}{reserva["nome_cliente"]:<{tamanho}}')
        else:
            verifica_nome -= 1
            if verifica_nome == 0:
                print(f'Não há reservas associadas ao {nomeApartamento}')
                return False
    return True


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

    for pos, reserva in enumerate(lista_reservas):
        if reserva['nome_cliente'] == nomeCliente:
            print(f'  {pos + 1:<{tamanho}}{reserva["nome_apartamento"]:<{tamanho}}{reserva["nome_cliente"]:<{tamanho}}')
        else:
            verifica_nome -= 1
            if verifica_nome == 0:
                print(f'Não há reservas no nome do cliente {nomeCliente}')
                return False

    return True

def exibir_detalhes_reserva(pos, chave, txt):

    lista_reservas = carregar_reservas()
    reserva = lista_reservas[pos]

    cabecalho(f'Detalhes da reserva {pos + 1} do {txt} {reserva[chave]}')
    for chave, valor in reserva.items():
        if 'quant' in chave:
            quant_chave = chave.replace('quant_','quantidade de ')
            print(f'{quant_chave}: {valor}')
        elif 'nome_' in chave:
            nome_chave = chave.replace('nome_','nome do ')
            print(f'{nome_chave}: {valor}')
        elif chave == 'observacao':
            print(f'observação: {valor}')
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

    reserva['quant_diarias'] = calculaDiarias(reserva['check-in'], reserva['check-out'])
    reserva['quant_hospedes'] = leiaInt('Digite a quantidade de hospedes: ')
    reserva['quant_animais'] = leiaInt('Digite a quantidade de animais: ')
    reserva['observacao'] = leiaStr('Digite a observação: ')

    lista_reservas[pos] = reserva.copy()
    salvar_reservas(lista_reservas)

    print(linha())
    print(f'Reserva {pos + 1} no nome do cliente {reserva["nome_cliente"]} Editada com sucesso!')
    print(linha())

def editar_dado_reserva(pos,chave, txt):

    lista_reservas = carregar_reservas()
    reserva = lista_reservas[pos]

    match chave:

        case 'nome_apartamento':
            reserva[chave] = nome_apartamentos()
        case 'nome_cliente':
            reserva[chave] = nome_clientes()
        case 'plataforma':
            reserva[chave] = leiaStr('Digite a plataforma de reserva (Airbnb/Whatsapp): ')
            if reserva[chave].lower() == 'whatsapp':
                lista_reservas[pos]['forma_de_pagamento'] = leiaStr('Digite a forma de pagamento: ')
        case 'forma_de_pagamento':
            reserva[chave] = leiaStr('Digite a forma de pagamento: ')
        case 'valor':
            reserva[chave] = leiaInt('Digite o valor do reserva: ')
        case 'check-in':
            while True:
                checkin = verificaData('Digite a data de Check-in: ')
                if verificaDiarias(checkin, reserva['check-out']):
                    reserva[chave] = checkin
                    reserva['quantidade_diarias'] = calculaDiarias(reserva['check-in'], reserva['check-out'])
                    break
                else:
                     print('Não é possivel inserir um check-in que seja após o check-out, digite novamente!')
        case 'check-out':
            while True:
                checkout = verificaData('Digite a data de Check-out: ')
                if verificaDiarias(reserva['check-in'], checkout):
                    reserva[chave] = checkout
                    reserva['quantidade_diarias'] = calculaDiarias(reserva['check-in'],reserva['check-out'])
                    break
                else:
                     print('Não é possivel inserir um check-out que seja antes do check-in, digite novamente!')
        case 'quant_hospedes':
            reserva[chave] = leiaInt('Digite a quantidade de hospedes: ')
        case 'quant_animais':
            reserva[chave] = leiaInt('Digite a quantidade de animais: ')
        case 'observacao':
            reserva[chave] = leiaStr('Digite o observacao: ')

    lista_reservas[pos][chave] = reserva[chave]
    salvar_reservas(lista_reservas)

    print(linha())
    print(f'{txt} da reserva editada com sucesso!')
    print(linha())

def excluir_reserva(pos):

    lista_reservas = carregar_reservas()

    print(linha())
    print(f'Reserva {pos + 1} no nome de {lista_reservas[pos]["nome_cliente"]} Removido com sucesso!')
    print(linha())

    lista_reservas.pop(pos)
    salvar_reservas(lista_reservas)




