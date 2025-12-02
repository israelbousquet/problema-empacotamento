"""
Aqui eu resolvo o problema de Empacotamento (Bin Packing) usando o OR-Tools.
A ideia é minimizar quantas caixas (y) a gente usa, colocando cada item (x)
em uma dessas caixas sem passar da capacidade.
"""
from ortools.sat.python import cp_model

def resolver_bin_packing(pesos, capacidade, limite_tempo_segundos=30):
    """
    Modelo didático do Bin Packing:
    - x[i,j] = 1 se o item i está na caixa j
    - y[j]   = 1 se a caixa j é usada
    Objetivo: minimizar a soma de y (ou seja, usar menos caixas).
    """
    # 1) Criando o modelo do CP-SAT
    model = cp_model.CpModel()

    num_itens = len(pesos)
    # No pior caso, cada item precisa de sua própria caixa
    num_caixas = num_itens

    # 2) Variáveis de decisão
    # Aqui eu crio as variáveis x que dizem em qual caixa cada item vai
    x = {}
    for i in range(num_itens):
        for j in range(num_caixas):
            x[i, j] = model.NewBoolVar(f'x_{i}_{j}')

    # Aqui eu crio as variáveis y que dizem se a caixa j está sendo usada
    y = {}
    for j in range(num_caixas):
        y[j] = model.NewBoolVar(f'y_{j}')

    # 3) Restrições do modelo
    # (i) Cada item deve ir em exatamente uma caixa
    for i in range(num_itens):
        model.Add(sum(x[i, j] for j in range(num_caixas)) == 1)

    # (ii) Capacidade da caixa: soma dos pesos dentro da caixa j não pode
    # passar de capacidade, e só conta se a caixa estiver sendo usada (y[j])
    for j in range(num_caixas):
        soma_pesos = sum(x[i, j] * pesos[i] for i in range(num_itens))
        model.Add(soma_pesos <= capacidade * y[j])

    # (iii) Quebra de simetria: usamos caixas em ordem para facilitar o solver
    for j in range(1, num_caixas):
        model.Add(y[j] <= y[j - 1])

    # 4) Objetivo: minimizar quantas caixas são usadas
    model.Minimize(sum(y[j] for j in range(num_caixas)))

    # 5) Configurando o solver (tempo limite e workers)
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = limite_tempo_segundos
    solver.parameters.log_search_progress = False
    solver.parameters.num_search_workers = 8

    # 6) Rodando o solver e coletando métricas
    status_val = solver.Solve(model)
    status_map = {
        cp_model.OPTIMAL: "OPTIMAL",
        cp_model.FEASIBLE: "FEASIBLE",
        cp_model.INFEASIBLE: "INFEASIBLE",
        cp_model.MODEL_INVALID: "INVALID",
        cp_model.UNKNOWN: "UNKNOWN",
    }

    status_str = status_map.get(status_val, "UNKNOWN")
    obj_value = solver.ObjectiveValue()
    best_bound = solver.BestObjectiveBound()
    wall_time = solver.WallTime()

    # Aqui eu calculo o Gap (%). Se for 0, quer dizer que provou ótimo.
    gap = 0.0
    if status_val in (cp_model.OPTIMAL, cp_model.FEASIBLE) and obj_value > 0:
        gap = abs((obj_value - best_bound) / obj_value) * 100
    elif status_val == cp_model.OPTIMAL:
        gap = 0.0

    return {
        "status": status_str,
        "objective": obj_value,
        "best_bound": best_bound,
        "time_seconds": wall_time,
        "gap_percent": gap
    }