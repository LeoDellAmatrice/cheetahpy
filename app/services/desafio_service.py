from app.domain.desafios_list import DESAFIOS
from app.domain.desafio import Desafio


class DesafioService:
    def __init__(self, desafio_atual: int = None):
        if desafio_atual is None:
            desafio_atual = 0

        self.desafio_atual = desafio_atual

    def proximo(self) -> Desafio:
        if self.desafio_atual+1 >= len(DESAFIOS):
            return DESAFIOS[self.desafio_atual]

        self.desafio_atual += 1
        return DESAFIOS[self.desafio_atual]

    def anterior(self) -> Desafio:
        if self.desafio_atual <= 0:
            return DESAFIOS[self.desafio_atual]

        self.desafio_atual -= 1
        return DESAFIOS[self.desafio_atual]

    def validar_codigo(self, codigo: str) -> tuple[bool, str]:
        return DESAFIOS[self.desafio_atual].validar(codigo)

    def get_atual(self) -> Desafio:
        return DESAFIOS[self.desafio_atual]