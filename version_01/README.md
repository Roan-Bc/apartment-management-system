#  Versão 1.0 🏢 Apartment Management System

---
  
## 🛠️ Roadmap de Desenvolvimento


### ✅ Versão 1 (atual)

📅 09/09/2025: Hoje foi feito a criação de algumas funções no módulo customer, assim como algumas funções de validação no módulo tests, vou explicar em mais detalhes no texto abaixo:
  
  Referente as novas funções adicionadas no módulo *customer*

- *carregar_clientes* e *salvar_clientes*: Assim como foi feito no módulo de cadastro de apartamentos, como estou querendo salvar minha lista de clientes dentro de um arquivo .json, a lógica para realizar o procedimento é a mesma.
  
  *carregar_clientes*: O arquivo definido na constante é aberto no modo leitura. Se o arquivo não existir ou estiver vazio/corrompido, a função retorna uma lista vazia, evitando que o programa quebre. Importante: o arquivo só será criado quando a lista for salva pela primeira vez usando a função

  *salvar_clientes*: A lista de clientes é convertida para JSON e salva no arquivo. Sempre que for necessário modificar a lista, é preciso chamar primeiro carregar_clientes, garantindo que os dados atuais sejam carregados corretamente. Após as alterações, a lista é passada para salvar_clientes, que atualiza o arquivo e mantém os dados sincronizados entre o programa e o arquivo JSON.

     ```python
        from version_01.modulos.tests import *
        from version_01.modulos.interface import linha, cabecalho
        import json
        
        CAMINHO_JSON = "dados/lista_clientes.json"
        
        def carregar_clientes():
        
            try:
                with open(CAMINHO_JSON, "r", encoding="utf-8") as file:
                    return json.load(file)
            except (FileNotFoundError, json.JSONDecodeError):
                return []
        
        
        def salvar_clientes(lista_clientes):
        
            with open(CAMINHO_JSON, "w", encoding="utf-8") as file:
                json.dump(lista_clientes, file, indent=4, ensure_ascii=False)
     ```
- *cadstrar_cliente*: A função não recebe nenhum parâmetro e também não retorna valor.

   A lógica dela é praticamente a mesma utilizada para cadastrar um apartamento: eu inicio a função chamando a função carregar_clientes para converter o conteúdo do arquivo .json em uma variável local chamada lista_clientes. Em seguida, crio um dicionário para armazenar os dados do cliente e, após finalizar o cadastro, salvo a alteração/incremento da lista utilizando a função salvar_clientes.

  Porém, diferente de um apartamento, os dados de um cliente são mais complexos. Minha ideia inicial foi implementar dessa forma, mas durante o desenvolvimento percebi que será necessário realizar diversas validações. Um exemplo é o id_fiscal (no Brasil, conhecido como CPF), que possui 11 dígitos, mas em outros países recebe nomes e formatos diferentes. O mesmo ocorre com informações como número de telefone e e-mail.

  Inicialmente, minha ideia era realizar todas as validações manualmente, mas dependendo do escopo, estou considerando utilizar bibliotecas específicas para auxiliar nesse processo. No momento, estou avaliando se mantenho o projeto com um escopo nacional — focado apenas em validações de dados no Brasil, com verificações simples para usuários de fora — ou se amplio para um escopo internacional, priorizando os países que mais fazem turismo no Brasil.

    ```python
        def cadastrar_cliente():
          lista_clientes = carregar_clientes()
      
          cliente = dict()
      
          cliente['nome'] = leiaStr("Digite o seu nome completo: ")
          cliente['pais'] = leiaStr("Digite seu pais: ")
          cliente['estado'] = leiaStr("Digite seu estado: ")
          cliente['endereco'] = leiaStr("Digite seu endereco: ")
          cliente['id_fiscal'] = verifica_idFiscal(cliente['pais'])
          cliente['numero_telefone'] = verifica_Telefone("Digite o seu número de telefone: ")
          cliente['numero_telefone_emergencia'] = verifica_Telefone("Digite o seu número de telefone de emergência: ")
          cliente['idade'] = leiaInt("Digite sua idade: ")
          cliente['email'] = verifica_Email("Digite sua email: ")
      
          lista_clientes.append(cliente)
          salvar_clientes(lista_clientes)
          print(linha())
          print('Cliente cadastrado com sucesso!')
          print(linha())
    ```
- *exibir_clientes*: A função não possui parâmetros no escopo e não retorna nenhum valor.
  
   A lógica dela é semelhante à função exibir_apartamentos: inicio chamando a função carregar_clientes para converter o conteúdo do arquivo em uma lista, atribuo essa lista à variável local lista_clientes, percorro posição e valor dentro dessa lista e exibo a posição, o nome e o id_fiscal de cada cliente cadastrado.

   Atualmente, estou enfrentando um problema visual: dependendo do tamanho do nome, a saída do print fica desorganizada. No momento, encontrei uma solução temporária que resolve parcialmente, mas ainda pretendo implementar uma forma melhor de exibição futuramente.

     ```python
      def exibir_clientes():
        lista_clientes = carregar_clientes()
        tamanho = (len(lista_clientes[0]['nome'])) + 4
        print(f'{"Numero":<{tamanho}}{"  Nome":<{tamanho}}{"  ID Fiscal":<{tamanho}}')
        print(linha())
        for pos, dado in enumerate(lista_clientes):
            print(f'  {pos + 1:<{tamanho}}{dado["nome"]:<{tamanho}}{dado["id_fiscal"]:<{tamanho}}')
     ```
Novas funções no módulo *tests*:

- *verifica_Email*: A função recebe um e-mail como parâmetro e retorna o e-mail validado.

  Como mencionei em textos anteriores, ainda estou avaliando a melhor forma de lidar com as validações. A forma atual que implementei serve apenas para garantir que o e-mail possua, no máximo, um caractere @ e um ponto (.). Essa abordagem é bem simples e não cobre todos os casos reais, mas para fins de teste nas funções de cadastro e edição de clientes já atende temporariamente.
    ```python
    
       def verifica_Email(email):
        #Função no momento está incompleta, mas vai servir para fazer os testes minimos dentro das funções.
        while True:
            test_email = str(input(email))
            if "@" in test_email and "." in test_email.split("@")[-1]:
                return test_email
            else:
                print('E-mail inválido, digite novamente!')
     ```
  
- *verifica_Telefone*: A função recebe um número de telefone e retorna o número validado.

     A forma atual que implementei serve apenas para garantir que o telefone possua, no máximo, uma quantidade x de caracteres e que todos sejam dígitos de 0 a 9. Essa abordagem é bem simples e não cobre todos os casos reais, mas, para fins de teste nas funções de cadastro e edição de clientes, já atende temporariamente.

  ```python
    def verifica_Telefone(telefone):
      # Função no momento está incompleta, mas vai servir para fazer os testes mínimos dentro das funções.
      formato = '54111512345678'
      while True:
          test_numero = str(input(telefone))
          if len(test_numero) <= len(formato) and test_numero.isdecimal():
              return test_numero
          else:
              print('Número de telefone inválido, digite novamente!')
    ```

  
- *verifica_idFiscal*: A função recebe como parâmetro o nome de um país. Caso não seja informado, por padrão é atribuído o valor Brasil. Ela retorna o id_fiscal referente ao país informado.

   De forma simplificada, a função verifica o nome do país passado como parâmetro e, se ele estiver em um dos cases, executa uma segunda função responsável por validar o id_fiscal.
  
  OBS: No momento, apenas o case do Brasil está implementado.

  ```python
    def verifica_idFiscal(pais='Brasil'):

      match pais:
  
          case 'Brasil':
              id = 'CPF'
              doc = verificaDoc(id)
              return doc
          case 'Argentina':
              id = 'CUIT'
          case 'Uruguai':
              id = 'RUT'
          case 'Paraguai':
              id = 'RUC'
          case 'Chile':
              id = 'RUT '
          case 'Estados Unidos':
              id = 'SSN'
          case 'Alemanha':
              id ='IdNr'
          case 'Reino Unido':
              id = 'NIN'
          case 'França':
              id = 'NFR'
          case 'Itália':
              id = 'CF'

    ```

  
- *verificaDoc*: A função recebe como parâmetro um id e retorna o id_fiscal validado para a função verifica_idFiscal.

  Resumidamente, essa função verifica qual case corresponde ao id informado. Caso encontre, entra em um loop pedindo ao usuário que digite o id_fiscal no formato esperado. Se o valor informado for válido, a função retorna o id_fiscal para a função verifica_idFiscal. Caso contrário, o usuário permanece no loop até fornecer um dado válido.

  OBS: Essa validação ainda não está 100% correta, pois não é possível verificar se o CPF realmente existe ou a quem está associado. No entanto, para fins de implementação das funções de cadastro e edição de clientes, essa abordagem já atende temporariamente.

  ```python
  def verificaDoc(id):
    match id:

        case 'CPF':
            formato = '00000000000'
            while True:
               doc = str(input(f'Digite seu {id} nesse formato "{formato}": '))
               if doc.isdecimal() and len(doc) == len(formato):
                   return doc
               else:
                    print(f'{id} inválido, por favor, digite novamente!')


    """
        case 'CUIT':

        case 'RUT':

        case 'RUC':

        case 'RUT ':

        case 'SSN':

        case 'IdNr':

        case 'NIN':

        case 'NFR':

        case 'CF':
    """
    ```

📅 08/09/2025: Hoje teve bastante mudança no projeto, então vou explicar por partes o que foi desenvolvido até agora.

  ⏰ Do período das 17:00 até as 20:00, estava pensando se terminava as funções do módulo de clientes, mas acabei querendo implementar alguma forma de salvar as minhas listas em algum documento, para ficar mais fácil de fazer testes e deixar o programa mais "completo". Então, precisei pesquisar a respeito de como fazer e fiquei entre três tipos de arquivo para armazenar as listas: TXT, CSV e JSON.

  Como pretendo fazer integração com API futuramente no projeto e estava bastante curioso para estudar esse tipo de formato, decidi salvar as informações das listas em arquivo .json.

  OBS: Mais tarde, descobri que além do JSON ser um dos melhores formatos para trabalhar com listas e dicionários, ele possui uma integração muito boa com bancos de dados

  E para conseguir desenvolver essa proposta, precisei pesquisar a documentação, assistir alguns vídeos no YouTube e fazer testes em outro programa, com auxílio do ChatGPT, para verificar o motivo de alguns erros.

  Agora vou explicar as principais mudanças e o motivo de cada uma delas.

 - *Mudança no módulo de apartamento*:

   A principal mudança desse módulo foi alterar todas as funções relacionadas ao gerenciamento de apartamentos e o arquivo index.
  
   Foi necessário importar a biblioteca json e criar uma constante (CAMINHO_JSON) indicando o caminho do arquivo onde a lista de apartamentos será salva.
  
   Na função carregar_apartamentos, o arquivo definido na constante é aberto no modo leitura. Se o arquivo não existir ou estiver vazio/corrompido, a função retorna uma lista vazia, evitando que o programa quebre. Importante: o arquivo só será criado quando a lista for salva pela primeira vez usando a função salvar_apartamentos.
  
   Essa função é útil porque, ao chamá-la antes de qualquer operação (como cadastrar, editar ou excluir um apartamento), garante que a lista mais atual seja carregada e utilizada, evitando sobrescrever dados anteriores.

   Como estamos trabalhando com JSON, não é mais necessário criar a lista manualmente no index. A função carregar_apartamentos passa a ser responsável tanto por criar a lista quanto por converter JSON para lista e vice-versa.
  
   Na função salvar_apartamentos, a lista de apartamentos é convertida para JSON e salva no arquivo. Sempre que for necessário modificar a lista, é preciso chamar primeiro carregar_apartamentos, garantindo que os dados atuais sejam carregados corretamente. Após as alterações, a lista é passada para salvar_apartamentos, que atualiza o arquivo, mantendo os dados sincronizados entre o programa e o arquivo JSON.
  
  
    ```python
    
            from version_01.modulos.tests import leiaInt, leiaStr
            from version_01.modulos.interface import linha, cabecalho
            import json
            
            CAMINHO_JSON = "dados/cadastro.json"
            
            def carregar_apartamentos():
            
                try:
                    with open(CAMINHO_JSON, "r", encoding="utf-8") as file:
                        return json.load(file)
                except (FileNotFoundError, json.JSONDecodeError):
                    return []
            
            
            def salvar_apartamentos(lista_apartamentos):
            
                with open(CAMINHO_JSON, "w", encoding="utf-8") as file:
                    json.dump(lista_apartamentos, file, indent=4, ensure_ascii=False)
    ```
  - *cadastrar_apartamento*: Como explicado acima, devido às novas funções que permitem salvar todo o progresso da lista no arquivo .json, houve uma mudança na estrutura da função.

    Agora, ela não recebe mais parâmetros e funciona da seguinte forma: a função é iniciada com a variável local lista_apartamentos, que recebe a conversão do arquivo .json para lista. Em seguida, é realizado o cadastro de um novo apartamento, e essa alteração é salva usando a função salvar_apartamentos(lista_apartamentos).

    OBS: Como precisei alterar bastante código, percebi que estava começando a ter problemas com o nome de parâmetros e variáveis que estava usando, como lista e key. Por isso, acabei trocando-os para evitar que o Python associasse esses nomes a tipos internos, como list ou key.
      ```python
            def cadastrar_apartamento():
              lista_apartamentos = carregar_apartamentos()
          
              dado_ap = dict()
              dado_ap['nome_ap'] = leiaStr('Digite o nome do apartamento: ')
              dado_ap['quant_quarto'] = leiaInt('Digite a quantidade de quartos: ')
              dado_ap['quant_cozinha'] = leiaInt('Digite a quantidade de cozinhas: ')
              dado_ap['quant_banheiro'] = leiaInt('Digite a quantidade de banheiros: ')
              dado_ap['quant_cama'] = leiaInt('Digite a quantidade de camas: ')
          
              if dado_ap['quant_cama'] > 0:
                  tipos = []
                  for i in range(dado_ap['quant_cama']):
                      tipos.append(leiaStr(f'Digite o modelo da {i + 1}ª cama: '))
                  dado_ap['tipo_cama'] = tipos
          
              lista_apartamentos.append(dado_ap)
              salvar_apartamentos(lista_apartamentos)
              print(linha())
              print('Apartamento cadastrado com sucesso!')
              print(linha())
       ```
      
- *exibir_apartamentos*: A mudança realizada nessa função foi que agora ela não recebe nenhum parâmetro. É necessário chamar a função carregar_apartamentos para salvar a lista de apartamentos em uma variável local e, em seguida, exibir a lista de apartamentos cadastrados usando essa variável.

    ```python
      def exibir_apartamentos():
        lista_apartamentos = carregar_apartamentos()
    
        print(f'{"Numero"}{"Apartamento":>20}')
        print(linha())
        for pos, dado in enumerate(lista_apartamentos):
            print(f'  {pos + 1:<13}{dado["nome_ap"]:<26}')
     ```
- *exibir_detalhes_apartamento*: A mudança realizada nessa função foi que agora ela recebe apenas a posição como parâmetro. Também é necessário chamar a função carregar_apartamentos para salvar a lista de apartamentos em uma variável local e exibir a lista de apartamentos cadastrados usando essa variável.
    ```python
      def exibir_detalhes_apartamento(pos):
        lista_apartamentos = carregar_apartamentos()
        dado = lista_apartamentos[pos]
        tamanho = (len(dado['nome_ap'])) + 4
        if dado['quant_cama'] > 0:
            tipos = ', '.join(dado["tipo_cama"])
  
        print(linha())
        print(f'{dado["nome_ap"]:<{tamanho}} {dado["quant_quarto"]:<7} {dado["quant_cozinha"]:<7} {dado["quant_banheiro"]:<7} {dado["quant_cama"]:<7} {tipos:<7}')
     ```
- *excluir_apartamento*: Houve várias mudanças nessa função. Uma delas foi remover a validação interna da posição do apartamento. Antes, a função recebia a lista como parâmetro e pedia para o usuário informar a posição do apartamento que desejava excluir. Agora, o usuário deve digitar a posição antes de chamar a função; em seguida, é verificado se essa posição realmente existe, e ela é passada como parâmetro para a função, que então realiza a exclusão do apartamento.

    Além dessa mudança, houve outra alteração padrão: a função agora chama carregar_apartamentos e salva o resultado em uma variável local (lista_apartamentos = carregar_apartamentos()). Em seguida, a exclusão do apartamento é realizada usando o parâmetro passado, e a lista modificada é salva novamente chamando salvar_apartamentos(lista_apartamentos).

     ```python
      def excluir_apartamento(pos):
        lista_apartamentos = carregar_apartamentos()
        print(linha())
        print(f'Apartamento {lista_apartamentos[pos]["nome_ap"]} Removido com sucesso!')
        print(linha())
        lista_apartamentos.pop(pos)
        salvar_apartamentos(lista_apartamentos)
     ```
- *editar_todo_apartamento*: As mudanças realizadas nessa função foram, basicamente, a implementação das funções carregar_apartamentos e salvar_apartamentos, a alteração para que o parâmetro seja apenas a posição do apartamento e a modificação de nomes de algumas variáveis, como dado_ap, que passou a se chamar apartamento.

     ```python

      def editar_todo_apartamento(posicao):
        lista_apartamentos = carregar_apartamentos()
        apartamento = dict()
        apartamento['nome_ap'] = leiaStr('Digite o nome do apartamento: ')
        apartamento['quant_quarto'] = leiaInt('Digite a quantidade de quartos: ')
        apartamento['quant_cozinha'] = leiaInt('Digite a quantidade de cozinhas: ')
        apartamento['quant_banheiro'] = leiaInt('Digite a quantidade de banheiros: ')
        apartamento['quant_cama'] = leiaInt('Digite a quantidade de camas: ')
    
        if apartamento['quant_cama'] > 0:
            tipos = []
            for i in range(apartamento['quant_cama']):
                tipos.append(leiaStr(f'Digite o modelo da {i + 1}° cama: '))
            apartamento['tipo_cama'] = tipos[:]
    
        lista_apartamentos[posicao] = apartamento.copy()
        print(linha())
        print('Apartamento Editado com sucesso!')
        print(linha())
        salvar_apartamentos(lista_apartamentos)
     ```
- *editar_dado_apartamento*: As mudanças realizadas nessa função foram, basicamente, a implementação das funções carregar_apartamentos e salvar_apartamentos, a remoção da lista como parâmetro da função e a alteração do nome da variável e do parâmetro key para chave.

    ```python
        def editar_dado_apartamento(pos, chave, txt):
          lista_apartamentos = carregar_apartamentos()
          if chave == 'quant_cama':
              lista_apartamentos[pos][chave] = leiaInt('Digite a quantidade de camas: ')
              if lista_apartamentos[pos][chave] > 0:
                  tipos = []
                  for i in range(lista_apartamentos[pos][chave]):
                      tipos.append(leiaStr(f'Digite o modelo da {i + 1}° cama: '))
                  lista_apartamentos[pos]['tipo_cama'] = tipos[:]
      
          elif chave == 'tipo_cama':
              tipos = []
              for i in range (lista_apartamentos[pos]['quant_cama']):
                  tipos.append(leiaStr(f'Digite o modelo da {i + 1}° cama: '))
              lista_apartamentos[pos][chave] = tipos[:]
      
          elif chave == 'nome_ap':
              lista_apartamentos[pos][chave] = leiaStr(f'Digite o {txt}: ')
          else:
              lista_apartamentos[pos][chave] = leiaInt(f'Digite a {txt}: ')
      
          print(linha())
          print('Apartamento editado com sucesso!')
          print(linha())
          salvar_apartamentos(lista_apartamentos)
     ```
- *index*: As mudanças realizadas no arquivo principal foram a remoção da variável global apartamento = list(). Como eu utilizava essa variável para verificar o tamanho da lista, foi necessário declarar a variável em alguns trechos do menu, atribuindo a ela o retorno da função carregar_apartamentos() para poder realizar a verificação usando len(). Além disso, foi adicionada uma validação da posição do apartamento antes de chamar a função excluir_apartamento.
  
    ```python
    
          from modulos.interface import *
          from modulos.apartment import *
    
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
    ```                                    
   --- 
 ⏰ Do período das 09:00 até as 16:00, finalizei as funções restantes, ajustei algumas já existentes e modifiquei o arquivo index e o módulo de interface para melhorar o espaçamento entre os menus.

 As principais mudanças foram:

- *index*: Alterações focadas na parte visual do projeto, renomeando menus, submenus e algumas funções para facilitar a localização. Também foi adicionado um parâmetro para exibir o nome correto no menu ou submenu dentro da função exibeMenu.

  OBS: Nessa versão, utilizei print antes e depois do menu para testar o espaçamento. Posteriormente, esses prints foram incorporados diretamente na função exibeMenu.


  ```python
      apartamento = list()
      
      while True:
          main_menu = exibeMenu(['Apartamento', 'Cliente', 'Sair do sistema'], 'Residencial Costão da Gamboa')
          match main_menu:
              case 1:
      
                  while True:
                      print()
                      sub_menu = exibeMenu(['Cadastrar Apartamento ', 'Exibir Apartamentos', 'Editar Apartamento','Excluir Apartamentos', 'Voltar ao menu'],'Menu apartamento')
                      print()
                      match sub_menu:
                          case 1:
                              cabecalho('Cadastro apartamento')
                              cadastrar_apartamento(apartamento)
      
                          case 2:
                              if len(apartamento) > 0:
                                  cabecalho('Lista dos apartamentos')
                                  exibir_apartamentos(apartamento)
                                  print(linha())
  
  
   ```
- *cadastrar_apartamento*: Chave ['tipo_cama']: Foi feita uma pequena alteração explicada na função editar_todo_apartamento. Além disso, algumas chaves dos dicionários foram renomeadas para manter um padrão, como quant_quarto, quant_cozinha, quant_banheiro etc.
    ```python    
        def cadastrar_apartamento(list):
           dado_ap['nome_ap'] = leiaStr('Digite o nome do apartamento: ')
            dado_ap['quant_quarto'] = leiaInt('Digite a quantidade de quartos: ')
            dado_ap['quant_cozinha'] = leiaInt('Digite a quantidade de cozinhas: ')
            dado_ap['quant_banheiro'] = leiaInt('Digite a quantidade de banheiros: ')
            dado_ap['quant_cama'] = leiaInt('Digite a quantidade de camas: ')
            if dado_ap['quant_cama'] > 0:
                tipos = []
                for i in range(dado_ap['quant_cama']):
                    tipos.append(leiaStr(f'Digite o modelo da {i+1} cama: '))
                dado_ap['tipo_cama'] = tipos[:]
            list.append(dado_ap.copy())
            print(linha())
            print('Apartamento cadastrado com sucesso!')
            print(linha())
            return list
    ```
- *exibir_detalhes_apartamento*: Nova função que recebe uma lista e posição, sem retorno. Foi criada para exibir os resultados de forma visualmente mais agradável no prompt, mesmo já existindo uma função que exibe a lista de apartamentos.

- *excluir_apartamento*: Adicionei apenas o return da lista após a exclusão de um apartamento.

- *editar_todo_apartamento*: EEsta função passou por grandes alterações, incluindo mudança de nome (antes era editar_apartamento_completo) e na estrutura. Por causa da chave tipo_cama, precisei ajustar para receber uma lista e armazenar cada tipo de cama corretamente, evitando problemas caso houvesse mais de uma cama.
    ```python   
        def editar_todo_apartamento(list, posicao):
          dado_ap = dict()
          dado_ap['nome_ap'] = leiaStr('Digite o nome do apartamento: ')
          dado_ap['quant_quarto'] = leiaInt('Digite a quantidade de quartos: ')
          dado_ap['quant_cozinha'] = leiaInt('Digite a quantidade de cozinhas: ')
          dado_ap['quant_banheiro'] = leiaInt('Digite a quantidade de banheiros: ')
          dado_ap['quant_cama'] = leiaInt('Digite a quantidade de camas: ')
          if dado_ap['quant_cama'] > 0:
              tipos = []
              for i in range(dado_ap['quant_cama']):
                  tipos.append(leiaStr(f'Digite o modelo da {i + 1}° cama: '))
              dado_ap['tipo_cama'] = tipos[:]
          list[posicao] = dado_ap.copy()
          print(linha())
          print('Apartamento Editado com sucesso!')
          print(linha())
          return list
    ```

- *editar_dado_apartamento:*: Nova função que recebe lista, posição, chave (key) e texto (txt) e retorna a lista com a alteração feita. Permite que o usuário escolha entre alterar todos os dados do apartamento ou apenas um dado específico.
    ```python 
        def editar_dado_apartamento(list, pos, key, txt):
        
            if key == 'quant_cama':
                list[pos][key] = leiaInt('Digite a quantidade de camas: ')
                if list[pos][key] > 0:
                    tipos = []
                    for i in range(list[pos][key]):
                        tipos.append(leiaStr(f'Digite o modelo da {i + 1}° cama: '))
                    list[pos]['tipo_cama'] = tipos[:]
        
            elif key == 'tipo_cama':
                tipos = []
                for i in range (list[pos]['quant_cama']):
                    tipos.append(leiaStr(f'Digite o modelo da {i + 1}° cama: '))
                list[pos][key] = tipos[:]
        
            elif key == 'nome_ap':
                list[pos][key] = leiaStr(f'Digite o {txt}: ')
            else:
                list[pos][key] = leiaInt(f'Digite a {txt}: ')
        
            print(linha())
            print('Apartamento editado com sucesso!')
            print(linha())
            return list
    ```
 📅 07/09/2025: Hoje também implementei a estrutura inicial de alguns submenus e finalizei as funções de exibir, editar e excluir apartamentos. A princípio está funcionando, mas quero fazer algumas modificações amanhã para melhorar ainda mais.
  
 -  Referente à estrutura de menu e submenus, a princípio está assim:
  
    ```python 
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
          
    ```
  
    Agora, referente às novas funções que criei no módulo Apartamento, foram estas:
    
    Funções:
  
    - *exibir_apartamentos*: Recebe como parâmetro uma lista e não possui retorno.

      A função basicamente vai exibir, via print, a posição e o nome de cada apartamento até não haver mais nenhum para mostrar.

      OBS: Por enquanto, só estou exibindo a posição e o nome, mas ainda estou pensando se vou exibir todas as informações de uma vez ou se pedirei para o usuário selecionar um apartamento específico e, então, exibir todas as informações referentes a ele.
       ```python 
                def exibir_apartamentos(list):
                  print(f'{"Numero"}{"Apartamento":>20}')
                  print(linha())
                  for pos, dado in enumerate(list):
                      print(f'  {pos + 1:<13}{dado["nome_ap"]:<26}')
       ```
    - *excluir_apoartamento*: Recebe como parâmetro uma lista e, no momento, não retorna nada.
 
      A função vai apenas excluir o apartamento cadastrado na lista, de acordo com a opção que o usuário digitar.
 
      OBS: Futuramente, pretendo remover a chamada da função exibir_apartamentos(list) e o input usado para o usuário digitar. Quero deixar apenas o for para remover o apartamento e retornar a lista atualizada, passando como parâmetro a lista e o índice do apartamento que será excluído.
     
       ```python 
                  def excluir_apartamento(list):
                    exibir_apartamentos(list)
                    opcao = leiaInt("Digite o número do apartamento que deseja excluir: ")
                    opcao -= 1
                    for pos, dado in enumerate(list):
                        if opcao == pos:
                            list.pop(opcao)
                            print(f'Apartamento {dado["nome_ap"]} Removido com sucesso!')
       ```

     - *editar_apartamento_completo*: Recebe como parâmetro uma lista e o índice da posição que desejo alterar. O retorno é a substituição total dos dados de um apartamento dentro da lista..
   
        A função, no momento, substitui todos os dados do apartamento passado como parâmetro.
  
        OBS: Estou refletindo sobre a função de editar todos os dados de um apartamento versus editar apenas um dado específico. Inicialmente, pensei em juntar tudo em uma única função, mas provavelmente acabarei criando uma função separada para editar apenas um dado manualmente.
      
         ```python 
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
      
         ```
📅 06/09/2025: Foi feita uma mudança em relação à organização dos arquivos. Agora, o projeto ficará separado por pastas, com o nome da versão (version_0X), até chegar ao produto final. A ideia é documentar as mudanças feitas a cada dia durante a criação do projeto e explicar o motivo delas.

   A respeito da estrutura do projeto, a ideia inicial foi a criação dinâmica do menu, já que a forma que posso apresentar a solução, no momento, será pelo prompt.
  
   A princípio, pensei em separar as funcionalidades em um menu principal e submenus. O menu principal disponibilizará as seguintes opções:
  
    - 1 Cadastrar Apartamento
    - 2 Cadastrar Cliente
    - 3 Sair do Programa
   
   O primeiro submenu terá duas variações: Apartamento e Cliente.
  
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
        
   O segundo submenu seria utilizado para exibir apenas a posição cadastrada e o nome do apartamento/cliente. Após exibir essas informações, serão mostradas duas opções para o usuário:
  
    - Digite o número do apartamento/cliente que deseja visualizar mais informações:
    - (Número/Palavra) para voltar ao menu principal
  
   Caso o usuário informe o número do apartamento/cliente, todas as informações do cadastro serão exibidas. Depois, será perguntado se ele deseja fazer alguma alteração. Se a resposta for "sim", ele será direcionado para o próximo submenu; caso contrário, retornará ao menu principal.
  
    - Deseja realizar alguma alteração(S/N)?
  
  O penúltimo submenu oferece duas opções: a primeira permite que o usuário digite todas as informações novamente, substituindo os dados atuais; a segunda permite que o usuário edite apenas uma informação específica.
  
     - 1 Editar todos os dados: 
     - 2 Editar um dado especifico: 
  
  O último menu terá duas versões: uma para Apartamento e outra para Cliente.
  
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
  
   OBS: Como comentei, essa é a forma inicial que pensei para o projeto. Ao longo do desenvolvimento, caso eu encontre uma maneira melhor, irei implementá-la e documentá-la.

   Em relação às mudanças feitas, no dia 06, foi implementada apenas a estrutura inicial do projeto, que consistiu em criar os módulos "interface", "apartament", "customer" e "tests". Isso foi feito para facilitar a correção e a implementação de melhorias no código.

   No momento, as funcionalidades que estão operando são:

  - Módulo Tests:
    
    Funções:
    
       - *leiaInt*: Recebe como parâmetro um valor e retorna esse valor como um número inteiro, caso ele passe na validação.

         A função verifica se o valor passado é um número do tipo inteiro. Se for, retorna esse valor; caso contrário, informa que o valor digitado não é válido e solicita que o usuário digite novamente até fornecer um valor correto.
      
         ```python 
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
         ``` 
    - *leiaStr*: Recebe como parâmetro um texto e faz uma validação; se ele passar, a função retorna esse texto.

      A função verifica, primeiro, se o texto contém apenas números. Caso não contenha, faz uma segunda validação para verificar se possui algum caractere inválido (!@#$%^&*()_+=[]{}|\/:;"'<>,.?~`).
Se o texto passar em todas as validações, ele é retornado. Caso contrário, é exibida uma mensagem de erro pedindo para o usuário digitar novamente até que o texto seja válido.

      ```python 
             def leiaStr(txt):
                caracteres_invalidos = """!@#$%^&*()_+=[]{}|\/:;"'<>,.?`~"""
                while True:
                    vT = str(input(txt))
                    if not vT.isdecimal():
                        if not any(c in caracteres_invalidos for c in vT):
                            return vT
                    else:
                        print(f'{vT} Não é um nome válido, digite novamente!')
      ``` 
   - Módulo Interface:
             
     Funções:
     
     - *linha*: Retorna uma string multiplicada pelo tamanho definido no parâmetro da função, chamado tamanho.
     
       No momento, não há interação do usuário com essa função, por isso deixei o parâmetro tamanho com valor opcional de 42, que corresponde aproximadamente ao tamanho padrão que quero utilizar nos menus.
         ```python 
            def linha(tamanho=42):
              return '-' * tamanho
         ``` 
     - *cabecalho*: Não possui retorno e recebe como parâmetro uma string. A função em si apenas exibe três prints.
     
        O primeiro e o último print chamam a função chamada linha sem nenhum parâmetro. Já o print do meio utiliza a string passada como parâmetro da função, deixando-a centralizada em 42 para se alinhar com as linhas.
          ```python 
            def cabecalho(txt):
              print(linha())
              print(txt.center(42))
              print(linha())
          ``` 

     - *exibeMenu*: Recebe como parâmetro uma lista com os nomes que estarão no menu e retorna um número do tipo inteiro, referente à opção que o usuário digitou da lista.

       A função em si cria a interface principal do menu, usando a função cabecalho com o parâmetro de uma string do nome que quero exibir. Após isso, o for percorre a lista recebida como parâmetro, exibindo um print com a posição e o item da lista (string). Depois de exibir todos os itens, é chamada a função linha, e então peço para o usuário digitar a opção que deseja utilizar.
       
       Verifico se o valor digitado é um número do tipo inteiro através da função leiaInt. Caso não seja, mantenho o usuário dentro de um laço de repetição até que ele digite um valor válido.

       Após digitar o valor válido, retorno esse valor.
        ```python 
            def exibeMenu(lista):
              cabecalho('MENU PRINCIPAL')
              contador = 1
              for item in lista:
                  print(f'{contador} - {item}')
                  contador += 1
              print(linha())
              opcao = leiaInt(f'Sua Opção: ')
              return opcao
        ```
  - Módulo Apartament:
    
    Funções:
    
    - *cadastrar_apartamento*: Recebe como parâmetro uma lista e adiciona dentro dessa lista um dicionário contendo as informações de um apartamento.

     Durante a inserção das informações de um apartamento, faço uma validação com as funções leiaInt e leiaStr antes de passar os valores para dentro do dicionário. Caso não passe na validação, o usuário precisa digitar novamente até escrever um valor válido.
      ```python 
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
       ```
📅 05/09/2025: Primeiro commit do projeto, com apenas os arquivos base.
