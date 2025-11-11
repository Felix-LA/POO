from Cliente import Cliente

while True:
    print("SysPerkal")
    print("=" * 30)
    print("Selecione uma opção: ")
    print("1 - Cadastrar Cliente")
    print("2 - Listar CLiente")
    print("3 - Excluir Cliente")
    print("4 - Atualizar")
    print("0 - Sair")
    opcao = input()

    if opcao == '0':##Sair
        break

    elif opcao == '1': ##Cadastrar
        cli = Cliente()
        cli.nome = input("Digite o Nome do Cliente: ")
        cli.cpf = input("Digite o CPF do Cliente: ")
        cli.fone = input("Digite o Fone do Cliente: ")
        cli.cidade = input("Digite a Cidade do Cliente: ")
        result = cli.cadastrar()
        if result == True:
            print("Cadastrado com Sucesso!!!")

    elif opcao == '2': ##Listar
        cli = Cliente()
        result = cli.buscar("cliente")
        print(result)
        
    elif opcao == '3':##Excluir
        cli = Cliente()
        result = cli.buscar("cliente")
        print(result)

        id_Excluir = int(input("Digite o id que deseja excluir: "))
        resultExcluir = cli.excluir(id_Excluir)
        if resultExcluir == True:
            print("Excluido")

    elif opcao == '4':##Atualizar
        cli = Cliente()
        result = cli.buscar("cliente")
        print(result)

        id_Atualizar = int(input("Digite o id que deseja Atualizar: "))
        resultAtualizar = list(cli.buscarPorID(id_Atualizar))
        print(resultAtualizar)
        resultAtualizar[1] = input("Digite o novo Nome: ")
        resultAtualizar[2] = input("Digite o novo CPF: ")
        resultAtualizar[3] = input("Digite o novo Fone: ")
        resultAtualizar[4] = input("Digite o novo Cidade: ")
        atualizacao = cli.update(tuple(resultAtualizar))
        print(resultAtualizar)
        if atualizacao == True:
            print("Cliente Atualizado com Sucesso")
            

