def validar_desafio_1(codigo: str) -> tuple[bool, str]:
    contexto = {}
    try:
        exec(codigo, contexto)
    except Exception as e:
        return False, f"Erro ao executar o código: {e}"

    if "x" not in contexto:
        return False, "A variável x não foi criada."

    if not isinstance(contexto["x"], (int, float)):
        return False, "x deve ser um número."

    if contexto["x"] != 10:
        return False, "x não tem o valor 10."

    return True, "Parabéns! Desafio concluído"


def validar_desafio_2(codigo: str) -> tuple[bool, str]:
    contexto = {}
    try:
        exec(codigo, contexto)
    except Exception as e:
        return False, f"Erro ao executar o código: {e}"

    if "y" not in contexto:
        return False, "A variável y não foi criada."

    if not isinstance(contexto["y"], (int, float)):
        return False, "y deve ser um número."

    if contexto["y"] != 20:
        return False, "y não tem o valor 20."

    return True, "Parabéns! Desafio concluído"