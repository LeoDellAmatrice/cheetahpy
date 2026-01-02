from app.domain.desafio import Desafio
import app.domain.desafios_validators as dv


DESAFIOS: list[Desafio] = [
    Desafio(
        id_desafio=1,
        titulo="Variável simples",
        descricao="Crie uma variável chamada x com valor 10.",
        validador=dv.validar_desafio_1,
    ),
    Desafio(
        id_desafio=2,
        titulo="Variável simples 2.0",
        descricao="Crie uma variável chamada y com valor 20.",
        validador=dv.validar_desafio_2,
    )
]
