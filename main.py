from modulos import *

if __name__ == "__main__":
    listDimensoes = []
    listEquipes = []
    listColaboradores = []
    listObservacoes = []
    path = str
    try:
        listDimensoes = carregarObjeto('data\\dimensoes.pkl')
        listEquipes = carregarObjeto('data\\equipes.pkl')

        for equipe in listEquipes:
            dimensao_correspondente = next((dimensao for dimensao in listDimensoes if dimensao.nomeDimensaoData == equipe.dimensaoDataEquipe.nomeDimensaoData), None)
            if dimensao_correspondente is not None:
                equipe.dimensaoDataEquipe = dimensao_correspondente

        listColaboradores = carregarObjeto('data\\colaboradores.pkl')

        for colaborador in listColaboradores:
            equipe_correspondente = next((equipe for equipe in listEquipes if equipe.nomeEquipe == colaborador.equipeColaborador.nomeEquipe), None)
            if equipe_correspondente is not None:
                colaborador.equipeColaborador = equipe_correspondente
        
        listObservacoes = carregarObjeto('data\\observacoes.pkl')

        for observacao in listObservacoes:
            equipe_correspondente = next((equipe for equipe in listEquipes if equipe.nomeEquipe == observacao.equipeObservacao.nomeEquipe), None)
            if equipe_correspondente is not None:
                observacao.equipeObservacao = equipe_correspondente
        path = carregarObjeto('data\\path.pkl')

    except Exception as e:
        print(f"Não foi possível importar os objetos.\n{str(e)}")

    while True:
        try:
            op = int(input("\n\tMenu de Controle de Gerencial\n\n1- Controles de Dimensão\n2- Controles de Equipe" + 
                        "\n3- Controles de Colaborador\n4- Controles de Meta\n5- Controles de Observação\n6- Definir caminho de salvamento\n7- Gerar Tabelas do Excel\n8- Sair sem Salvar\n0- Sair e Salvar\n\nSua Opção: "))
            match op:
                case 1:
                    while True:
                        opDim = controlesDimensoes()
                        match opDim:
                            case 1:
                                print(cadastrarDimensao(listDimensoes))
                            case 2:
                                if len(listDimensoes) > 0:
                                    print(removerDimensao(listDimensoes, listEquipes, listColaboradores))
                                else: print("Não há Dimensões cadastradas.")
                            case 3:
                                if len(listDimensoes) > 0:
                                    print(alterarDimensao(listDimensoes))
                                else: print("Não há Dimensões cadastradas.")
                            case 4:
                                if len(listDimensoes) > 0: 
                                    visualizarDimensoes(listDimensoes)
                                else: print("Não há Dimensões cadastradas.")
                            case 0:
                                break
                            case _:
                                print("Opção inválida, entre novamente com uma opção existente.")
                        input()
                case 2:
                    if len(listDimensoes) > 0:
                        while True:
                            opEquipe = controlesEquipe()
                            match opEquipe:
                                case 1:
                                    print(cadastrarEquipe(listEquipes, listDimensoes))
                                case 2:
                                    if len(listEquipes) > 0:
                                        print(removerEquipe(listEquipes, listColaboradores))
                                    else: print("Não há nenhuma equipe cadastrada.")
                                case 3:
                                    if len(listEquipes) > 0:
                                        print(alterarEquipe(listEquipes, listDimensoes))
                                    else: print("Não há nenhuma equipe cadastrada.")
                                case 4:
                                    if len(listEquipes) > 0: visualizarEquipes(listEquipes)
                                    else: print("Não há nenhuma equipe cadastrada.")
                                case 5:
                                    if len(listEquipes) > 0: print(ordenarEquipes(listEquipes))
                                    else: print("Não há nenhuma equipe cadastrada.")
                                case 0:
                                    break
                                case _:
                                    print("Opção inválida, entre novamente com uma opção existente.")
                            input()
                    else: 
                        print("Não há Dimensões cadastradas. Inicie uma dimensão antes de tratar Equipes.")
                        input()
                case 3:
                    if len(listEquipes) > 0:
                        while True:
                            opColaborador = controlesColaborador()
                            match opColaborador:
                                case 1:
                                    print(cadastrarColaborador(listColaboradores, listEquipes))
                                case 2:
                                    if len(listColaboradores) > 0:
                                        print(removerColaborador(listColaboradores))
                                    else: print("Não há nenhum Colaborador cadastrado.")
                                case 3:
                                    if len(listColaboradores) > 0:
                                        print(alterarColaborador(listColaboradores, listEquipes))
                                    else: print("Não há nenhum Colaborador cadastrado.")
                                case 4:
                                    if (len(listColaboradores) > 0): visualizarColaboradores(listColaboradores)
                                    else: print("Não há Colaboradores cadastrados.")
                                case 5:
                                    if (len(listColaboradores) > 0): print(ordenarColaboradores(listColaboradores))
                                    else: print("Não há Colaboradores cadastrados.")
                                case 0:
                                    break
                                case _:
                                    print("Opção inválida, entre novamente com uma opção existente.")
                            input()
                    else: 
                        print("Não é possivel acessar o Menu de Colaboradores sem cadastrar uma Equipe.")
                        input()
                case 4:
                    if len(listColaboradores) > 0:
                        while True:
                            opMetas = controlesMetas()
                            match opMetas:
                                case 1:
                                    print(definirDiasZeradosTodos(listColaboradores))
                                case 2:
                                    print(definirDiasZeradosDim(listDimensoes, listEquipes, listColaboradores))
                                case 3:
                                    print(definirDiasZeradosColab(listColaboradores))
                                case 4:
                                    print(definirDiasMetade(listColaboradores))
                                case 5:
                                    print(removerDiasZeradosTodos(listColaboradores))
                                case 6:
                                    print(removerDiasMetadeTodos(listColaboradores))
                                case 7:
                                    print(removerDiasZeradosColab(listColaboradores))
                                case 8:
                                    print(removerDiasMetadeColab(listColaboradores))
                                case 0:
                                    break
                                case _:
                                    print("Opção inválida, entre novamente com uma opção existente.")
                            input()
                    else: 
                        print("Não é possível acesso o Menu de Metas sem cadastrar Colaboradores.")
                        input()
                case 5:
                    if len(listEquipes) > 0:
                        while True:
                            opObs = controlesObservacoes()
                            match opObs:
                                case 1:
                                    print(cadastrarObservacao(listObservacoes, listEquipes))
                                case 2:
                                    if len(listObservacoes) > 0: print(removerObservacao(listObservacoes))
                                    else: print("Não há nenhuma observação cadastrada.")
                                case 3:
                                    if len(listObservacoes) > 0: print(alterarObservacao(listObservacoes, listEquipes))
                                    else: print("Não há nenhuma observação cadastrada.")
                                case 4:
                                    if len(listObservacoes) > 0: visualizarObservacoes(listObservacoes)
                                    else: print("Não há nenhuma observação cadastrada.")
                                case 5:
                                    try:
                                        listObservacoes.clear()
                                        print(f"As observações foram removidas com sucesso.")
                                    except Exception as e:
                                        print(f"Houve um erro ao limpar a tabela.\n{str(e)}")
                                case 6:
                                    if len(listObservacoes) > 0: print(ordenarObservacoes(listObservacoes))
                                    else: print("Não há nenhuma observação cadastrada.")
                                case 0:
                                    break
                                case _:
                                    print("Opção inválida, entre novamente com uma opção existente.")
                            input()
                    else: 
                        print("Não é possível acessar o Menu de observações sem cadastrar uma Equipe.")
                        input()
                case 6:
                    path = setPath()
                case 7:
                    confirmaPath = input(f"Deseja gerar no caminho: {path} ? (Y): ")
                    if confirmaPath.lower() == 'y':
                        print(gerarTabelas(listDimensoes, listEquipes, listColaboradores, listObservacoes, path))
                    else: 
                        print("As tabelas não foram geradas.")
                    input()
                case 8:
                    confirmaSairSemSalvar = input("Deseja sair SEM SALVAR as alterações? (Y/n): ")
                    if confirmaSairSemSalvar.lower() == 'y':
                        print("Saindo sem salvar")
                        exit()
                    else:
                        print("Voltando ao Menu anterior.")
                        input()
                case 0:
                    confirmaSalvar = input(f"Deseja salvar as alterações? (Y/n): ")
                    if confirmaSalvar.lower() == 'y':
                        salvarObjeto(listDimensoes, 'data\\dimensoes.pkl')
                        salvarObjeto(listEquipes, 'data\\equipes.pkl')
                        salvarObjeto(listColaboradores, 'data\\colaboradores.pkl')
                        salvarObjeto(listObservacoes, 'data\\observacoes.pkl')
                        salvarObjeto(path, 'data\\path.pkl')
                        print("\nObrigado por utilizar o programa.")
                        exit()
                    else: 
                        print("Modelo não foi salvo.") 
                        input()
                case _:
                    print("\nOpção inválida, entre novamente com uma opção existente.")
        except Exception as e:
            print(f"\nEntrada inválida, tente novamente.\n{str(e)}")
            continue