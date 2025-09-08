from modulos.interface import *
from modulos.apartment import *

apartamento = list()

while True:
    main_menu = exibeMenu(['Apartamento', 'Cliente', 'Sair do sistema'])
    match main_menu:
        case 1:

            while True:
                sub_menu = exibeMenu(['Cadastrar Apartamento ', 'Exibir Apartamentos', 'Editar Apartamento','Excluir Apartamentos', 'Voltar ao menu'])
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
                        cabecalho('Editar apartamento')
                        exibir_apartamentos(apartamento)
                        linha()

                        while True:
                            opcao = leiaInt('Digite o número do apartamento que deseja editar(999 para sair): ')
                            if opcao == 999:
                                break
                            opcao -= 1
                            if opcao < len(apartamento):
                                while True:
                                    sub_menu = exibeMenu(['Editar todos os dados do apartamento','Editar um dado especifico do apartamento','Voltar ao menu'])
                                    if sub_menu == 3:
                                        break
                                    elif sub_menu == 1:
                                        editar_apartamento_completo(apartamento, opcao)
                                        break
                                    else:
                                        print('Opção inválida!')
                                break
                            else:
                                print('Opção inválida!')
                    case 4:
                        cabecalho('Excluir apartamentos')
                        excluir_apartamento(apartamento)
                        linha()
                    case 5:
                        break
                    case _:
                        print('Opção inválida!')
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
                    case _:
                        print('Opção inválida!')
        case 3:
            linha()
            print('Saindo do sistema...')
            break
        case _:
            print('Opção inválida!')