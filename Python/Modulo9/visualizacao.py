import pandas as pd
import seaborn as sns


def gerar_grafico(nome_arquivo: str):
    # Extraindo as colunas hora e taxa

    df = pd.read_csv('./taxa-cdi.csv')

    # Salvando no grafico

    grafico = sns.lineplot(x=df['hora'], y=df['taxa'])
    _ = grafico.set_xticklabels(labels=df['hora'], rotation=90)
    grafico.get_figure().savefig(f"{nome_arquivo}.png")
