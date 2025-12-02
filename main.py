"""
Aqui é o script principal que monta as instâncias, chama o solver
e guarda tudo num CSV para o relatório da disciplina.
"""
import random
import csv
from solver import resolver_bin_packing

# --- Configurações do Experimento [cite: 20, 96, 97, 101, 102] ---
TAMANHOS = [20, 50, 100]  # quantos itens por instância
CAPACIDADE = 30           # capacidade fixa da caixa
REPETICOES = 3            # quantas vezes rodar por tamanho
LIMITE_TEMPO = 30.0       # limite de tempo (segundos)
ARQUIVO_SAIDA = "results.csv"

def gerar_pesos(n, seed):
    """Gero os pesos dos itens entre 1 e 10 usando uma semente para repetir."""
    random.seed(seed)
    return [random.randint(1, 10) for _ in range(n)]

def main():
    print(f"Iniciando: tamanhos {TAMANHOS}, reps {REPETICOES}, capacidade {CAPACIDADE}")
    
    results_data = []
    
    # Cabeçalho do CSV conforme solicitado na Tabela [cite: 27]
    headers = ["Instância", "#itens", "C", "Tempo (s)", "#Caixas", "Best Bound", "Gap (%)", "Status"]

    experiment_count = 0
    total_experiments = len(TAMANHOS) * REPETICOES

    for size in TAMANHOS:
        for rep in range(1, REPETICOES + 1):
            experiment_count += 1
            instance_name = f"inst_{size}_{rep}"
            
            # Seed única para cada combinação (size * 1000 + rep) garante reprodutibilidade
            current_seed = size * 1000 + rep
            pesos = gerar_pesos(size, current_seed)
            
            print(f"[{experiment_count}/{total_experiments}] Rodando {instance_name} (n={size})...", end=" ")
            
            # Chama o solver
            metrics = resolver_bin_packing(pesos, CAPACIDADE, LIMITE_TEMPO)
            
            print(f"Done. Caixas: {metrics['objective']} | Tempo: {metrics['time_seconds']:.2f}s")
            
            # Prepara a linha para o CSV
            row = {
                "Instância": instance_name,
                "#itens": size,
                "C": CAPACIDADE,
                "Tempo (s)": round(metrics['time_seconds'], 4),
                "#Caixas": int(metrics['objective']),
                "Best Bound": round(metrics['best_bound'], 2),
                "Gap (%)": round(metrics['gap_percent'], 2),
                "Status": metrics['status']
            }
            results_data.append(row)

    # Salvando em CSV (forma simples)
    with open(ARQUIVO_SAIDA, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(results_data)
    print(f"\nSucesso! Resultados salvos em '{ARQUIVO_SAIDA}'.")
    print("Obs: limite de tempo do solver = 30s. Se o Gap > 0% nas instâncias maiores, significa que a solução é viável mas pode não ser ótima provada.")

if __name__ == "__main__":
    main()