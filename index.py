from modulos.interface import *

while True:
    opcao = exibeMenu(['Apartamento', 'Cliente', 'Sair do sistema'])

    match opcao:
        case 1:
            opcao = exibeMenu(['Cadastrar Apartamento ', 'Exibir Apartamentos', 'Excluir Apartamentos', 'Voltar ao menu'])
        case 2:
            opcao = exibeMenu(['Cadastrar Cliente ', 'Exibir Cliente', 'Excluir Cliente', 'Voltar ao menu'])
        case 3:
            linha()
            print('Saindo do sistema...')
            break