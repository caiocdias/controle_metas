from datetime import datetime
from modulos import visualizarDimensoes, visualizarColaboradores

#Utilizado para retornar a entrada do usuário para o main.py
def controlesMetas():
    op = int(input("\n\tMenu de Controle de Metas\n\n1- Zerar dias em todos os colaboradores\n2- Zerar dias com base em Dimensão\n3- Zerar dias com base em colaborador" +
                   "\n4- Definir meta pela metade para colaborador\n5- Remover todos os Dias Zerados\n6- Remover todos os Dias pela Metade\n7- Remover dias zerados específicos para colaborador\n8- Remover dias pela metade específicos para colaborador\n0- Voltar\n\nSua opção: "))
    return op

def definirDiasZeradosTodos(listColaboradores):
    try:
        listDiasZerados = []
        while True:
                try:
                    entrada = input("Digite a Data (dd/mm/aaaa) em que a meta deve ser zerada ou digite 0 para sair: ")
                    if entrada == '0':
                        break
                    listDiasZerados.append(datetime.strptime(entrada, '%d/%m/%Y'))
                except Exception as e:
                    print(str(e))
                    continue
        for colaborador in listColaboradores:
            colaborador.diasZerados = listDiasZerados.copy()
        return f"Função executada com sucesso."
    except Exception as e:
        return f"{str(e)}"
    
def definirDiasZeradosDim(listDimensoes, listEquipes, listColaboradores):
    try:
        while True:
            visualizarDimensoes(listDimensoes)
            index = int(input("\n0- Voltar\nDimensão para zerar dias: "))
            if (index >= 1 and index <= len(listDimensoes)): break
            elif index == 0: raise Exception("Voltando ao menu anterior.")
            else: print("Entrada inválida, tente novamente.")
        
        equipesParaAlterar = [equipe.nomeEquipe for equipe in listEquipes if equipe.dimensaoDataEquipe.nomeDimensaoData == listDimensoes[index-1].nomeDimensaoData]
        if len(equipesParaAlterar) == 0:
            raise Exception("A dimensão não possui nenhuma equipe.")
        
        colaboradoresParaAlterar = [colaborador.nomeColaborador + colaborador.equipeColaborador.nomeEquipe for colaborador in listColaboradores if colaborador.equipeColaborador.nomeEquipe in equipesParaAlterar]
        if len(colaboradoresParaAlterar) == 0:
            raise Exception("Não há colaboradores nas equipes desta dimensão.")
        listDiasZerados = []

        while True:
            try:
                entrada = input("Digite a Data (dd/mm/aaaa) para zerar ou digite 0 para sair: ")
                if entrada == '0':
                    break
                listDiasZerados.append(datetime.strptime(entrada, '%d/%m/%Y'))
            except Exception as e:
                print(str(e))
                continue
        for colaborador in listColaboradores:
            if colaborador.nomeColaborador + colaborador.equipeColaborador.nomeEquipe in colaboradoresParaAlterar:
                colaborador.diasZerados = listDiasZerados.copy()

        return f"Função executada com sucesso."
    except Exception as e:
        return f"{str(e)}"
    
def definirDiasZeradosColab(listColaboradores):
    try:
        while True:
            visualizarColaboradores(listColaboradores)
            index = int(input("\n0- Voltar\nColaborador para zerar a meta: "))
            if (index >= 1 and index <= len(listColaboradores)): break
            elif index == 0: raise Exception("Voltando ao menu anterior.")
            else: print("Entrada inválida, tente novamente.")
        listDiasZerados = [] 
        while True:
            try:
                entrada = input("Digite a Data (dd/mm/aaaa) em que a meta deve ser zerada ou digite 0 para sair: ")
                if entrada == '0':
                    break
                listDiasZerados.append(datetime.strptime(entrada, '%d/%m/%Y'))
            except Exception as e:
                print(str(e))
                continue
        for dia in listDiasZerados:
            listColaboradores[index-1].diasZerados.append(dia)
        return f"Função executada com sucesso."
    except Exception as e:
        return f"{str(e)}"
    
def definirDiasMetade(listColaboradores):
    try:
        while True:
            visualizarColaboradores(listColaboradores)
            index = int(input("\n0- Voltar\nColaborador para definir meta pela metade: "))
            if (index >= 1 and index <= len(listColaboradores)): break
            elif index == 0: raise Exception("Voltando ao menu anterior.")
            else: print("Entrada inválida, tente novamente.")
        listDiasMetade = []
        while True:
            try:
                entrada = input("Digite a Data (dd/mm/aaaa) em que a meta deve ser reduzida pela metade ou digite 0 para sair: ")
                if entrada == '0':
                    break
                listDiasMetade.append(datetime.strptime(entrada, '%d/%m/%Y'))
            except Exception as e:
                print(str(e))
                continue
        for dia in listDiasMetade:
            listColaboradores[index-1].diasMetade.append(dia)
        return f"Função executada com sucesso."
    except Exception as e:
        return f"{str(e)}"

def removerDiasZeradosTodos(listColaboradores):
    try:
        confirma = input("Deseja remover todos os dias zerados de todos os colaboradores? (Y/n): ")
        if confirma.lower() == 'y':
            for colaborador in listColaboradores:
                colaborador.diasZerados.clear()
            return f"Dias zerados removidos com sucesso."
        else:
            raise Exception("Voltando ao Menu anterior.")
    except Exception as e:
        return f"Não foi possível remover os dias.\n{str(e)}"

def removerDiasMetadeTodos(listColaboradores):
    try:
        confirma = input("Deseja remover todos os dias pela metade de todos os colaboradores? (Y/n): ")
        if confirma.lower() == 'y':
            for colaborador in listColaboradores:
                colaborador.diasMetade.clear()
            return f"Dias pela metade removidos com sucesso."
        else:
            raise Exception("Voltando ao Menu anterior.")
    except Exception as e:
        return f"Não foi possível remover os dias.\n{str(e)}"
    
def removerDiasZeradosColab(listColaboradores):
    try:
        while True:
            visualizarColaboradores(listColaboradores)
            index = int(input("\n0- Voltar\nColaborador para alterar a meta: "))
            if (index >= 1 and index <= len(listColaboradores)): break
            elif index == 0: raise Exception("Voltando ao menu anterior.")
            else: print("Entrada inválida, tente novamente.")
        
        diasParaRemover = []
        for x in range(len(listColaboradores[index-1].diasZerados)):
            print(f"{x+1}- {datetime.strftime(listColaboradores[index-1].diasZerados[x], "%d/%m/%Y")}")
        while True:
            diaRemovido = int(input("Digite o indexador do dia para remover ou 0 para sair: "))
            if diaRemovido == 0:
                break
            else:
                diasParaRemover.append(listColaboradores[index-1].diasZerados[diaRemovido-1])

        listColaboradores[index-1].diasZerados =  [dia for dia in listColaboradores[index-1].diasZerados if dia not in diasParaRemover]
        return f"Dias removidos com sucesso."
            
    except Exception as e:
        return f"Não foi possível remover os dias.\n{str(e)}"
    
def removerDiasMetadeColab(listColaboradores):
    try:
        while True:
            visualizarColaboradores(listColaboradores)
            index = int(input("\n0- Voltar\nColaborador para alterar a meta: "))
            if (index >= 1 and index <= len(listColaboradores)): break
            elif index == 0: raise Exception("Voltando ao menu anterior.")
            else: print("Entrada inválida, tente novamente.")
        
        diasParaRemover = []
        for x in range(len(listColaboradores[index-1].diasMetade)):
            print(f"{x+1}- {datetime.strftime(listColaboradores[index-1].diasMetade[x], "%d/%m/%Y")}")
        while True:
            diaRemovido = int(input("Digite o indexador do dia para remover ou 0 para sair: "))
            if diaRemovido == 0:
                break
            else:
                diasParaRemover.append(listColaboradores[index-1].diasMetade[diaRemovido-1])

        listColaboradores[index-1].diasMetade =  [dia for dia in listColaboradores[index-1].diasMetade if dia not in diasParaRemover]
        return f"Dias removidos com sucesso."
            
    except Exception as e:
        return f"Não foi possível remover os dias.\n{str(e)}"