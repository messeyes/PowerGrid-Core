from controller.PowerGrid import PowerGrid


def mostrar_menu():
    print("\n========================================")
    print("           POWERGRID CORE")
    print("========================================")
    print("1 - Telemetria")
    print("2 - Ordenação")
    print("3 - Testar desempenho")
    print("4 - Busca binária")
    print("5 - Estrutura hierárquica")
    print("6 - Relatórios")
    print("0 - Sair")
    print("========================================")


def telemetria(controller):
    print("\n========== TELEMETRIA ==========")

    leituras = controller.criar_leituras(10)

    for leitura in leituras:
        controller.adicionar_leitura(leitura)

    print(f"\nQuantidade de leituras: {controller.quantidade_leituras()}")

    for leitura in controller.obter_leituras():
        print(leitura)


def testar_ordenacao(controller):
    print("\n========== ORDENAÇÃO ==========")

    leituras = controller.criar_leituras(10)

    print("\nEscolha o algoritmo:")
    print("1 - Insertion Sort")
    print("2 - Selection Sort")
    print("3 - Merge Sort")
    print("4 - Quick Sort")
    print("0 - Voltar")

    opcao = input("\nDigite o número: ")

    algoritmos = {
        "1": "insertion",
        "2": "selection",
        "3": "merge",
        "4": "quick"
    }

    if opcao == "0":
        return

    if opcao not in algoritmos:
        print("\nOpção inválida.")
        return

    algoritmo = algoritmos[opcao]

    print("\nANTES DA ORDENAÇÃO:")

    for leitura in leituras:
        print(leitura)

    # Coloca as leituras no sensor
    controller.sensor.leituras = leituras

    controller.ordenar_por_id(algoritmo)

    print("\nDEPOIS DA ORDENAÇÃO:")

    for leitura in controller.obter_leituras():
        print(leitura)


def testar_desempenho(controller):
    print("\n========== DESEMPENHO ==========")

    resultados = controller.executar_testes()

    controller.exibir_resultados(resultados)


def main():

    controller = PowerGrid()

    while True:

        mostrar_menu()

        opcao = input("Digite o número da opção: ")

        if opcao == "1":
            telemetria(controller)

        elif opcao == "2":
            testar_ordenacao(controller)

        elif opcao == "3":
            testar_desempenho(controller)

        elif opcao == "4":
            print("\nBusca binária - ainda não implementada.")

        elif opcao == "5":
            print("\nEstrutura hierárquica - ainda não implementada.")

        elif opcao == "6":
            print("\nRelatórios - ainda não implementados.")

        elif opcao == "0":
            print("\nEncerrando o PowerGrid Core...")
            break

        else:
            print("\nOpção inválida. Escolha um número do menu.")


if __name__ == "__main__":
    main()