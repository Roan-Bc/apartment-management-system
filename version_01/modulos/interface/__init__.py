from version_01.modulos.tests import leiaInt

def linha(tamanho=42):
    return '-' * tamanho

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def exibeMenu(lista):
    cabecalho('MENU PRINCIPAL')
    contador = 1
    for item in lista:
        print(f'{contador} - {item}')
        contador += 1
    print(linha())
    opcao = leiaInt(f'Sua Opção: ')
    return opcao