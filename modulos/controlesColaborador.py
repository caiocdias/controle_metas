from .classes import Colaborador
from .controlesEquipe import visualizarEquipes

#Utilizado para retornar a entrada do usuário para o main.py
def controlesColaborador():
    op = int(input("\n\tMenu de Controle de Colaboradores\n\n1- Cadastrar Colaborador\n2- Remover Colaborador\n3- Alterar Colaborador\n4- Visualizar Colaborador\n5- Ordenar colaboradores\n0- Voltar\n\nSua opção: "))
    return op

def visualizarColaboradores(listColaboradores = []):
    print("\n\tColaboradores Existentes\n")
    for i in range(len(listColaboradores)):
        print(f"{i+1}- {str(listColaboradores[i])}")

def cadastrarColaborador(listColaboradores = [], listEquipes = []):
    try:
        nomeColaborador = input("Entre com o nome completo do Colaborador: ")
        matriculaColaborador = input("Entre com a matrícula do Colaborador: ")

        while True:
            visualizarEquipes(listEquipes)
            index = int(input("\nEquipe para associar ao Colaborador: "))
            if (index >= 1 and index <= len(listEquipes)): break
            else: print("Entrada inválida, tente novamente.")

        for i in range(len(listColaboradores)):
            if listColaboradores[i].nomeColaborador.lower() + listColaboradores[i].equipeColaborador.nomeEquipe.lower() == nomeColaborador.lower() + listEquipes[index-1].nomeEquipe.lower():
                raise Exception("Não é possível criar este colaborador nessa equipe pois o mesmo ja está cadastrado.")

        aux = Colaborador(nomeColaborador, matriculaColaborador, listEquipes[index-1], [], [])
        listColaboradores.append(aux)
        return f"Colaborador cadastrado com sucesso."
    except Exception as e:
        return f"Não foi possível cadastrar o colaborador.\n{str(e)}"
    
def removerColaborador(listColaboradores = []):
    try:
        while True:
            visualizarColaboradores(listColaboradores)
            print("\n0- Voltar")
            index = int(input("\nColaborador que deseja remover: "))
            if (index >= 1 and index <= len(listColaboradores)): break
            elif index == 0: raise Exception("Voltando ao menu anterior.")
            else: print("Entrada inválida, tente novamente.")
        del listColaboradores[index-1]
        return f"Colaborador removido com sucesso."
    except Exception as e:
        return f"Não foi possível remover o Colaborador.\n{str(e)}"

def alterarColaborador(listColaboradores = [], listEquipes = []):
    try:
        while True:
            visualizarColaboradores(listColaboradores)
            index = int(input("\n0-Voltar\nColaborador que deseja alterar: "))
            if (index >= 1 and index <= len(listColaboradores)): break
            elif index == 0: raise Exception("Voltando ao menu anterior.")
            else: print("Entrada inválida, tente novamente.")

        while True:
            opAlt = int(input("\n0- Voltar\n1- Alterar Nome\n2- Alterar Matricula\n3- Alterar Equipe\n\nSua opção: "))
            match opAlt:
                case 1:
                    novoNome = input("Digite o novo nome do colaborador: ")

                    for i in range(len(listColaboradores)):
                        if listColaboradores[i].nomeColaborador + listColaboradores[i].equipeColaborador.nomeEquipe == novoNome + listColaboradores[index-1].equipeColaborador.nomeEquipe:
                            raise Exception("Não é possível alterar o nome do Colaborador, pois este nome ja está cadastrado nessa equipe")
                    
                    listColaboradores[index-1].nomeColaborador = novoNome
                case 2:
                    listColaboradores[index-1].matriculaColaborador = input("Nova matrícula: ")
                case 3:
                    while True:
                        visualizarEquipes(listEquipes)
                        indexEquipe = int(input("\nEquipe para associar ao Colaborador: "))
                        if (indexEquipe >= 1 and indexEquipe <= len(listEquipes)): break
                        else: print("Entrada inválida, tente novamente.")      
                    listColaboradores[index-1].equipeColaborador = listEquipes[indexEquipe-1]
                case 0:
                    raise Exception("Voltando ao menu anterior.")
                case _:
                    print("Opção inválida, tente novamente.")
            return f"Colaborador alterado com sucesso."
    except Exception as e:
        return f"Não foi possível alterar o Colaborador.\n{str(e)}"
    
def ordenarColaboradores(listColaboradores):
    try:
        listColaboradores.sort(key=lambda x: x.equipeColaborador.nomeEquipe)
        return f"Tabela ordenada com sucesso."
    except Exception as e:
        return f"Não foi possível ordenar a tabela.\n{str(e)}" 