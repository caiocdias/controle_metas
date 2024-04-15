from .DimensaoData import DimensaoData

class Equipe:
    def __init__(self, nomeEquipe, metaTotalNS, metaTotalUS, dimensaoDataEquipe: DimensaoData) -> None:
        self.nomeEquipe = nomeEquipe
        self.metaTotalNS = (metaTotalNS if metaTotalNS>=0 else 0)
        self.metaTotalUS = (metaTotalUS if metaTotalUS>=0 else 0)
        self.dimensaoDataEquipe = dimensaoDataEquipe

    def __str__(self) -> str:
        return f"Nome: {self.nomeEquipe}, Meta Total NS: {self.metaTotalNS}, Meta Total US: {self.metaTotalUS}, Dimensão: {self.dimensaoDataEquipe.nomeDimensaoData}"