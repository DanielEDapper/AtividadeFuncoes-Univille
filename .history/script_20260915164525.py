import time

opcoes = []
votos = []

def iniciarPrograma():
    while True:
        print("""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                ENQUETES                ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

1 - Cadastrar Opção
2 - Listar Opções
3 - Registrar Voto na Enquete
4 - Consultar Quantidade de Votos
5 - Mostrar Resultado
6 - Mostrar Opção Vencedora
7 - Encerrar Programa""")

        opcao = int(input("O que deseja fazer?: "))

        match opcao:
            case 1:
                limpaTerminal()
                cadastrarOpcao()

                time.sleep(2)
            case 2:
                limpaTerminal()
                listarOpcao()

                time.sleep(2)
            case 3:
                registrarVoto()

                time.sleep(2)
            case 4:
                consultarQuantidadeVoto()

                time.sleep(2)
            case 5:
                mostrarResultado()

                time.sleep(2)
            case 6:
                mostrarOpcaoVencedor()
            case 7:
                print("""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃       PROGRAMA DE VOTOS ENCERRADO      ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛""")
                break
            case _:
                print("Opção invalida!")

def cadastrarOpcao():
    print("""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃          CADASTRAR NOVA OPÇÃO          ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛""")
    opcao = str(input("Digite a opção: "))

    if opcao not in opcoes:
        opcoes.append(opcao)
        votos.append(0)

        print("Opção cadastrada com sucesso!")

def listarOpcao():
    print("""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃           OPÇÕES CADASTRADAS           ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛""")

    if len(opcoes) == 0:
        print("Nenhuma opção cadastrada.")

    for i in range(len(opcoes)):
        print(f"{i + 1}. {opcoes[i]}")

def registrarVoto():
    print("""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             REGISTRAR VOTO             ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛""")
    if len(opcoes) == 0:
        print("Nenhuma opção registrada.")

    listarOpcao()

    try:
        escolha = int(input("Digite o número da opção: "))

        if escolha < 1 or escolha > len(opcoes):
            print("Opção inválida!")
            return

        votos[escolha-1] += 1
        print("Votos registrados com sucesso!")

    except ValueError:
        print("Digite apenas números.")

def consultarQuantidadeVoto():
    print("""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     CONSULTAR QUANTIDADE DE VOTOS      ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛""")

    if len(opcoes) == 0:
        print("Nenhuma opção registrada.")

    for i in range(len(opcoes)):
        print(f"{i + 1}. {opcoes[i]} - {votos[i]}")

def mostrarResultado():
    print("""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃           MOSTRAR RESULTADO            ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛""")


    if len(opcoes) == 0:
        print("Nenhuma opção registrada.")

    totalVotos = sum(votos)

    for i in range(len(opcoes)):
        quantidade = votos[i]

        if totalVotos == 0:
            percentualVoto = 0
        else:
            percentualVoto = (quantidade / totalVotos) * 100

        print(
            f"{opcoes[i]}:"
            f"{quantidade} voto(s) - "
            f"{percentualVoto}"
        )

def mostrarOpcaoVencedor():
    print("""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃         MOSTRAR OPÇÃO VENCEDOR         ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛""")


    if len(opcoes) == 0:
        print("Nenhuma opção registrada.")

    maiorQuantidade = max(votos)

    if maiorQuantidade == 0:
        print("Ainda não existem votos!")
        return

    vencedores = []

    for i in range(len(opcoes)):
        if votos[i] == maiorQuantidade:
            vencedores.append(opcoes[i])

    if len(vencedores) > 1:
        print("EMPATE")

        for opcao in vencedores:
            print(f"- {opcao}")


    else:
        print("Opção Vencedora")
        print(f"Vencedora: {vencedores[0]}")
        print(f"Quantidade de Votos: {maiorQuantidade}")

def limpaTerminal():
    print("""
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    """)


iniciarPrograma()