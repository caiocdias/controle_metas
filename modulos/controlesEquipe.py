from .classes import Equipe
from .controlesDimensoes import visualizarDimensoes

#Utilizado para retornar a entrada do usuário para o main.py
def controlesEquipe():
    op = int(input("\n\tMenu de Controle de Equipes\n\n1- Cadastrar Equipe\n2- Remover Equipe\n3- Alterar Equipe\n4- Visualizar Equipes\n5- Ordenar Equipes\n0- Voltar\n\nSua opção: "))
    return op

def visualizarEquipes(listEquipes = []):
    print("\n\tEquipes existentes\n\n", end="")
    for i in range(len(listEquipes)):
        print(f"{i+1}- {str(listEquipes[i])}")

def cadastrarEquipe(listEquipes = [], listDimensoes = []):
    try:
        nomeEquipe = str(input("\nEntre com o nome da equipe: "))
        
        if nomeEquipe == '':
            raise Exception("Não é possível cadastrar uma equipe com este nome, o nome é inválido.")
        for i in (range(len(listEquipes))):
            if listEquipes[i].nomeEquipe.lower() == nomeEquipe.lower():
                raise Exception("Não é possível cadastrar uma equipe com este nome, pois a equipe já existe.")
        
        metaTotalNS = float(input("Entre com a meta total de NS: "))
        metaTotalUS = float(input("Entre com a meta total de US: "))

        while True:
            visualizarDimensoes(listDimensoes)
            index = int(input("\nDimensão para associar à Equipe: "))
            if (index >= 1 and index <= len(listDimensoes)): break
            else: print("Entrada inválida, tente novamente.")

        aux = Equipe(nomeEquipe, metaTotalNS, metaTotalUS, listDimensoes[index-1])
        listEquipes.append(aux)
        return f"Equipe cadastrada com sucesso."
    except Exception as e:
        return f"Não foi possível cadastrar a equipe.\n{str(e)}"
    

def removerEquipe(listEquipes = [], listColaboradores = []):
    try:
        while True:
            visualizarEquipes(listEquipes)
            print("\n0- Voltar\n", end="")
            index = int(input("\nEquipe para deletar: "))
            if (index >= 1 and index <= len(listEquipes)): break
            elif index == 0: raise Exception("Voltando ao menu anterior.")
            else: print("Entrada inválida, tente novamente!")
        confirmacao = input("\nTodos os colaboradores associados a essa equipe serão excluidos. Deseja realmente excluir? (Y): ")
        if confirmacao.lower() != 'y': raise Exception("Voltando ao menu anterior.")

        identificadoresColaboradoresParaRemover = [colaborador.nomeColaborador + colaborador.equipeColaborador.nomeEquipe for colaborador in listColaboradores if colaborador.equipeColaborador.nomeEquipe == listEquipes[index-1].nomeEquipe]
        listColaboradores[:] = [colaborador for colaborador in listColaboradores if colaborador.nomeColaborador + colaborador.equipeColaborador.nomeEquipe not in identificadoresColaboradoresParaRemover]
        
        del listEquipes[index-1]
        return f"Equipe removida com sucesso."
    except Exception as e:
        return f"Não foi possível remover a Equipe.\n{str(e)}"
    
def alterarEquipe(listEquipes, listDimensoes):
    try:
        while True:
            visualizarEquipes(listEquipes)
            print("\n0- Voltar\n", end="")
            index = int(input("\nEquipe para alterar: "))
            if (index >= 1 and index <= len(listEquipes)): break
            elif index == 0: raise Exception("Voltando ao menu anterior.")
            else: print("Entrada inválida, tente novamente!")
        while True:
            opAlt = int(input("\n0- Voltar\n1- Alterar Nome\n2- Alterar Meta NS\n3- Alterar Meta US\n4- Alterar Dimensão\n\nSua opção: "))
            match opAlt:
                case 1:
                    novoNome = input("Novo nome: ")
                    for i in range(len(listEquipes)):
                        if listEquipes[i].nomeEquipe == novoNome:
                            raise Exception("Já existe uma equipe com este nome")

                    listEquipes[index-1].nomeEquipe = novoNome
                case 2:
                    listEquipes[index-1].metaTotalNS = float(input("\nNova Meta NS: "))
                case 3:
                    listEquipes[index-1].metaTotalUS = float(input("\nNova Meta US: "))
                case 4:
                    while True:
                        visualizarDimensoes(listDimensoes)
                        indexDim = int(input("\nDimensão para associar à Equipe: "))
                        if (indexDim >= 1 and indexDim <= len(listDimensoes)): break
                        else: print("Entrada inválida, tente novamente.")
                    
                    listEquipes[index-1].dimensaoDataEquipe = listDimensoes[indexDim-1]
                case 0:
                    raise Exception("Voltando ao menu anterior.")
                case _:
                    print("Opção inválida, tente novamente.")
            return f"Equipe alterada com sucesso."
    except Exception as e:
        return f"Não foi possível alterar a Equipe.\n{str(e)}"
    
def ordenarEquipes(listEquipes):
    try:
        listEquipes.sort(key=lambda x: x.nomeEquipe)
        return f"Equipes ordenadas com sucesso."
    except Exception as e:
        return f"Não foi possível ordenar as Equipes.\n{str(e)}"