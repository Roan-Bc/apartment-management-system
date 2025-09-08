#  Versão 1.0 🏢 Apartment Management System

---
  
## 🛠️ Roadmap de Desenvolvimento


### ✅ Versão 1 (atual)


- 📅 07/09/2025: Hoje fiz a implementação da minha estrutura inicial de alguns sub-menus e também terminei de fazer as funções de exibir, editar e excluir apartamentos, a princípio está funcionando mas quero fazer algumas modificações amanhã pois acho que da fazer de uma forma melhor.

  Referente a estrutura de menu e sub-menu, a princpio está assim:

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


  Agora referente as novas funções que fiz no módulo Apartament, foram essas:
    
  Funções:
  
    - *exibir_apartamentos*: Recebe como parâmetro uma lista, não possui retorno.

      A função basicamente, vai retornar print da posição e o nome do apartamento até não ter mais nenhum apartamento apra mostrar.

      OBS: Por enquanto só estou exibindo a posição e o nome, mas estou pensando ainda se vou exibir todas as informações de uma vez ou se peço para o usuário selecionar o apartamento e após selecionar o apartamento especifico, exibir todas a informações referente ao apartamento.

          def exibir_apartamentos(list):
            print(f'{"Numero"}{"Apartamento":>20}')
            print(linha())
            for pos, dado in enumerate(list):
                print(f'  {pos + 1:<13}{dado["nome_ap"]:<26}')

    - *excluir_apoartamento*: Recebe como paramêtro uma lista, no momento, não retorna nada.
 
      A função vai apenas excluir o apartamento cadastrado na lista, referente a opção que o usuário digitar.
 
      OBS: Futuramente, vou remover a chamada da função exibir_apartamentos(list) e o input que faço o usuário digitar, quero deixar apenas o for para remover e me retornar a lista atual e passar como parametro a lista + o index do apartamento que vai ser excluido.
 
      
 
          def excluir_apartamento(list):
            exibir_apartamentos(list)
            opcao = leiaInt("Digite o número do apartamento que deseja excluir: ")
            opcao -= 1
            for pos, dado in enumerate(list):
                if opcao == pos:
                    list.pop(opcao)
                    print(f'Apartamento {dado["nome_ap"]} Removido com sucesso!')
    
    - *editar_apartamento_completo*: Recebe como parâmetro uma lista e a posição do index que desejo alterar, o retorno é a subistituição total dos dados de um apartamento dentro da lista.
 
      A função no momento, vai apenas subistituir todos os dados do apartamento que foi passado no parâmetro.

      OBS: No momento, estou pensando sobre a função de Editar todos os dados de um apartamento e editar apenas um dado especifico, eu estava pensando em juntar tudo em uma função, mas acho que vou acabar fazendo outra função para editar o dado manualmente.
 
          def editar_apartamento_completo(list, posicao):
            dado_ap = dict()
            dado_ap['nome_ap'] = leiaStr('Digite o nome do apartamento: ')
            dado_ap['quant_quarto'] = leiaInt('Digite a quantidade de quartos: ')
            dado_ap['quant_cozinha'] = leiaInt('Digite a quantidade de cozinhas: ')
            dado_ap['quan_banheiro'] = leiaInt('Digite a quantidade de banheiros: ')
            dado_ap['quan_cama'] = leiaInt('Digite a quantidade de camas: ')
            if dado_ap['quan_cama'] > 0:
                for i in range(dado_ap['quan_cama']):
                    dado_ap['tipo_cama'] = leiaStr(f'Digite o tipo da {i + 1} cama: ')
            list[posicao] = dado_ap.copy()
            print('Apartamento Editado com sucesso!')
            return list

      OBS: Referente aos nomes de variaveis, planejo fazer algumas mudanças futuramente, para seguir um padrão


- 📅 06/09/2025: Foi feito uma mudança em relação a organização dos arquivos, agora vou deixar o projeto separado por pastas, com o nome da versão(version_0X),
  até chegar no produto final. A ideia é ir documentando as mudanças feitas a cada dia durante a criação do projeto e explicar o por que delas também.

  A respeito da estrutura do projeto, a ideia inicial que tive no momento, foi a criação dinâmica do menu, já que a forma que posso apresentar a minha solução no momento, vai ser pelo prompt.
  
  A principio, pensei em separar as funcionaliades em um menu principal e subs_menu, o menu principal vai disponibilizar as opções de:
  
    - 1 Cadastrar Apartamento
    - 2 Cadastrar Cliente
    - 3 Sair do Programa
   
  O primeiro sub_menu, vai ter essas duas variações (Apartamento e Cliente):
  
    1°
    
    - 1 Cadastrar Apartamento           
    - 2 Exibir Apartamento              
    - 3 Excluir Apartamento             
    - 4 Voltar ao menu principal        
  
   2°
   
    - 1 Cadastrar Cliente
    - 2 Exibir Cliente
    - 3 Excluir Cliente
    - 4 Voltar ao menu principal
        
  O segundo sub_menu a ideia dele, seria utilizar a fução de exibir, para mostrar apenas a posição que esta cadastrado e o nome do apartamento/cliente e após exibir, mostrar 2 opções para o usuário:
  
    - Digite o número do apartamento/cliente que deseja visualizar mais informações:
    - (Número/Palavra) para voltar ao menu principal
  
  Caso o cliente informe o número do apartamento/cliente é exibido todas informações do cadastro e após exibir os valores, pergunta para o usuário se ele deseja fazer alguma alteração, se ele escrever sim, vai para o proximo sub_menu se não, volta para o menu principal:
  
  - Deseja realizar alguma alteração(S/N)?
  
  O penúltimo sub_menu, daria duas opções, a primeira eu ia pedir para o usuário digitar todas as informações novamente, subistituindo os dados atuais e a segunda, seria dar a opção do usuário editar uma informação especifica:
  
   - 1 Editar todos os dados: 
   - 2 Editar um dado especifico: 
  
  Ultimo menu teria duas versões(Apartamento/Cliente):
  
  1°
  
    - 1 Nome do apartamento
    - 2 Quantidade de quartos:
    - 3 Quantidade de cozinha:
    - 4 Quantidade de banheiro:
    - 5 Quantidade de cama:
    - 6 Tipo de cama (essa opção só vai aparecer se tiver pelo menos 1 em quantidade de cama)
    
  
  2° 
  
    - 1 Nome completo:
    - 2 CPF ou FTID (outro país):
    - 3 Número de telefone:
    - 4 Telefone de emergência:
    - 5 E-mail:
    - 6 Placa do carro:
    - 7 País:
    - 8 Estado:
    - 9 Endereço:
  
  OBS: Como comentei, essa é a forma inicial que pensei no projeto, ao decorrer do desenvolvimento, se eu encontrar uma forma melhor irei fazer e documentar.

  Referente as mudanças feitas, no dia 06, foi implementando apenas a estrutura inicial do projeto, que foi criar os módulo de "interface", "apartament", "customer" e "tests" para facilitar na correção e implementação de melhorias dentro do código e dentro desses módulos,
  no momento as funcionalidades que estão operando são:

  - Módulo Tests:
    
    Funções:
    
      - *leiaInt*: Recebe como parâmetro um valor e retorna esse valor como um número inteiro, caso ele passe na validação.

        A função, verifica se valor passado é um número do tipo inteiro, se ele for, retorna esse valor, se não, ele informa que o valor digitado não é um número válido e manda o usuário digitar novamente, até ser digitado um valor válido.

            def leiaInt(valor):
              """
              -> Função para validar o input de um número do tipo inteiro
              :param valor: uma string digitada pelo usuário
              :return: um valor int
              """
              while True:
                  try:
                      v = int(input(valor))
                  except (ValueError, TypeError):
                      print(f'ERRO: por favor, digite um número interio válido.')
                      continue
                  except KeyboardInterrupt:
                      print(f'\nO usuário preferiu não informar os dados.')
                  else:
                      return v
        
      - *leiaStr*: Recebe como parâmetro um texto e faz uma validação, se ele passar, a função retorna o texto.

        A função, verifica se dentro desse texto, possui apenas números, se não possuir, faz a ultima validação que verifica se possui algum caracter inválido """!@#$%^&*()_+=[]{}|\/:;"'<>,.?`~""". Caso o texto passe nas validações, a função retorna esse texto e caso o texto não passe
        é exibido uma mensagem de erro, pedindo para o usuário digitar novamente o texto até esse texto passar por todas as validações.

             def leiaStr(txt):
                caracteres_invalidos = """!@#$%^&*()_+=[]{}|\/:;"'<>,.?`~"""
                while True:
                    vT = str(input(txt))
                    if not vT.isdecimal():
                        if not any(c in caracteres_invalidos for c in vT):
                            return vT
                    else:
                        print(f'{vT} Não é um nome válido, digite novamente!')
   - Módulo Interface:
             
     Funções:
     
     - *linha*: retorna uma string multiplicada pelo tamanho contido no paramêtro da função, que se chama 'tamanho'.
     
       No momento não fazendo o usuário interagir com essa função, então deixei para o tamanho receber o valor de 42 como parâmetro opcional que seria mais ou menos o tamanho
       padrão que quero que fique nos menus;
       
            def linha(tamanho=42):
              return '-' * tamanho
       
     - *cabecalho*: não possui retorno e recebe como parâmetro uma string, a função em si, apenas vai exibir 3 prints.
     
        O primeiro e o ultimo print chamam a função chamada 'linha' sem nada no parâmetro e o print do meio, vai pegar a string que foi passada no parâmetro da função, deixando ela centralizada em 42 para se posicionar com as linhas;

            def cabecalho(txt):
              print(linha())
              print(txt.center(42))
              print(linha())


     - *exibeMenu*: recebe como parâmetro uma lista com os nomes que vão estar no menu e vai retornar um número do tipo inteiro, referente a opção que o usuário digitou da lista.

        A função em si, cria a interface principal do menu, usando a função 'cabecalho' com o parâmetro de uma string do nome que quero exibir, após isso, o for vai percorrer a lista que recebi como parâmetro, exibindo um print com a posição e o item da lista(string), após exibir todos os itens, é chamado a função 'linha'
        e peço para o usuário digitar a opção que ele deseja utilizar e verifico se o que ele digitou é um número do tipo inteiro através da função leiaInt, se o que ele digitou não for um número inteiro, vou deixar ele dentro de um laço de repetição até dele digitar um valor válido.
        Após ele digitar o valor valido, retorno esse valor.

            def exibeMenu(lista):
              cabecalho('MENU PRINCIPAL')
              contador = 1
              for item in lista:
                  print(f'{contador} - {item}')
                  contador += 1
              print(linha())
              opcao = leiaInt(f'Sua Opção: ')
              return opcao

  - Módulo Apartament:
    
    Funções:
    
    - *cadastrar_apartamento*: Recebe como parâmetro uma lista e adiciona dentro dessa lista, um dicionário contendo as informações de um apartamento.

      Durante a inserção das informações de um apartamento, faço uma validação com as funções leiaInt e leiaStr antes de passar os valores para dentro do dicionário, caso não passe na validação, o usuário precisa digitar novamente até escrever um valor válido..

          def cadastrar_apartamento(list):
            dado_ap = dict()
            dado_ap['nome_ap'] = leiaStr('Digite o nome do apartamento: ')
            dado_ap['quant_quarto'] = leiaInt('Digite a quantidade de quartos: ')
            dado_ap['quant_cozinha'] = leiaInt('Digite a quantidade de cozinhas: ')
            dado_ap['quan_banheiro'] = leiaInt('Digite a quantidade de banheiros: ')
            dado_ap['quan_cama'] = leiaInt('Digite a quantidade de camas ')
            if dado_ap['quan_cama'] > 0:
                for i in range(dado_ap['quan_cama']):
                    dado_ap['tipo_cama'] = leiaStr(f'Digite o tipo da {i+1} cama: ')
            list.append(dado_ap.copy())
            return list

- 📅 05/09/2025: Primeiro commit do projeto, com apenas os arquivos base.
