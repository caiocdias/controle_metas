from .Equipe import Equipe
from datetime import datetime

class Observacao:
    def __init__(self, colaborador, equipeObservacao : Equipe, dataInicial, dataFinal, ocorrencia) -> None:
        self.colaborador = colaborador
        self.equipeObservacao = equipeObservacao
        self.dataInicial = dataInicial
        self.dataFinal = dataFinal
        self.ocorrencia = ocorrencia

    def __str__(self):
        return f"{self.colaborador}, {self.equipeObservacao.nomeEquipe}, {datetime.strftime(self.dataInicial, "%d/%m/%Y")} à {datetime.strftime(self.dataFinal, "%d/%m/%Y")}:\nOcorrência: {self.ocorrencia}"