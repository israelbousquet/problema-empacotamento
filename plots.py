"""
Aqui eu faço gráficos simples a partir do CSV gerado pelo main.
Quero ver como o tempo e o número de caixas crescem com o tamanho.
"""
import pandas as pd
import matplotlib.pyplot as plt

def gerar_graficos(caminho_csv):
    try:
        df = pd.read_csv(caminho_csv)
    except FileNotFoundError:
        print(f"Arquivo {caminho_csv} não encontrado. Rode o main.py primeiro.")
        return

    # Agrupo por quantidade de itens e tiro a média para ficar mais estável
    df_grouped = df.groupby('#itens')[['Tempo (s)', '#Caixas']].mean().reset_index()

    # Vou usar uma configuração mais simples, sem estilos avançados
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # Gráfico 1: Número de itens x Tempo médio
    ax1.plot(df_grouped['#itens'], df_grouped['Tempo (s)'], marker='o', color='blue')
    ax1.set_title('Tempo médio por tamanho')
    ax1.set_xlabel('Número de itens')
    ax1.set_ylabel('Tempo (s)')
    ax1.grid(True)

    # Gráfico 2: Número de itens x Caixas médias usadas
    ax2.plot(df_grouped['#itens'], df_grouped['#Caixas'], marker='s', color='red')
    ax2.set_title('Caixas usadas por tamanho')
    ax2.set_xlabel('Número de itens')
    ax2.set_ylabel('Média de caixas')
    ax2.grid(True)

    plt.tight_layout()
    plt.savefig('analise_bin_packing.png')
    print("Gráfico salvo como 'analise_bin_packing.png'")
    plt.show()

if __name__ == "__main__":
    gerar_graficos("results.csv")