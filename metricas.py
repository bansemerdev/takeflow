def classificar_projeto(valor, limite_medio=500, limite_alto=1000):
    """
    Classifica um projeto com base no valor recebido.

    Parâmetros:
        valor (float): Valor recebido pelo projeto.
        limite_medio (float): Limite para classificação de médio valor.
        limite_alto (float): Limite para classificação de alto valor.

    Retorno:
        str: Classificação do projeto.
    """
    if valor >= limite_alto:
        return "Projeto de alto valor"
    elif valor >= limite_medio:
        return "Projeto de médio valor"
    else:
        return "Projeto de baixo valor"


def calcular_faturamento(projetos):
    """
    Calcula o valor total recebido pelos projetos.

    Parâmetros:
        projetos (list): Lista de projetos cadastrados.

    Retorno:
        float: Soma dos valores recebidos.
    """

    total = 0

    for projeto in projetos:
        total += projeto[3]

    return total


def calcular_total_horas(projetos):
    """
    Calcula o total de horas trabalhadas em todos os projetos.

    Parâmetros: 
        projetos (list): lista de projetos cadastrados, onde cada projeto é representado por uma lista contendo informações como nome, tipo, horas trabalhadas, valor recebido e classificação.
    
    Retorno:
        float: Soma das horas trabalhadas.
    """

    total_horas = 0

    for projeto in projetos:
        total_horas += projeto[2]  # As horas trabalhadas estão na posição 2 da lista do projeto

    return total_horas


def calcular_valor_medio(projetos):
    """
    Calcula o valor médio recebido por projeto.
    
    Parâmetros:
        projetos (list): lista de projetos cadastrados, onde cada projeto é representado por uma lista contendo informações como nome, tipo, horas trabalhadas, valor recebido e classificação.
    
    Retorno:
        float: Valor médio recebido por projeto.
    """
    if len(projetos) == 0:
        return 0

    faturamento_total = calcular_faturamento(projetos)

    return faturamento_total / len(projetos)