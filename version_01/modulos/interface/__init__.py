from version_01.modulos.tests import leiaInt, leiaStr

def linha(tamanho=120):
    return '=' * tamanho

def cabecalho(txt):
    print(linha())
    print(txt.center(120))
    print(linha())

def exibeMenu(lista,nome='MENU PRINCIPAL'):
    cabecalho(nome)
    contador = 1
    for item in lista:
        print(f'{contador} - {item}')
        contador += 1
    print(linha())
    opcao = leiaInt(f'Sua Opção: ')
    return opcao
