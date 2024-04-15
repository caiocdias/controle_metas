from .classes import DimensaoData
from datetime import datetime

#Utilizado para retornar a entrada do usuário para o main.py
def controlesDimensoes():
    op = int(input("\n\tMenu de Controle de Dimensões\n\n1- Criar Dimensão\n2- Remover Dimensão\n3- Alterar Dimensão\n4- Visualizar Dimensões\n0- Voltar\n\nSua opção: "))
    return op

def visualizarDimensoes(listDimensoes):
    print("\n\tDimensões de Data Existentes\n")
    for i in range(len(listDimensoes)):
        print(f"{i+1}- {str(listDimensoes[i])}")

def nomeDimensaoExiste(nome, lista):
    return any(dim.nomeDimensaoData.lower() == nome.lower() for dim in lista)

def cadastrarDimensao(listDimensoes):
    try:
        nomeDimensao = input("\nEntre com o nome da dimensão: ").strip()
        if not nomeDimensao: raise ValueError("Nome da dimensão não pode ser vazio.")

        if nomeDimensaoExiste(nomeDimensao, listDimensoes): raise ValueError("Dimensão com nome já existente.")

        dataInicial = datetime.strptime(input("Entre com a Data Inicial: "), "%d/%m/%Y")
        dataFinal = datetime.strptime(input("Entre com a Data Final: "), "%d/%m/%Y")

        if dataInicial > dataFinal: raise ValueError("A Data Inicial não pode ser maior que a Data Final.")

        diasUteis = int(input("Entre com a quantidade de dias úteis: "))
        if diasUteis <= 0: raise ValueError("A quantidade de Dias Úteis deve ser maior do que zero.")

        dimensao = DimensaoData(nomeDimensao, dataInicial, dataFinal, diasUteis)
        listDimensoes.append(dimensao)
        return "Dimensão cadastrada com sucesso."
    except Exception as e:
        return f"Não foi possível cadastrar a dimensão.\n{str(e)}"

def removerDimensao(listDimensoes, listEquipes, listColaboradores):
    try:
        while True:
            visualizarDimensoes(listDimensoes)
            try:
                index = int(input("0- Voltar\n\nDimensão para remover: "))
            except ValueError:
                print("Entrada inválida, tente novamente.")
                continue

            if index >= 1 and index <= len(listDimensoes):
                break
            elif index == 0:
                raise Exception("Voltando ao menu anterior.")
            else:
                print("Entrada inválida, tente novamente.")

        confirmacao = input("Ao apagar esta dimensão todas as equipes relacionadas e seus colaboradores também serão apagados, deseja continuar? (Y): ")
        if confirmacao.lower() != 'y':
            raise Exception("Voltando ao menu anterior.")

        nomesEquipesParaRemover = [equipe.nomeEquipe for equipe in listEquipes if equipe.dimensaoDataEquipe.nomeDimensaoData == listDimensoes[index-1].nomeDimensaoData]
        identificadoresColaboradoresParaRemover = [colaborador.nomeColaborador + colaborador.equipeColaborador.nomeEquipe for colaborador in listColaboradores if colaborador.equipeColaborador.nomeEquipe in nomesEquipesParaRemover]

        listColaboradores[:] = [colaborador for colaborador in listColaboradores if colaborador.nomeColaborador + colaborador.equipeColaborador.nomeEquipe not in identificadoresColaboradoresParaRemover]
        listEquipes[:] = [equipe for equipe in listEquipes if equipe.nomeEquipe not in nomesEquipesParaRemover]

        del listDimensoes[index-1]
        return f"Dimensão removida com sucesso."
    except Exception as e:
        return f"Não foi possível remover a Dimensão.\n{str(e)}"

def alterarDimensao(listDimensoes):
    try:
        while True:
            visualizarDimensoes(listDimensoes)
            try:
                index = int(input("0- Voltar\n\nDimensão para alterar: "))
            except ValueError:
                print("\nEntrada inválida, tente novamente.")
                continue

            if index >= 1 and index <= len(listDimensoes):
                break
            elif index == 0:
                raise Exception("Voltando ao menu anterior.")
            else:
                print("Entrada inválida, tente novamente.")
        
        confirmacao = input("Ao alterar esta dimensão todas as equipes relacionadas e seus colaboradores também serão alterados, deseja continuar? (Y): ")
        if confirmacao.lower() != 'y':
            raise Exception("Voltando ao menu anterior.")
        
        while True:
            try:
                indexAlt = int(input("\n\tAtributo para alterar\n\n1- Alterar Nome\n2- Alterar Intervalo de Datas\n3- Alterar Quantidade de Dias Uteis\n\nSua opção: "))
            except ValueError:
                print("Entrada inválida, tente novamente.")
                continue

            if indexAlt >= 1 and indexAlt <= 3:
                break
            else:
                print("Entrada inválida, tente novamente.")

        match indexAlt:
            case 1:
                nomeDimensaoData = input("Novo Nome: ")
                if nomeDimensaoExiste(nomeDimensaoData, listDimensoes): raise ValueError("Dimensão com nome já existente.")
                if not nomeDimensaoData: 
                    raise ValueError("Nome da dimensão não pode ser vazio.")   
                listDimensoes[index-1].nomeDimensaoData = nomeDimensaoData

            case 2:
                dataInicial = datetime.strptime(input("Entre com a Data Inicial: "), "%d/%m/%Y")
                dataFinal = datetime.strptime(input("Entre com a Data Final: "), "%d/%m/%Y")

                if dataInicial > dataFinal: 
                    raise ValueError("A Data Inicial não pode ser maior que a Data Final.")
                
                listDimensoes[index-1].dataInicial = dataInicial
                listDimensoes[index-1].dataFinal = dataFinal

            case 3:
                diasUteis = int(input("Entre com a quantidade de dias úteis: "))
                if diasUteis <= 0: 
                    raise ValueError("A quantidade de Dias Úteis deve ser maior do que zero.")
                listDimensoes[index-1].diasUteis = diasUteis

            case _:
                print("\nEntrada inválida.")
                raise Exception("Não foi possível encontrar o atributo especificado.")
        return f"Dimensão alterada com sucesso."
    except Exception as e:
        return f"Não foi possível alterar a dimensão.\n{str(e)}"