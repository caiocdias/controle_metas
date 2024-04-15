from .classes import Observacao
from .controlesEquipe import visualizarEquipes
from datetime import datetime

#Utilizado para retornar a entrada do usuário para o main.py
def controlesObservacoes():
    op = int(input("\n\tMenu de Controle de Observações\n\n1- Cadastrar Observação\n2- Remover Observação\n3- Alterar Observação\n4- Visualizar Observações\n5- Remover todas as Observações\n6- Ordenar observações\n0- Voltar\n\nSua opção: "))
    return op

def visualizarObservacoes(listObservacoes):
    print("\n\tObservações Existentes\n")
    for i in range(len(listObservacoes)):
        print(f"{i+1}- {str(listObservacoes[i])}")

def cadastrarObservacao(listObservacoes, listEquipes):
    try:
        colaborador = input("Colaborador Referente à observação: ")
        dataInicial = datetime.strptime(input("Entre com a data inicial: "), "%d/%m/%Y")
        dataFinal = datetime.strptime(input("Entre com a data final: "), "%d/%m/%Y")
        if dataInicial > dataFinal: raise Exception("A data inicial não pode ser maior que a data final.")

        while True:
            visualizarEquipes(listEquipes)
            index = int(input("\n0- Voltar\n\nEquipe para associar à observação: "))
            if index >= 1 and index <= len(listEquipes): break
            elif index == 0: raise Exception("Voltando ao menu antior.")
            else: print("Entrar inválida, tente novamente.")
        
        ocorrencia = input("Entre com a ocorrência: ")
        aux = Observacao(colaborador, listEquipes[index-1], dataInicial, dataFinal, ocorrencia)
        listObservacoes.append(aux)
        return f"Observação cadastrada com sucesso."
    
    except Exception as e:
        return f"Não foi possível cadastrar a observação.\n{str(e)}"

def removerObservacao(listObservacoes):
    try:
        while True:
            visualizarObservacoes(listObservacoes)
            index = int(input("\n0- Voltar\n\nObservação para remover: "))
            if index >= 1 and index <= len(listObservacoes): break
            elif index == 0: raise Exception("Voltando ao menu anterior.")
            else: print("Entrada inválida, tente novamente.")
        
        confirmacao = input("Tem certeza que deseja remover essa observação? (Y): ")
        if confirmacao.lower() != 'y': raise Exception("Voltando ao menu anterior.")

        del listObservacoes[index-1]
        return f"Observação removida com sucesso."
    
    except Exception as e:
        return f"Não foi possível remover a Observação.\n{str(e)}"
    
def alterarObservacao(listObservacoes, listEquipes):
    try:
        while True:
            visualizarObservacoes(listObservacoes)
            index = int(input("\n0- Voltar\n\nObservação para alterar: "))
            if index >= 1 and index <= len(listObservacoes): break
            elif index == 0: raise Exception("Voltando ao menu anterior.")
            else: print("Entrada inválida, tente novamente.")

        while True:
            opAtributo = int(input("\n\tAtributo para alterar\n\n1- Colaborador\n2- Intervalo de datas\n3- Equipe\n4- Ocorrência\n0- Voltar\n\nSua opção: "))
            match opAtributo:
                case 1:
                    listObservacoes[index-1].colaborador = input("Novo colaborador: ")
                    break
                case 2:
                    dataInicial = datetime.strptime(input("Entre com a nova data inicial: "), "%d/%m/%Y")
                    dataFinal = datetime.strptime(input("Entre com a nova data final: "), "%d/%m/%Y")
                    if dataInicial > dataFinal: raise Exception("A data inicial não pode ser maior que a data final.")
                    listObservacoes[index-1].dataInicial = dataInicial
                    listObservacoes[index-1].dataFinal = dataFinal
                    break
                case 3:
                    while True:
                        visualizarEquipes(listEquipes)
                        indexEquipe = int(input("\n0- Voltar\n\nNova Equipe para associar à observação: "))
                        if indexEquipe >= 1 and indexEquipe <= len(listEquipes): break
                        elif indexEquipe == 0: raise Exception("Voltando ao menu antior.")
                        else: print("Entrar inválida, tente novamente.")
                    listObservacoes[index-1].equipeObservacao = listEquipes[indexEquipe-1]
                    break
                case 4:
                    listObservacoes[index-1].ocorrencia = input("Nova Ocorrência: ")
                    break
                case 0:
                    raise Exception("Voltando ao menu anterior.")
                case _:
                    print("Entrada inválida, tente novamente: ")
        return f"Observação alterada com sucesso."
    
    except Exception as e:
        return f"Não foi possível alterar a Observação.\n{str(e)}"

def ordenarObservacoes(listObservacoes):
    try:
        listObservacoes.sort(key=lambda x: x.equipeObservacao.nomeEquipe)
        return f"Tabela ordenada com sucesso."
    except Exception as e:
        return f"Não foi possível ordernar a tabela.\n{str(e)}"