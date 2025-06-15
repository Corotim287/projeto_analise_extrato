import pandas as pd
import matplotlib.pyplot as plt

def carregar_dados(caminho_arquivo):
    return pd.read_excel(caminho_arquivo)

def classificar_categoria(descricao):
    descricao = descricao.lower()

    if any(x in descricao for x in ['ifood', 'mcdonald', 'supermercado', 'padaria']):
        return 'Alimentação'
    elif any(x in descricao for x in ['uber', '99', 'gasolina', 'manutenção']):
        return 'Transporte'
    elif any(x in descricao for x in ['netflix', 'spotify', 'amazon prime', 'youtube premium']):
        return 'Assinaturas'
    elif any(x in descricao for x in ['cinema', 'bar', 'show', 'parque']):
        return 'Lazer'
    elif any(x in descricao for x in ['salário', 'pagamento']):
        return 'Renda'
    elif any(x in descricao for x in ['curso', 'udemy', 'livro']):
        return 'Educação'
    elif any(x in descricao for x in ['farmácia', 'consulta', 'exame']):
        return 'Saúde'
    else:
        return 'Outros'

def tratar_dados(df):
    #
    #       Realiza limpeza básica do DataFrame:
    #     - Converte a coluna 'Data' para datetime
    #     - Remove linhas com datas inválidas
    #     - Garante que a coluna 'Valor' é numérica
    #     - Remove linhas com valores nulos ou negativos
    #
    # Converter coluna 'Data' para datetime
    df['Data'] = pd.to_datetime(df['Data'], errors='coerce')

    # Remover linhas com datas inválidas
    df = df.dropna(subset=['Data'])

    # Garantir que 'Valor' é numérico
    df['Valor'] = pd.to_numeric(df['Valor'], errors='coerce')

    # Remover linhas com valor nulo ou negativo
    df = df.dropna(subset=['Valor'])
    df = df[df['Valor'] >= 0]

    return df

def func_autopct(pct, valores):
    # pct é o valor percentual (float)
    # valores é o array com os valores absolutos de cada fatia
    absolute = int(round(pct/100.*sum(valores)))
    return f"{pct:.1f}%\n(R$ {absolute:,})".replace(',', '.')

def plotar_pizza_categorias(df):
    df['Categoria'] = df['Descrição'].apply(classificar_categoria)

    total_renda = df[df['Categoria'] == 'Renda']['Valor'].sum()
    df_despesas = df[df['Categoria'] != 'Renda']
    resumo = df_despesas.groupby('Categoria')['Valor'].sum()

    total_despesas = resumo.sum()
    saldo = total_renda - total_despesas
    percentual_sobra = (saldo / total_renda) * 100 if total_renda > 0 else 0

    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Gráfico 1 - Pizza com despesas
    axes[0].pie(
        resumo,
        labels=resumo.index,
        autopct=lambda pct: func_autopct(pct, resumo),
        startangle=140,
        colors=plt.cm.Set3.colors
    )
    axes[0].set_title('Despesas por Categoria')
    axes[0].axis('equal')

    # Gráfico 2 - Barras com salário, despesas e saldo
    categorias = ['Salário Líquido', 'Despesas Totais', 'Saldo Restante']
    valores = [total_renda, total_despesas, saldo]
    cores = ['#4CAF50', '#F44336', '#2196F3']  # verde, vermelho, azul

    bars = axes[1].bar(categorias, valores, color=cores)
    axes[1].set_title('Resumo Financeiro')
    axes[1].bar_label(bars, labels=[f'R$ {v:,.2f}' for v in valores], padding=3)

    # Exibir percentual sobra como texto extra no gráfico de barras
    axes[1].text(2, saldo * 0.5, f'Sobra: {percentual_sobra:.1f}%', fontsize=12, color='black', fontweight='bold')

    plt.tight_layout()
    plt.show()

def calcular_despesas(df):
    total_renda = df[df['Categoria'] == 'Renda']['Valor'].sum()
    total_despesas = df[df['Categoria'] != 'Renda']['Valor'].sum()

    return total_renda-total_despesas

def main():
    caminho = 'gastos_exemplo (2).xlsx'
    df = carregar_dados(caminho)
    if df.empty:
        return

    df['Categoria'] = df['Descrição'].apply(classificar_categoria)
    df = tratar_dados(df)

    print("Dados carregados, classificados e tratados com sucesso!")

    plotar_pizza_categorias(df)
    print(f"Saldo liquido:{calcular_despesas(df)}")

if __name__ == '__main__':
    main()