# Bin Packing Problem Solver - Trabalho 2 (PO)

Este projeto implementa uma solução para o **Problema do Empacotamento (Bin Packing Problem)** utilizando Programação por Restrições (CP) com a biblioteca **Google OR-Tools**. O objetivo é minimizar o número de caixas necessárias para alocar um conjunto de itens com pesos variados, respeitando uma capacidade fixa por caixa.

## 📋 Visão Geral

O projeto foi estruturado para realizar experimentos computacionais automatizados, gerando instâncias sintéticas de diferentes tamanhos, resolvendo-as e coletando métricas de desempenho para análise posterior.

### Funcionalidades Principais
- **Geração de Instâncias:** Cria cenários com 20, 50 e 100 itens (pesos aleatórios entre 1 e 10).
- **Solver Otimizado:** Utiliza o solver CP-SAT do OR-Tools com restrições de quebra de simetria para melhor desempenho.
- **Coleta de Métricas:** Registra tempo de execução, número de caixas, *best bound*, gap de otimalidade e status da solução.
- **Visualização:** Gera gráficos automáticos relacionando o tamanho da instância com o tempo de execução e a qualidade da solução.

## 🛠️ Pré-requisitos

Devido a requisitos de compatibilidade da biblioteca `ortools`, este projeto requer:
- **Python 3.11** (Versões mais recentes como 3.12+ podem não ter suporte oficial ainda para o OR-Tools).

## 🚀 Instalação

1. **Verifique sua versão do Python:**
   Certifique-se de ter o Python 3.11 instalado. No Windows, você pode verificar e usar o "Python Launcher" (`py`):
   ```bash
   py --list
   ```

2. **Instale as dependências:**
   Utilize o comando abaixo para garantir a instalação no ambiente Python 3.11:
   ```bash
   py -3.11 -m pip install ortools pandas matplotlib
   ```

## ▶️ Como Executar

### 1. Rodar os Experimentos
O script principal gera as instâncias, executa o solver e salva os resultados em `results.csv`.
```bash
py -3.11 main.py
```
*Tempo estimado: 1 a 2 minutos.*

### 2. Gerar Gráficos de Análise
Após a execução do passo anterior, gere os gráficos de desempenho (`analise_bin_packing.png`):
```bash
py -3.11 plots.py
```

## 📂 Estrutura do Projeto

| Arquivo | Descrição |
|---------|-----------|
| `main.py` | **Orquestrador:** Define os parâmetros do experimento (tamanhos, capacidade, repetições), gera os dados, chama o solver e exporta o CSV. |
| `solver.py` | **Núcleo:** Contém a função `solve_bin_packing`. Implementa o modelo matemático (variáveis, restrições e função objetivo) usando OR-Tools. |
| `plots.py` | **Visualização:** Lê o arquivo `results.csv` e gera gráficos comparativos de Tempo e Solução. |
| `results.csv` | **Saída:** Arquivo gerado automaticamente contendo os dados brutos de todas as execuções. |

## 🧠 Detalhes da Modelagem (`solver.py`)

O problema foi modelado como um problema de satisfação de restrições (CP):
- **Variáveis:** 
  - $x_{i,j}$: Binária, indica se o item $i$ está na caixa $j$.
  - $y_j$: Binária, indica se a caixa $j$ foi utilizada.
- **Restrições:**
  1. Cada item deve estar em exatamente uma caixa.
  2. A soma dos pesos em uma caixa não pode exceder sua capacidade (se a caixa for usada).
  3. **Quebra de Simetria:** Força o uso das caixas em ordem ($y_j \leq y_{j-1}$) para reduzir o espaço de busca e acelerar a convergência.
- **Objetivo:** Minimizar $\sum y_j$.

## 📊 Interpretando os Resultados

No arquivo `results.csv`, você encontrará:
- **Status:** `OPTIMAL` (solução ótima comprovada) ou `FEASIBLE` (solução viável encontrada, mas pode não ser a ótima se o tempo acabou).
- **Gap (%):** Diferença percentual entre a solução encontrada e o melhor limite inferior teórico. Um Gap de 0.0% indica otimalidade comprovada.
- **Tempo (s):** Tempo de parede (*wall time*) gasto pelo solver.

---
*Desenvolvido para a disciplina de Pesquisa Operacional (UFF).*

## 📝 Próximos Passos (Sua "To-Do List")

1. **Instalação:** Certifique-se de instalar as dependências:
   ```bash
   pip install ortools pandas matplotlib
   ```

2. **Execução:** Rode `python main.py`. Isso vai demorar cerca de 1 a 2 minutos no total (devido às instâncias de 100 itens).

3. **Relatório:** Pegue o arquivo `results.csv`. Abra no Excel, formate como tabela e copie para a seção **5. Resultados Obtidos** do seu relatório.

4. **Análise:** Ao escrever a **Discussão**, observe o **Gap** na instância de 100 itens. Se o Gap for > 0%, significa que o solver parou pelo *Time Limit* (30s) e a solução pode não ser a ótima global, embora seja viável. Isso é um ponto excelente para discutir nas "Limitações".

