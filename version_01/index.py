from modulos.interface import *
from modulos.apartment import *

apartamento = list()

while True:
    main_menu = exibeMenu(['Apartamento', 'Cliente', 'Sair do sistema'])
    match main_menu:
        case 1:

            while True:
                sub_menu = exibeMenu(['Cadastrar Apartamento ', 'Exibir Apartamentos', 'Excluir Apartamentos', 'Voltar ao menu'])
                match sub_menu:
                    case 1:
                        cabecalho('Cadastrar apartamento')
                        cadastrar_apartamento(apartamento)
                        linha()
                    case 2:
                        cabecalho('Exibir apartamentos')
                        exibir_apartamentos(apartamento)
                        linha()
                    case 3:
                        cabecalho('Excluir apartamentos')
                        linha()
                    case 4:
                        break
        case 2:

            while True:
                sub_menu = exibeMenu(['Cadastrar Cliente ', 'Exibir Cliente', 'Excluir Cliente', 'Voltar ao menu'])
                match sub_menu:
                    case 1:
                        print('Cadastrar Cliente')
                    case 2:
                        print('Exibir clientes')
                    case 3:
                        print('Excluir cliente')
                    case 4:
                        break
        case 3:
            linha()
            print('Saindo do sistema...')
            break