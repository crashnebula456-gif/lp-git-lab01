# promedio.py
# Calcula el promedio final del curso según el sílabo UPN 2026-2

PESOS = {"T1": 0.10, "EP": 0.20, "T2": 0.20, "EF": 0.50}


def calcular_promedio(notas):
    """Calcula el promedio ponderado."""
    total = 0

    for evaluacion, peso in PESOS.items():
        total += notas[evaluacion] * peso

    return round(total, 2)


if __name__ == "__main__":
    notas_ejemplo = {"T1": 14, "EP": 15, "T2": 13, "EF": 16}
    print("Promedio final:", calcular_promedio(notas_ejemplo))