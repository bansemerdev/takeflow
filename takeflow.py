# CineControl - Sistema de Coleta de Dados
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
    horas_trabalhadas = float(input("Horas trabalhadas: "))
    while horas_trabalhadas <= 0:
        print("Valor inválido. As horas trabalhadas devem ser maiores que zero.")
        horas_trabalhadas = float(input("Digite novamente as horas trabalhadas: "))
    valor_projeto = float(input("Valor recebido pelo projeto (R$): "))

    while valor_projeto <= 0:
        print("Valor inválido. O valor recebido deve ser maior que zero.")
        valor_projeto = float(input("Digite novamente o valor recebido (R$): "))
    # Classificação do projeto de acordo com o valor recebido
    if valor_projeto >= 1000:
        classificacao = "Projeto de alto valor"
    elif valor_projeto >= 500:
        classificacao = "Projeto de médio valor"
    else:
        classificacao = "Projeto de baixo valor"
    # Armazena os dados do projeto em uma lista
    projeto = [nome_projeto, tipo_projeto, horas_trabalhadas,
               valor_projeto, classificacao]

    projetos.append(projeto)
    # Exibição dos dados cadastrados
    print("\n--- RESUMO DO PROJETO ---")
    print(f"Projeto: {nome_projeto}")
    print(f"Tipo: {tipo_projeto}")
    print(f"Horas trabalhadas: {horas_trabalhadas}")
    print(f"Valor recebido: R$ {valor_projeto:.2f}")
    print(f"Classificação: {classificacao}")

    # Pergunta se o usuário deseja realizar outro cadastro
    continuar = input("\nDeseja cadastrar outro projeto? (s/n): ").lower()

    while continuar != "s" and continuar != "n":
        print("Opção inválida. Digite apenas 's' para sim ou 'n' para não.")
        continuar = input("Deseja cadastrar outro projeto? (s/n): ").lower()
    # Variáveis para os cálculos do relatório
total_horas = 0
faturamento_total = 0

for projeto in projetos:
    total_horas += projeto[2]
    faturamento_total += projeto[3]
# Relatório final dos projetos cadastrados
print("\n" + "=" * 50)
print("          RELATÓRIO FINAL")
print("=" * 50)

for projeto in projetos:
    print(f"\nProjeto: {projeto[0]}")
    print(f"Tipo: {projeto[1]}")
    print(f"Horas trabalhadas: {projeto[2]}")
    print(f"Valor recebido: R$ {projeto[3]:.2f}")
    print(f"Classificação: {projeto[4]}")
print("\n--- TOTAIS ---")
print(f"Quantidade de projetos: {len(projetos)}")
print(f"Total de horas trabalhadas: {total_horas}")
print(f"Faturamento total: R$ {faturamento_total:.2f}")
media_valor = faturamento_total / len(projetos)
print(f"Valor médio por projeto: R$ {media_valor:.2f}")

print("\nCadastro encerrado. Obrigado por utilizar o CineControl!")