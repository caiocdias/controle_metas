from datetime import datetime, timedelta
import pandas as pd

class DimensaoData:
    def __init__(self, nomeDimensaoData, dataInicial, dataFinal, diasUteis) -> None:
        self.nomeDimensaoData = nomeDimensaoData
        self.dataInicial = dataInicial
        self.dataFinal = dataFinal
        self.diasUteis = diasUteis

    def __str__(self) -> str:
        return f"{self.nomeDimensaoData}, {self.dataInicial.strftime("%d/%m/%Y")} à {self.dataFinal.strftime("%d/%m/%Y")}, {self.diasUteis} dias úteis."
    
    def exportToExcel(self, path):
        aux = []
        dataInicial = self.dataInicial
        while dataInicial <= self.dataFinal:
            aux.append(datetime.strftime(dataInicial, "%d/%m/%Y"))
            dataInicial += timedelta(days=1)
        dfDimData = pd.DataFrame(aux, columns=['DATA'])
        dfDimData.to_excel(f"{path}\\DimensaoData_{self.nomeDimensaoData}.xlsx", sheet_name='data', index=None)
