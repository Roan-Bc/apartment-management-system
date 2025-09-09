from modulos.interface import *
from modulos.apartment import *
from modulos.customer import *

while True:
    main_menu = exibeMenu(['Apartamento', 'Cliente', 'Sair do sistema'], 'Residencial Costão da Gamboa')
    match main_menu:
        case 1:

            while True:
                sub_menu = exibeMenu(['Cadastrar Apartamento ', 'Exibir Apartamentos', 'Editar Apartamento','Excluir Apartamentos', 'Voltar ao menu'],'Menu apartamento')
                match sub_menu:
                    case 1:
                        cabecalho('Cadastro apartamento')
                        cadastrar_apartamento()
                    case 2:
                        apartamentos = carregar_apartamentos()
                        if len(apartamentos) > 0:
                            cabecalho('Lista dos apartamentos')
                            exibir_apartamentos()
                            print(linha())

                            while True:
                                pos = leiaInt('Digite o número do apartamento que deseja ver mais detalhes: ')
                                pos -= 1

                                if pos < len(apartamentos):
                                    print()
                                    exibir_detalhes_apartamento(pos)
                                    print(linha())
                                    break
                                else:
                                    print(linha())
                                    print('Opção inválida!')
                                    print(linha())

                        else:
                            print(linha())
                            print('Não há apartamentos cadastrados no momento para exibir!')
                            print(linha())
                    case 3:
                        apartamentos = carregar_apartamentos()
                        if len(apartamentos) > 0:
                            cabecalho('Editar apartamento')
                            exibir_apartamentos()
                            print(linha())
                            while True:
                                pos = leiaInt('Digite o número do apartamento que deseja editar: ')
                                pos -= 1
                                if pos < len(apartamentos):
                                    while True:
                                        sub_menu = exibeMenu(['Editar todos os dados do apartamento','Editar um dado especifico do apartamento','Voltar ao menu'],'Editar dados do apartamento')
                                        if sub_menu == 1:
                                            cabecalho('Dados do apartamento')
                                            editar_todo_apartamento(pos)
                                            break
                                        elif sub_menu == 2:
                                             while True:
                                                 sub_menu = exibeMenu(['Nome','Quantidade Quarto','Quantidade Cozinha', 'Quantidade Banheiro', 'Quantidade Cama', 'Modelo da cama'], 'Dados do apartamento')
                                                 match sub_menu:

                                                     case 1:
                                                         editar_dado_apartamento(pos, 'nome_ap', 'nome do apartamento')
                                                         break
                                                     case 2:
                                                         editar_dado_apartamento( pos, 'quant_quarto', 'quantidade de quarto')
                                                         break
                                                     case 3:
                                                         editar_dado_apartamento( pos, 'quant_cozinha', 'quantidade de cozinha')
                                                         break
                                                     case 4:
                                                         editar_dado_apartamento( pos, 'quant_banheiro', 'quantidade banheiro')
                                                         break
                                                     case 5:
                                                         editar_dado_apartamento( pos, 'quant_cama', 'quantidade da cama')
                                                         break
                                                     case 6:
                                                         if apartamentos[pos]['quant_cama'] > 0 :
                                                            editar_dado_apartamento(pos, 'tipo_cama', 'modelo da cama')
                                                            break
                                                         else:
                                                             print(linha())
                                                             print('Como não há uma quantidade de camas cadastradas, não é possivel fazer a alteração do modelo da cama!')
                                                             print(linha())
                                                     case _:
                                                         print(linha())
                                                         print('Opção Inválida!')
                                                         print(linha())

                                             break
                                        elif sub_menu == 3:
                                             break
                                        else:
                                             print(linha())
                                             print('Opção inválida!')
                                             print(linha())
                                    break
                                else:
                                    print(linha())
                                    print('Opção inválida!')
                                    print(linha())
                        else:
                            print(linha())
                            print('Não há apartamentos cadastrados no momento para editar!')
                            print(linha())
                    case 4:
                        apartamentos = carregar_apartamentos()
                        if len(apartamentos) > 0:
                            cabecalho('Excluir apartamentos')
                            exibir_apartamentos()
                            while True:
                                pos = leiaInt('Digite o número do apartamento que deseja editar: ')
                                pos -= 1
                                if pos < len(apartamentos):
                                    excluir_apartamento(pos)
                                    break
                                else:
                                    print(linha())
                                    print('Opção inválida!')
                                    print(linha())

                        else:
                            print(linha())
                            print('Não há apartamentos cadastrados no momento para excluir!')
                            print(linha())
                    case 5:
                        break
                    case _:
                        print(linha())
                        print('Opção inválida!')
                        print(linha())
        case 2:

            while True:
                sub_menu = exibeMenu(['Cadastrar Cliente ', 'Exibir Cliente', 'Editar Cliente','Excluir Cliente', 'Voltar ao menu'])
                match sub_menu:
                    case 1:
                        cabecalho('Cadastrar Cliente')
                        cadastrar_cliente()
                    case 2:
                        cabecalho('Exibir clientes')
                        exibir_clientes()
                    case 3:
                        print('Editar Cliente')
                    case 4:
                        print('Excluir cliente')
                    case 5:
                        break
                    case _:
                        print('Opção inválida!')
        case 3:
            linha()
            print('Saindo do sistema...')
            break
        case _:
            print('Opção inválida!')