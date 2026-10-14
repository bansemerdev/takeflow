# TakeFlow - Sistema de Gestão Audiovisual
# Sistema desenvolvido para uma empresa fictícia do setor audiovisual

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

    nome_projeto = input("Nome do projeto: ")
    tipo_projeto = input(
        "Tipo do projeto (curta, documentário, publicidade etc.): "
    )

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

    # Classificação do projeto de acordo com o valor recebido
    if valor_projeto >= 1000:
        classificacao = "Projeto de alto valor"
    elif valor_projeto >= 500:
        classificacao = "Projeto de médio valor"
    else:
        classificacao = "Projeto de baixo valor"

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