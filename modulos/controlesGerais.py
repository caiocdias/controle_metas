import pickle
from datetime import datetime, timedelta
import pandas as pd

def setPath():
    return input("Entre com o caminho de salvamento das tabelas excel: ")

def gerarTabelas(listDimensoes, listEquipes, listColaboradores, listObservacoes, path):
    try:
        aux = []
        columns = ['nomeColaborador', 'nomeEquipe', 'dataInicial', 'dataFinal', 'ocorrencia']
        for observacao in listObservacoes:
            aux.append([observacao.colaborador, observacao.equipeObservacao.nomeEquipe, datetime.strftime(observacao.dataInicial, "%d/%m/%Y"), datetime.strftime(observacao.dataFinal, "%d/%m/%Y"), observacao.ocorrencia])
        dfObs = pd.DataFrame(aux, columns=columns)


        aux = []
        columns = ['nomeEquipe', 'metaTotalNS', 'metaTotalUS', 'nomeDimensaoData', 'diasUteis']
        for equipe in listEquipes:
            aux.append([equipe.nomeEquipe, equipe.metaTotalNS, equipe.metaTotalUS, equipe.dimensaoDataEquipe.nomeDimensaoData, equipe.dimensaoDataEquipe.diasUteis])
        dfEquipe = pd.DataFrame(aux, columns=columns)
        
        aux = []
        columns = ['matriculaColaborador', 'nomeColaborador', 'nomeEquipe', 'chaveColaborador']
        for colaborador in listColaboradores:
            aux.append([colaborador.matriculaColaborador, colaborador.nomeColaborador, colaborador.equipeColaborador.nomeEquipe, colaborador.nomeColaborador+colaborador.equipeColaborador.nomeEquipe])
        dfColab = pd.DataFrame(aux, columns=columns)
        
        aux = []
        columns = ['matriculaColaborador', 'nomeColaborador', 'nomeEquipe', 'chaveColaborador', 'dataMeta', 'metaDiariaNS', 'metaDiariaUS']
        for colaborador in listColaboradores:
            dataInicial = colaborador.equipeColaborador.dimensaoDataEquipe.dataInicial
            dataFinal = colaborador.equipeColaborador.dimensaoDataEquipe.dataFinal

            while dataInicial <= dataFinal:
                if dataInicial not in colaborador.diasZerados and dataInicial not in colaborador.diasMetade:
                    aux.append([colaborador.matriculaColaborador, colaborador.nomeColaborador, colaborador.equipeColaborador.nomeEquipe, colaborador.nomeColaborador+colaborador.equipeColaborador.nomeEquipe,
                                dataInicial, colaborador.equipeColaborador.metaTotalNS / colaborador.equipeColaborador.dimensaoDataEquipe.diasUteis, colaborador.equipeColaborador.metaTotalUS / colaborador.equipeColaborador.dimensaoDataEquipe.diasUteis])
                elif dataInicial in colaborador.diasZerados and dataInicial not in colaborador.diasMetade:
                    aux.append([colaborador.matriculaColaborador, colaborador.nomeColaborador, colaborador.equipeColaborador.nomeEquipe, colaborador.nomeColaborador+colaborador.equipeColaborador.nomeEquipe,
                                dataInicial, 0, 0])
                elif dataInicial not in colaborador.diasZerados and dataInicial in colaborador.diasMetade:
                    aux.append([colaborador.matriculaColaborador, colaborador.nomeColaborador, colaborador.equipeColaborador.nomeEquipe, colaborador.nomeColaborador+colaborador.equipeColaborador.nomeEquipe,
                                dataInicial, colaborador.equipeColaborador.metaTotalNS / colaborador.equipeColaborador.dimensaoDataEquipe.diasUteis / 2, colaborador.equipeColaborador.metaTotalUS / colaborador.equipeColaborador.dimensaoDataEquipe.diasUteis / 2])
                elif dataInicial in colaborador.diasZerados and dataInicial in colaborador.diasMetade:
                    aux.append([colaborador.matriculaColaborador, colaborador.nomeColaborador, colaborador.equipeColaborador.nomeEquipe, colaborador.nomeColaborador+colaborador.equipeColaborador.nomeEquipe,
                                dataInicial, 0, 0])
                else:
                    raise Exception("Erro ao gerar modelo")
                dataInicial += timedelta(days=1)
        dfMetas = pd.DataFrame(aux, columns=columns)
                
        dfEquipe.to_excel(f"{path}\\DimensaoEquipe_equipes.xlsx", index=None)
        dfColab.to_excel(f"{path}\\DimensaoColaborador_colaboradores.xlsx", index=None)
        dfMetas.to_excel(f"{path}\\DimensaoColaborador_metas.xlsx", index=None)
        dfObs.to_excel(f"{path}\\metaDados_observacao.xlsx", index=None)
        for dimensao in listDimensoes:
            dimensao.exportToExcel(path)

        return f"Modelo gerado com sucesso."
    except Exception as e:
        return f"Não foi possível gerar o modelo.\n{str(e)}"

def salvarObjeto(obj, path):
    with open(path, 'wb') as file:
        pickle.dump(obj, file)

def carregarObjeto(path):
    with open(path, 'rb') as file:
        return pickle.load(file)