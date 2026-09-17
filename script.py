# MENU PRINCIPAL:
def menu_principal():
    print("-=-=-=-=-=- UNIVILLE ENQUETES -=-=-=-=-=-")
    print("1. Cadastrar opções de enquete.")
    print("2. Menu.")
    print("3. Sair")

    return input("Digite o número da opção desejada: ")


# MENÚ DE OPÇÕES DE ENQUETE:
def menu():
    print("-=-=-=-=- MENU DE ENQUETE -=--=-=-")
    opcoes_menu = [
        " Listar opções.",
        " Resgistrar voto.",
        " Consultar votos.",
        " Mostrar resultado.",
        " Mostrar vencedor.",
        " Voltar ao menu principal."
    ]

    for i, texto in enumerate(opcoes_menu, start=1):
        print(f"{i}. {texto}")

    return input("Escolha uma opção: ")


# CADASTRO DE OPÇÕES DE ENQUETE:
def cadastrar_opcao(votos):
    opcao = input("Digite a opção a ser cadastrada: ")

    if opcao not in votos:

        votos[opcao] = 0
        print("Opção cadastrada com sucesso!")

    else:

        print("Essa opção já existe.")


# MOSTRAR OPÇÕES CADASTRADAS:
def listar_opcoes(opcoes):
    print("As opções cadastradas são: ")

    for i, opcao in enumerate(opcoes, start=1):
        print(f"{i}. {opcao}")


# REGISTRAR VOTOS:
def registro_votos(votos):
    opcoes = list(votos)
    listar_opcoes(votos)
    escolha = int(input("Digite o número da opção que deseja votar: "))

    if 1 <= escolha <= len(opcoes):

        votos[opcoes[escolha - 1]] += 1
        print("Voto registrado com sucesso!")

    else:

        print("Opção inválida.")


# CONSULTAR VOTOS:

def consultar_votos(votos):
    print("Quantidade de votos por opção: ")

    for opcao, quantidade in votos.items():
        print(f"{opcao}: {quantidade} votos")


# MOSTRAR RESULTADO:

def mostrar_resultado(votos):
    total = sum(votos.values())
    print("Resultado da enquete: ")

    for opcao, quantidade in votos.items():
        percentual = (quantidade / total * 100) if total > 0 else 0
        print(f"{opcao}: {quantidade} votos ({percentual:.2f}%)")


# MOSTRAR VENCEDOR:
def mostrar_vencedor(votos):
    if not votos:
        print("Nenhuma opção cadastrada.")
        return

    max_votos = max(votos.values())
    vencedores = [opcao for opcao, quantidade in votos.items() if quantidade == max_votos]

    if len(vencedores) > 1:

        print("Empate entre as opções: ")

        for v in vencedores:
            print(f"- {v} ({max_votos} votos)")

    else:

        print(f"Opção vencedora: {vencedores[0]} com {max_votos} votos")


# AÇÕES DO PROGRAMA:
def acoes_programa():
    votos = {}
    # CHAMANDO AS FUNÇÕES DO MENU PRINCIPAL
    while True:
        escolha = menu_principal()
        if escolha == "1":
            cadastrar_opcao(votos)
        elif escolha == "2":
            # MENU DE OPÇÕES DE ENQUETE
            while True:
                sub_escolha = menu()
                if sub_escolha == "1":
                    listar_opcoes(votos)
                elif sub_escolha == "2":
                    registro_votos(votos)
                elif sub_escolha == "3":
                    consultar_votos(votos)
                elif sub_escolha == "4":
                    mostrar_resultado(votos)
                elif sub_escolha == "5":
                    mostrar_vencedor(votos)
                elif sub_escolha == "6":
                    break
                else:
                    print("Opção inválida. Tente novamente.")
        elif escolha == "3":
            print('-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-')
            print("Encerrando o programa...")

            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    acoes_programa()