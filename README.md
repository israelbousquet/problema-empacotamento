# Empacotamento (Bin Packing) – Trabalho 2 (PO)

Projeto da disciplina de **Pesquisa Operacional (UFF)**. Resolvemos o **Problema do Empacotamento (Bin Packing)** usando **OR-Tools (CP-SAT)**. Maior detalhamento na continuação do readme.

## 📋 Visão Geral

O projeto foi estruturado para realizar experimentos computacionais automatizados, gerando instâncias sintéticas de diferentes tamanhos, resolvendo-as e coletando métricas de desempenho para análise posterior.

### O que o código faz
- Gera instâncias com 20, 50 e 100 itens (pesos aleatórios de 1 a 10).
- Monta o modelo no OR-Tools com variáveis `x` (item na caixa) e `y` (caixa usada), exatamente como vemos na teoria.
- Roda o solver com limite de tempo de 30s.
- Salva tudo em `results.csv` para usar no relatório.
- Gera um gráfico simples (`analise_bin_packing.png`) com tempo médio e caixas médias por tamanho.

## 🛠️ Pré-requisitos

- **Python 3.11** (o OR-Tools é compatível com essa versão).

## 🚀 Instalação

1. **Verifique sua versão do Python:**
   Obrigatório Python 3.11 instalado. Comando para identificar versões instaladas:
   ```bash
   py --list
   ```

2. **Instale as dependências:**
   Indicado utilizar o `python` para download das dependências:
   ```bash
   py -3.11 -m pip install ortools pandas matplotlib
   python -m pip install ortools pandas matplotlib
   ```

## ▶️ Como Executar

### 1. Rodar os Experimentos
Gera as instâncias, roda o solver e salva em um excel: `results.csv`. Comandos para executar main.py:
```bash
py -3.11 main.py
python main.py
```
Execução pode chegar a demorar entre 1 a 2 minutos dependendo das configurações no contexto da execução, a demora ocorre pela quantidade de instâncias.

### 2. Gerar Gráficos
Após criar o CSV, é possível gerar um gráfico: `analise_bin_packing.png`. Comandos para executar plots.py:
```bash
py -3.11 plots.py
python plots.py
```

## 📂 Estrutura do Projeto

| Arquivo | Descrição |
|---------|-----------|
| `main.py` | Gera instâncias, chama o solver, e salva o CSV. |
| `solver.py` | Onde está o modelo do OR-Tools (variáveis x e y, restrições e objetivo). Função é `resolver_bin_packing`. |
| `plots.py` | Lê excel `results.csv` e cria um gráfico simples para o relatório. |
| `results.csv` | **Saída:** Arquivo gerado automaticamente contendo os dados brutos de todas as execuções. |

## 🧠 Como é o modelo (bem direto)

- **Variáveis:**
   - `x[i,j]` = 1 se o item i está na caixa j.
   - `y[j]` = 1 se a caixa j foi usada.
- **Restrições:**
   1. Cada item vai em exatamente uma caixa.
   2. A soma dos pesos dentro da caixa j não passa da capacidade (só conta se `y[j]=1`).
   3. Quebra de simetria: usamos caixas na ordem (`y[j] <= y[j-1]`).
- **Objetivo:** Minimizar a soma de `y[j]` (menos caixas usadas).

## 📊 Sobre os resultados

No `results.csv` tem:
- **Status:** `OPTIMAL` (provou ótimo) ou `FEASIBLE` (achou solução viável, mas talvez não provou ótimo porque acabou o tempo).
- **Gap (%):** Se for `0.0`, ótimo provado. Se for `> 0%` na instância de 100 itens, é porque bateu o **time limit (30s)**.
- **Tempo (s):** tempo que o solver gastou.

---
*Projeto da disciplina de Pesquisa Operacional (UFF).* 

## 📝 Passo a Passo Guiado

1. **Instalar dependências**:
   ```bash
   py -3.11 -m pip install ortools pandas matplotlib
   python -m pip install ortools pandas matplotlib
   ```
2. **Rodar `main.py`** (gera arquivo `results.csv`).
3. **Rodar `plots.py`** (gera gráfico `analise_bin_packing.png`).
4. **Relatório**: abrir `results.csv` no Excel, formatar como tabela e colar na seção de Resultados. Na Discussão, comentar que se o **Gap** da instância de 100 itens for **> 0%**, é por causa do **time limit (30s)** — solução é viável, mas talvez não ótima provada (boa limitação para mencionar).

