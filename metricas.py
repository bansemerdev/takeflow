def classificar_projeto(valor):
    """Classifica um projeto com base no valor recebido."""""
    if valor >= 1000:
        return "Projeto de alto valor"
    elif valor >= 500:
        return "Projeto de médio valor"
    else:
        return "Projeto de baixo valor"

def calcular_faturamento(projetos):
        """Calcula o valor total recebido pelos projetos."""

        total = 0

        for projeto in projetos:
            total += projeto [3] # O valor recebido está na posição 3 da lista do projeto

        return total
def calcular_total_horas(projetos):
    """Calcula o total de horas trabalhadas em todos os projetos."""

    total_horas = 0

    for projeto in projetos:
        total_horas += projeto[2]  # As horas trabalhadas estão na posição 2 da lista do projeto

    return total_horas
def calcular_valor_medio(projetos):
    faturamento_total = calcular_faturamento(projetos)

    if len(projetos) ==0:
        return 0

    return faturamento_total / len(projetos)