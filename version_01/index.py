from modulos import *


while True:
    main_menu = exibeMenu(['Apartamento', 'Cliente', 'Reserva', 'Sair do sistema'], 'Residencial Costão da Gamboa')

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

                                if 0 <= pos < len(apartamentos):
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

                                if 0 <= pos < len(apartamentos):

                                    while True:
                                        sub_menu = exibeMenu(['Editar todos os dados do apartamento','Editar um dado especifico do apartamento','Voltar ao menu'],f'Editar dados do {apartamentos[pos]["nome_ap"]}')
                                        if sub_menu == 1:
                                            editar_todo_apartamento(pos)
                                            break
                                        elif sub_menu == 2:

                                             while True:
                                                 sub_menu = exibeMenu(['Nome','Quantidade Quarto','Quantidade Cozinha', 'Quantidade Banheiro', 'Quantidade Cama', 'Modelo da cama'], f'Dados do {apartamentos[pos]["nome_ap"]}')
                                                 match sub_menu:

                                                     case 1:
                                                         editar_dado_apartamento(pos, 'nome_ap', 'nome')
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
                                                        if apartamentos[pos]['quant_cama'] > 0:
                                                            editar_dado_apartamento(pos, 'tipo_cama', 'modelo da cama')
                                                            break
                                                        else:
                                                            print(linha())
                                                            print('Como a quantidade de camas é igual 0, não é possivel realizar a alteração do modelo da cama!')
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
                                pos = leiaInt('Digite o número do apartamento que deseja excluir: ')
                                pos -= 1

                                if 0 <= pos < len(apartamentos):
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
                sub_menu = exibeMenu(['Cadastrar Cliente ', 'Exibir Cliente', 'Editar Cliente','Excluir Cliente', 'Voltar ao menu'], 'Menu Cliente')

                match sub_menu:

                    case 1:
                        cabecalho('Cadastrar Cliente')
                        cadastrar_cliente()

                    case 2:

                        clientes = carregar_clientes()
                        if len(clientes) > 0:
                            cabecalho('Exibir clientes')
                            exibir_clientes()

                            while True:
                                if len(clientes) > 0:
                                    pos = leiaInt('Digite o número do cliente que deseja visualizar mais detalhes: ')
                                    pos -= 1

                                    if 0 <= pos < len(clientes):
                                        exibir_detalhes_cliente(pos)
                                        print(linha())
                                        break
                                    else:
                                        print('Opção inválida!')
                                else:
                                    print('Opção inválida!')
                        else:
                            print('Não há clientes cadastrados no momento para exibir!')

                    case 3:

                        clientes = carregar_clientes()
                        if len(clientes) > 0:
                            cabecalho('Editar Cliente')
                            exibir_clientes()
                            print(linha())

                            while True:
                                pos = leiaInt('Digite o número do Cliente que deseja editar: ')
                                pos -= 1

                                if 0 <= pos < len(clientes):

                                    while True:
                                        sub_menu = exibeMenu(['Editar todos os dados do cliente','Editar um dado especifico do cliente','Voltar ao menu'], f'Editar dados do Cliente {clientes[pos]["nome"]}')

                                        if sub_menu == 1:
                                            editar_todo_cliente(pos)
                                            break

                                        elif sub_menu == 2:

                                            while True:
                                                sub_menu = exibeMenu(['Nome', 'pais', 'estado','endereco', 'id_fiscal','numero_telefone', 'numero_telefone_emergencia', 'idade', 'email'], f'Dados do cliente {clientes[pos]["nome"]}')

                                                match sub_menu:

                                                    case 1:
                                                        editar_dado_cliente(pos, 'nome', 'nome completo')
                                                        break
                                                    case 2:
                                                        editar_dado_cliente(pos, 'pais', 'pais')
                                                        break
                                                    case 3:
                                                        editar_dado_cliente(pos, 'estado','estado')
                                                        break
                                                    case 4:
                                                        editar_dado_cliente(pos, 'endereco', 'endereço')
                                                        break
                                                    case 5:
                                                        editar_dado_cliente(pos, 'id_fiscal', 'id fiscal')
                                                        break
                                                    case 6:
                                                        editar_dado_cliente(pos, 'numero_telefone', 'número de telefone')
                                                    case 7:
                                                        editar_dado_cliente(pos, 'numero_telefone','número de telefone de emergência')
                                                    case 8:
                                                        editar_dado_cliente(pos, 'numero_telefone', 'idade')
                                                    case 9:
                                                        editar_dado_cliente(pos, 'email','email')
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
                            print('Não há clientes cadastrados no momento para editar!')
                            print(linha())

                    case 4:

                        clientes = carregar_clientes()
                        if len(clientes) > 0:
                            cabecalho('Excluir Cliente')
                            exibir_clientes()

                            while True:
                                pos = leiaInt('Digite o número do cliente que deseja excluir: ')
                                pos -= 1

                                if 0 <= pos < len(clientes):
                                    excluir_cliente(pos)
                                    break
                                else:
                                    print(linha())
                                    print('Opção inválida!')
                                    print(linha())
                        else:
                            print(linha())
                            print('Não há clientes cadastrados no momento para excluir!')
                            print(linha())

                    case 5:
                        break
                    case _:
                        print('Opção inválida!')
        case 3:

            while True:
                sub_menu = exibeMenu(['Cadastrar Reserva ', 'Exibir Reserva', 'Editar Reserva', 'Excluir Reserva', 'Voltar ao menu'],'Menu Reserva')

                match sub_menu:

                    case 1:
                        cabecalho('Cadastrar reserva')
                        cadastrar_reserva()

                    case 2:

                        reserva = carregar_reservas()
                        if len(reserva) > 0:

                            while True:
                                sub_menu = exibeMenu(['Exibir todas reservas ', 'Exibir todas reservas de um apartamento', 'Exibir todas reserva de um cliente','Voltar ao menu'], 'Reservas')

                                match sub_menu:

                                    case 1:
                                        cabecalho('Exibir reservas')
                                        exibir_reservas()

                                        while True:
                                            pos = leiaInt('Digite o número da reserva que deseja ver mais detalhes: ')
                                            pos -= 1

                                            if 0 <= pos < len(reserva):
                                                exibir_detalhes_reserva(pos,'nome_cliente','cliente')
                                                print(linha())
                                                break
                                            else:
                                                print(linha())
                                                print('Opção inválida!')
                                                print(linha())
                                    case 2:

                                        nome = nome_apartamentos()
                                        cabecalho(f'Reservas associadas ao {nome}')
                                        verifica = exibir_reservas_nomeApartamento(nome)
                                        if verifica:
                                            while True:
                                                pos = leiaInt('Digite o número da reserva que deseja ver mais detalhes: ')
                                                pos -= 1

                                                if 0 <= pos < len(reserva):
                                                    exibir_detalhes_reserva(pos,'nome_apartamento','apartamento')
                                                    print(linha())
                                                    break
                                                else:
                                                    print(linha())
                                                    print('Opção inválida!')
                                                    print(linha())
                                    case 3:
                                        nome = nome_clientes()
                                        cabecalho(f'Reservas feitas do cliente {nome}')
                                        verifica = exibir_reservas_nomeCliente(nome)
                                        if verifica:
                                            while True:
                                                pos = leiaInt('Digite o número da reserva que deseja ver mais detalhes: ')
                                                pos -= 1

                                                if 0 <= pos < len(reserva):
                                                    exibir_detalhes_reserva(pos,'nome_cliente', 'cliente')
                                                    print(linha())
                                                    break
                                                else:
                                                    print(linha())
                                                    print('Opção inválida!')
                                                    print(linha())
                                    case 4:
                                        break
                                    case _:
                                        print('Opção inválida!')
                        else:
                            print('Não há reservas cadastradas no momento disponiveis para exibir!')
                    case 3:

                        reserva = carregar_reservas()
                        if len(reserva) > 0:
                            cabecalho('Editar Reserva')
                            exibir_reservas()
                            print(linha())

                            while True:
                                pos = leiaInt('Digite o número da Reserva que deseja editar: ')
                                pos -= 1

                                if 0 <= pos < len(reserva):

                                    while True:
                                        sub_menu = exibeMenu(['Editar todos os dados da reserva', 'Editar um dado especifico da reserva','Voltar ao menu'], f'Editar dados da Reserva {pos + 1} do cliente {reserva[pos]["nome_cliente"]}')

                                        if sub_menu == 1:
                                            cabecalho('Dados da reserva')
                                            editar_toda_reserva(pos)
                                            break

                                        elif sub_menu == 2:

                                            while True:
                                                sub_menu = exibeMenu(['nome apartamento', 'nome cliente', 'plataforma', 'forma de pagamento', 'valor','check-in', 'check-out', 'quantidade hospedes', 'quantidade animais','observação','voltar ao menu'], f'Dados da reserva {pos + 1} do cliente {reserva[pos]["nome_cliente"]}')

                                                match sub_menu:

                                                    case 1:
                                                        editar_dado_reserva(pos, 'nome_apartamento', 'nome do apartamento')
                                                        break
                                                    case 2:
                                                        editar_dado_reserva(pos, 'nome_cliente', 'nome do cliente')
                                                        break
                                                    case 3:
                                                        editar_dado_reserva(pos, 'plataforma', 'plataforma')
                                                        break
                                                    case 4:
                                                        if reserva[pos]['plataforma'].lower() == 'whatsapp':
                                                            editar_dado_reserva(pos, 'forma_de_pagamento', 'forma de pagamento')
                                                            break
                                                        else:
                                                           print(linha())
                                                           print('Não é possivel editar a forma de pagamento se a plataforma de reserva não for whatsapp!')
                                                           print(linha())
                                                    case 5:
                                                        editar_dado_reserva(pos, 'valor', 'valor')
                                                        break
                                                    case 6:
                                                        editar_dado_reserva(pos, 'check-in', 'check-in')
                                                        break
                                                    case 7:
                                                        editar_dado_reserva(pos, 'check-out', 'check-out')
                                                        break
                                                    case 8:
                                                        editar_dado_reserva(pos, 'quant_de_hospede', 'quantidade de hóspede')
                                                        break
                                                    case 9:
                                                        editar_dado_reserva(pos, 'quant_de_animais', 'quantidade de animais')
                                                        break
                                                    case 10:
                                                        editar_dado_reserva(pos, 'observacao', 'observação')
                                                        break
                                                    case 11:
                                                        break
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
                            print('Não há Reservas cadastrados no momento para editar!')
                            print(linha())
                    case 4:

                        reserva = carregar_reservas()
                        if len(reserva) > 0:
                            cabecalho('Excluir Reserva')
                            exibir_reservas()

                            while True:
                                pos = leiaInt('Digite o número da reserva que deseja excluir: ')
                                pos -= 1

                                if 0 <= pos < len(reserva):
                                    excluir_reserva(pos)
                                    break
                                else:
                                    print(linha())
                                    print('Opção inválida!')
                                    print(linha())
                        else:
                            print(linha())
                            print('Não há reservas cadastradas no momento para excluir!')
                            print(linha())
                    case 5:
                        break
                    case _:
                        print('Opção inválida')
        case 4:
            print('Saindo do sistema...')
            break
        case _:
            print('Opção inválida!')