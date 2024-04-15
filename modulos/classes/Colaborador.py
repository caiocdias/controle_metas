from .Equipe import Equipe

class Colaborador:
    def __init__(self, nomeColaborador, matriculaColaborador, equipeColaborador: Equipe, diasZerados, diasMetade) -> None:
        self.nomeColaborador = nomeColaborador
        self.matriculaColaborador = matriculaColaborador
        self.equipeColaborador = equipeColaborador
        self.diasZerados = diasZerados
        self.diasMetade = diasMetade

    def __str__(self) -> str:
        return f"Equipe: {self.equipeColaborador.nomeEquipe}, Colaborador: {self.nomeColaborador}, Matrícula: {self.matriculaColaborador}, Dias zerados: {len(self.diasZerados)}, Dias metade: {len(self.diasMetade)}"