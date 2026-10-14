# TakeFlow - Sistema de Gestão Audiovisual
# Sistema desenvolvido para uma empresa fictícia do setor audiovisual
from metricas import classificar_projeto, calcular_faturamento, calcular_total_horas, calcular_valor_medio
print("=" * 50)
print("              TAKEFLOW")
print("     Sistema de Gestão Audiovisual")
print("=" * 50)

print("\nBem-vindo ao TakeFlow!")
print("Cadastre e acompanhe os projetos da produtora.")

# Lista utilizada para armazenar os projetos cadastrados
projetos = []

# Variável que controla a repetição dos cadastros
continuar = "s"

while continuar == "s":

    # Coleta dos dados do projeto
    print("\n--- CADASTRO DE PROJETO ---")

    # Validação do nome do projeto
    while True:
        nome_projeto = input("Nome do projeto: ").strip()

        if nome_projeto:
            break

        print("O nome do projeto não pode ficar vazio.")

    #Tipos de projetos válidos
    tipos_validos = [
        "curta",
        "longa-metragem",
        "documentário",
        "videoclipe",
        "série",
        "outro"
    
    ]
    while True:
        tipo_projeto = input("Tipo do projeto (curta, longa-metragem, documentário, videoclipe, série, outro): ").strip().lower()

        if tipo_projeto in tipos_validos:
            break
        else:
            print("Tipo inválido. Por favor, escolha uma das opções válidas.")
            print(", ".join(tipos_validos))

    # Validação das horas trabalhadas
    while True:
        try:
            horas_trabalhadas = float(input("Horas trabalhadas: "))

            if horas_trabalhadas <= 0:
                print("As horas trabalhadas devem ser maiores que zero.")
                continue

            break

        except ValueError:
            print("Entrada inválida. Digite um número válido.")

    # Validação do valor recebido
    while True:
        try:
            valor_projeto = float(
                input("Valor recebido pelo projeto (R$): ")
            )

            if valor_projeto <= 0:
                print("O valor recebido deve ser maior que zero.")
                continue

            break

        except ValueError:
            print("Entrada inválida. Digite um número válido.")

    # Classificação utilizando a função criada
    classificacao = classificar_projeto(valor_projeto)

    # Armazena os dados do projeto em uma lista
    projeto = [
        nome_projeto,
        tipo_projeto,
        horas_trabalhadas,
        valor_projeto,
        classificacao
    ]

    projetos.append(projeto)

    # Exibição dos dados cadastrados
    print("\n--- RESUMO DO PROJETO ---")
    print(f"Projeto: {nome_projeto}")
    print(f"Tipo: {tipo_projeto}")
    print(f"Horas trabalhadas: {horas_trabalhadas}")
    print(f"Valor recebido: R$ {valor_projeto:.2f}")
    print(f"Classificação: {classificacao}")

    # Pergunta se o usuário deseja cadastrar outro projeto
    while True:
        continuar = input(
    "\nDeseja cadastrar outro projeto? (s/n): "
        ).strip().lower()

        if continuar in ["s", "n"]:
            break
        print("Opção inválida. Digite 's' para sim ou 'n' para não.")

#Calcula as métricas após finalizar os cadastros
faturamento_total = calcular_faturamento(projetos)
valor_medio = calcular_valor_medio(projetos)
total_horas = calcular_total_horas(projetos)

print("\n--- RELATÓRIO DE MÉTRICAS ---")
print(f"Faturamento total: R$ {faturamento_total:.2f}")
print(f"Total de horas trabalhadas: {total_horas}")
print(f"Valor médio por projeto: R$ {valor_medio:.2f}")