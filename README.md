# Relatorio de gastos de extrato bancario em planilhas 🧾📊

Este projeto é uma aplicação simples de análise financeira pessoal, desenvolvida em Python, que permite ao usuário:

- Importar extratos financeiros em formato `.xlsx`
- Classificar automaticamente os gastos por categoria
- Gerar gráficos interativos de despesas
- Exibir um resumo de saldo disponível com base no salário
- Simular sobras mensais após os gastos

## Funcionalidades

- 📁 **Leitura de planilhas (.xlsx)** com colunas: Data, Valor, Descrição
- 🤖 **Classificação automática de transações** (ex: alimentação, transporte, salário, etc.)
- 📊 **Geração de gráficos**:
  - Pizza com porcentagem e valor de cada categoria
  - Salário vs. despesas mensais
- 💰 **Cálculo do saldo restante** com base nos lançamentos

## Tecnologias utilizadas

- Python 3.11+
- pandas
- matplotlib
- openpyxl

## Como usar

1. Clone este repositório
2. Instale as dependências:
   ```bash
   pip install pandas matplotlib openpyxl
