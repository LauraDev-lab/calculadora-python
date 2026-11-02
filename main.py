"""
Arquivo principal da Calculadora Interativa em Python.
Responsável pela interface de usuário via terminal com suporte a cores ANSI,
design moderno em caixas Unicode, histórico de operações e tratamento de erros.
"""

import os
import sys
from datetime import datetime
from operacoes import (
    somar,
    subtrair,
    multiplicar,
    dividir,
    calcular_porcentagem,
)

# Códigos ANSI para cores e estilos no terminal
class Cores:
    RESET = "\033[0m"
    NEGRITO = "\033[1m"
    DIM = "\033[2m"
    
    # Cores de texto
    CIANO = "\033[96m"
    VERDE = "\033[92m"
    AMARELO = "\033[93m"
    VERMELHO = "\033[91m"
    MAGENTA = "\033[95m"
    AZUL = "\033[94m"
    BRANCO = "\033[97m"

    # Fundos
    BG_VERDE = "\033[42m\033[30m"
    BG_VERMELHO = "\033[41m\033[37m"
    BG_AZUL = "\033[44m\033[37m"


def limpar_tela():
    """Limpa o terminal de acordo com o sistema operacional."""
    os.system("cls" if os.name == "nt" else "clear")


def pausar():
    """Pausa a execução até o usuário pressionar Enter."""
    input(f"\n{Cores.DIM}Pressione [ENTER] para continuar...{Cores.RESET}")


def exibir_cabecalho(total_historico: int = 0):
    """Exibe o cabeçalho estilizado da calculadora."""
    print(f"{Cores.CIANO}╔═══════════════════════════════════════════════════════╗{Cores.RESET}")
    print(f"{Cores.CIANO}║{Cores.NEGRITO}{Cores.BRANCO}            ✨ CALCULADORA INTERATIVA EM PYTHON ✨       {Cores.RESET}{Cores.CIANO}║{Cores.RESET}")
    print(f"{Cores.CIANO}║{Cores.DIM}          Operações Básicas & Cálculo de Porcentagem   {Cores.RESET}{Cores.CIANO}║{Cores.RESET}")
    print(f"{Cores.CIANO}╚═══════════════════════════════════════════════════════╝{Cores.RESET}")
    if total_historico > 0:
        print(f" {Cores.MAGENTA}📌 {total_historico} operação(ões) registrada(s) na memória{Cores.RESET}\n")
    else:
        print()


def exibir_menu():
    """Exibe o menu de opções em formato de painel moderno."""
    print(f"{Cores.AZUL}┌───────────────────────────────────────────────────────┐{Cores.RESET}")
    print(f"{Cores.AZUL}│{Cores.NEGRITO}{Cores.BRANCO}  OPÇÕES DISPONÍVEIS:                                  {Cores.RESET}{Cores.AZUL}│{Cores.RESET}")
    print(f"{Cores.AZUL}├───────────────────────────────────────────────────────┤{Cores.RESET}")
    print(f"{Cores.AZUL}│{Cores.RESET}  {Cores.CIANO}[ 1 ]{Cores.RESET} ➕  Somar                                       {Cores.AZUL}│{Cores.RESET}")
    print(f"{Cores.AZUL}│{Cores.RESET}  {Cores.CIANO}[ 2 ]{Cores.RESET} ➖  Subtrair                                    {Cores.AZUL}│{Cores.RESET}")
    print(f"{Cores.AZUL}│{Cores.RESET}  {Cores.CIANO}[ 3 ]{Cores.RESET} ✖️   Multiplicar                                 {Cores.AZUL}│{Cores.RESET}")
    print(f"{Cores.AZUL}│{Cores.RESET}  {Cores.CIANO}[ 4 ]{Cores.RESET} ➗  Dividir                                     {Cores.AZUL}│{Cores.RESET}")
    print(f"{Cores.AZUL}│{Cores.RESET}  {Cores.AMARELO}[ 5 ]{Cores.RESET} ％  Calcular Porcentagem                        {Cores.AZUL}│{Cores.RESET}")
    print(f"{Cores.AZUL}├───────────────────────────────────────────────────────┤{Cores.RESET}")
    print(f"{Cores.AZUL}│{Cores.RESET}  {Cores.MAGENTA}[ 6 ]{Cores.RESET} 📜  Ver Histórico de Cálculos                   {Cores.AZUL}│{Cores.RESET}")
    print(f"{Cores.AZUL}│{Cores.RESET}  {Cores.MAGENTA}[ 7 ]{Cores.RESET} 🗑️   Limpar Histórico                            {Cores.AZUL}│{Cores.RESET}")
    print(f"{Cores.AZUL}│{Cores.RESET}  {Cores.VERMELHO}[ 0 ]{Cores.RESET} 🚪  Sair do Programa                            {Cores.AZUL}│{Cores.RESET}")
    print(f"{Cores.AZUL}└───────────────────────────────────────────────────────┘{Cores.RESET}")


def obter_numero(mensagem: str) -> float:
    """
    Solicita um número ao usuário com visual interativo e validação em tempo real.
    """
    while True:
        try:
            entrada = input(f"{Cores.AMARELO}▶ {mensagem}{Cores.RESET}").strip()
            # Permite trocar vírgula por ponto (útil no padrão brasileiro)
            entrada_formatada = entrada.replace(",", ".")
            return float(entrada_formatada)
        except ValueError:
            print(f"  {Cores.VERMELHO}✖ Valor inválido! Digite apenas números (ex: 10 ou 3.5).{Cores.RESET}")


def exibir_resultado_box(expressao: str, resultado: float):
    """Exibe um painel de destaque com o resultado da operação."""
    texto_res = f"  {expressao} = {resultado}  "
    largura = max(len(texto_res) + 4, 38)
    
    print(f"\n{Cores.VERDE}┌{'─' * largura}┐{Cores.RESET}")
    print(f"{Cores.VERDE}│{Cores.NEGRITO}{' RESULTADO DA OPERAÇÃO '.center(largura)}{Cores.RESET}{Cores.VERDE}│{Cores.RESET}")
    print(f"{Cores.VERDE}├{'─' * largura}┤{Cores.RESET}")
    print(f"{Cores.VERDE}│{Cores.NEGRITO}{Cores.BRANCO}{texto_res.center(largura)}{Cores.RESET}{Cores.VERDE}│{Cores.RESET}")
    print(f"{Cores.VERDE}└{'─' * largura}┘{Cores.RESET}")


def exibir_historico(historico: list):
    """Exibe todas as operações realizadas na sessão atual."""
    if not historico:
        print(f"\n{Cores.AMARELO}ℹ️ Nenhum cálculo foi realizado ainda nesta sessão.{Cores.RESET}")
        return

    print(f"\n{Cores.MAGENTA}╔═══════════════════════════════════════════════════════╗{Cores.RESET}")
    print(f"{Cores.MAGENTA}║{Cores.NEGRITO}              📜 HISTÓRICO DE CÁLCULOS                 {Cores.RESET}{Cores.MAGENTA}║{Cores.RESET}")
    print(f"{Cores.MAGENTA}╠══════════╦════════════════════════════════════════════╣{Cores.RESET}")
    print(f"{Cores.MAGENTA}║{Cores.RESET}   HORA   {Cores.MAGENTA}║{Cores.RESET} CÁLCULO REALIZADO                          {Cores.MAGENTA}║{Cores.RESET}")
    print(f"{Cores.MAGENTA}╠══════════╬════════════════════════════════════════════╣{Cores.RESET}")

    for item in historico:
        hora = item["hora"]
        calc = item["calc"]
        calc_formatado = (calc[:41] + "..") if len(calc) > 41 else calc.ljust(43)
        print(f"{Cores.MAGENTA}║{Cores.RESET} {hora} {Cores.MAGENTA}║{Cores.VERDE} {calc_formatado}{Cores.RESET}{Cores.MAGENTA}║{Cores.RESET}")

    print(f"{Cores.MAGENTA}╚══════════╩════════════════════════════════════════════╝{Cores.RESET}")


def main():
    historico = []

    while True:
        limpar_tela()
        exibir_cabecalho(len(historico))
        exibir_menu()

        opcao = input(f"\n{Cores.CIANO}👉 Escolha uma opção [0-7]: {Cores.RESET}").strip()

        # 0. Sair
        if opcao == "0":
            limpar_tela()
            print(f"\n{Cores.VERDE}✨ Obrigado por usar a Calculadora Interativa! Até logo! ✨{Cores.RESET}\n")
            break

        # 1 a 4. Operações Básicas
        elif opcao in ["1", "2", "3", "4"]:
            titulos = {
                "1": ("SOMA", "+"),
                "2": ("SUBTRAÇÃO", "-"),
                "3": ("MULTIPLICAÇÃO", "×"),
                "4": ("DIVISÃO", "÷")
            }
            nome_op, simbolo = titulos[opcao]

            print(f"\n{Cores.NEGRITO}--- Realizando: {nome_op} ---{Cores.RESET}")
            num1 = obter_numero("Digite o primeiro número: ")
            num2 = obter_numero("Digite o segundo número: ")

            try:
                if opcao == "1":
                    resultado = somar(num1, num2)
                elif opcao == "2":
                    resultado = subtrair(num1, num2)
                elif opcao == "3":
                    resultado = multiplicar(num1, num2)
                elif opcao == "4":
                    resultado = dividir(num1, num2)

                expressao = f"{num1} {simbolo} {num2}"
                exibir_resultado_box(expressao, resultado)

                # Salva no histórico
                hora_atual = datetime.now().strftime("%H:%M:%S")
                historico.append({
                    "hora": hora_atual,
                    "calc": f"{expressao} = {resultado}"
                })

            except ValueError as erro:
                print(f"\n{Cores.VERMELHO}⚠️  {erro}{Cores.RESET}")

            pausar()

        # 5. Porcentagem
        elif opcao == "5":
            print(f"\n{Cores.NEGRITO}--- Realizando: PORCENTAGEM (%) ---{Cores.RESET}")
            base = obter_numero("Digite o valor base (ex: 200): ")
            taxa = obter_numero("Digite a porcentagem desejada (ex: 15 para 15%): ")

            resultado = calcular_porcentagem(base, taxa)
            expressao = f"{taxa}% de {base}"
            exibir_resultado_box(expressao, resultado)

            # Salva no histórico
            hora_atual = datetime.now().strftime("%H:%M:%S")
            historico.append({
                "hora": hora_atual,
                "calc": f"{expressao} = {resultado}"
            })

            pausar()

        # 6. Ver Histórico
        elif opcao == "6":
            exibir_historico(historico)
            pausar()

        # 7. Limpar Histórico
        elif opcao == "7":
            total = len(historico)
            historico.clear()
            print(f"\n{Cores.VERDE}✔ Histórico limpo com sucesso! ({total} registro(s) removido(s)){Cores.RESET}")
            pausar()

        else:
            print(f"\n{Cores.VERMELHO}✖ Opção '{opcao}' inválida! Escolha um número entre 0 e 7.{Cores.RESET}")
            pausar()


if __name__ == "__main__":
    main()
