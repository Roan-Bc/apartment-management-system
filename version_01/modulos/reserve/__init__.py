from version_01.modulos.tests import *
from version_01.modulos.interface import linha, cabecalho
from version_01.modulos.customer import *
from version_01.modulos.apartment import *
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
    lista_apartamentos = carregar_apartamentos()
    lista_clientes = carregar_clientes()

    reserva = dict()

    for pos, valor in enumerate(lista_apartamentos):
        if valor['nome_ap']:
            print(f'{pos+1}  {valor["nome_ap"]}')


    while True:
        pos = leiaInt('Digite o número do apartamento que deseja adicionar: ')
        pos -= 1
        if 0 < pos < len(lista_apartamentos):
            reserva['nome_apartamento'] = lista_apartamentos[pos]['nome_ap']
            break
        else:
            print('Número inválido, digite novamente.')

    for pos, valor in enumerate(lista_clientes):
        if valor['nome']:
            print(f'{pos + 1}   {valor["nome"]}')

    while True:
        pos = leiaInt('Digite o número do cliente que deseja adicionar: ')
        pos -= 1
        if 0 <= pos < len(lista_clientes):
            reserva['nome_cliente'] = lista_clientes[pos]['nome']
            break
        else:
            print('Número inválido, digite novamente.')

    reserva['plataforma'] = leiaStr('Digite a plataforma de reserva (Airbnb/Whatsapp): ')
    if reserva['plataforma'].lower() == 'whatsapp':
        reserva['Forma de pagamento'] = leiaStr('Digite a forma de pagamento: ')
    reserva['valor'] = leiaInt('Digite o valor do reserva: ')
    reserva['check-in'] = verificaData('Digite a data de Check-in: ')
    reserva['check-out'] = verificaData('Digite a data de Check-out: ')
    reserva['quant_hospedes'] = leiaInt('Digite a quantidade de hospedes: ')
    reserva['quant_animais'] = leiaInt('Digite a quantidade de animais: ')

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

    print(f'{"Numero":<{tamanho}}{"  Nome apartamento":<{tamanho}}{"  Nome Cliente":<{tamanho}}')
    print(linha())
    for pos, dado in enumerate(lista_reservas):
        print(f'  {pos + 1:<{tamanho}}{dado["nome_apartamento"]:<{tamanho}}{dado["nome_cliente"]:<{tamanho}}')