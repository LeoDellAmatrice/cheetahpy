from collections.abc import Callable

class Desafio:
    def __init__(self, id_desafio: int, titulo: str, descricao: str, validador: Callable[[str], tuple[bool, str]]):
        self.id_desafio = id_desafio
        self.titulo = titulo
        self.descricao = descricao
        self.validador = validador

    def validar(self, codigo: str):
        return self.validador(codigo)

    def __str__(self):
        return f'{self.id_desafio}-{self.titulo}: {self.descricao}'