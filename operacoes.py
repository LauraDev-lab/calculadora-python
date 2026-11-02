"""
Módulo de operações matemáticas da calculadora.
Contém funções simples e reutilizáveis para cada operação matemática.
"""

def somar(a: float, b: float) -> float:
    """Retorna a soma de dois números."""
    return a + b


def subtrair(a: float, b: float) -> float:
    """Retorna a subtração entre dois números (a - b)."""
    return a - b


def multiplicar(a: float, b: float) -> float:
    """Retorna a multiplicação de dois números."""
    return a * b


def dividir(a: float, b: float) -> float:
    """
    Retorna a divisão entre dois números (a / b).
    Lança ValueError caso o divisor seja zero.
    """
    if b == 0:
        raise ValueError("Erro: Divisão por zero não é permitida.")
    return a / b


def calcular_porcentagem(total: float, percentual: float) -> float:
    """
    Calcula uma porcentagem sobre um valor base.
    Exemplo: calcular_porcentagem(200, 15) -> calcula 15% de 200 = 30.0
    """
    return (total * percentual) / 100
