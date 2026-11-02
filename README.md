# 🧮 Calculadora Interativa em Python & Web

Um projeto completo de calculadora desenvolvido com foco em boas práticas de programação, modularidade, experiência visual rica e facilidade de aprendizado.

---

## 📁 Estrutura dos Arquivos

| Arquivo | Descrição |
|---|---|
| `operacoes.py` | Módulo matemático puro (soma, subtração, multiplicação, divisão e porcentagem). |
| `main.py` | Interface interativa de linha de comando (terminal) com cores ANSI, molduras Unicode e histórico de operações. |
| `test_calculadora.py` | Testes automatizados usando a biblioteca padrão `unittest` do Python. |
| `index.html` | Interface visual web moderna, autônoma (funciona offline), com suporte a teclado físico, efeitos sonoros e histórico dinâmico. |
| `executar_calculadora.bat` | Atalho no Windows para iniciar a calculadora no terminal com um clique duplo. |
| `abrir_web.bat` | Atalho no Windows para abrir a versão web no seu navegador padrão. |

---

## 🚀 Como Executar o Projeto

### Opção 1: Terminal Python
Abra o terminal ou prompt de comando dentro desta pasta e digite:
```bash
python main.py
```
*(Se estiver no Windows, você também pode simplesmente dar um clique duplo no arquivo `executar_calculadora.bat`)*

### Opção 2: Interface Web Gráfica
Basta abrir o arquivo `index.html` em qualquer navegador (Google Chrome, Edge, Firefox) ou dar um duplo clique no arquivo `abrir_web.bat`.

### Opção 3: Executar os Testes Automatizados
Para verificar a integridade de todas as operações:
```bash
python -m unittest test_calculadora.py
```

---

## 💡 Funcionalidades Principais
- ➕ **Soma**
- ➖ **Subtração**
- ✖️ **Multiplicação**
- ➗ **Divisão** (com proteção contra divisão por zero)
- ％ **Porcentagem** (cálculo de taxa percentual sobre base)
- 📜 **Histórico de Cálculos** (consulte as contas anteriores na mesma sessão)
- 🛡️ **Validação contra entradas inválidas** (trata digitação de letras ou caracteres especiais)
