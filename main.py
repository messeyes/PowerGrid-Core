from controller.PowerGrid import PowerGrid
from model.hierarquia import estrutura_hierarquica


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


def pausar():
    input("\nPressione Enter para voltar ao menu...")


def telemetria(controller):
    print("\n========== TELEMETRIA ==========")

    leituras = controller.criar_leituras(10)

    for leitura in leituras:
        controller.adicionar_leitura(leitura)

    print(f"\nQuantidade de leituras: {controller.quantidade_leituras()}")

    for leitura in controller.obter_leituras():
        print(leitura)

    pausar()


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
        pausar()
        return

    algoritmo = algoritmos[opcao]

    print("\nANTES DA ORDENAÇÃO:")

    for leitura in leituras:
        print(leitura)

    controller.sensor.leituras = leituras

    controller.ordenar_por_id(algoritmo)

    print("\nDEPOIS DA ORDENAÇÃO:")

    for leitura in controller.obter_leituras():
        print(leitura)

    pausar()


def testar_desempenho(controller):
    print("\n========== DESEMPENHO ==========")

    resultados = controller.executar_testes()

    controller.exibir_resultados(resultados)

    pausar()


def buscar_sensor(controller):
    print("\n========== BUSCA BINÁRIA ==========")

    if controller.quantidade_leituras() == 0:
        print("\nNenhuma leitura pode ser feita. Use a opção 1 - Telemetria primeiro.")
        pausar()
        return

    try:
        sensor_id = int(input("\nDigite o ID do sensor: "))
    except ValueError:
        print("\nID inválido. Digite um número inteiro.")
        pausar()
        return

    leituras = controller.buscar_por_sensor_id(sensor_id)

    if leituras:
        print(f"\nQuantidade de leituras: {len(leituras)}")
        for leitura in leituras:
            print(leitura)
    else:
        print("\nNenhuma leitura foi encontrada para esse sensor.")

    pausar()


def mostrar_hierarquia():
    print("\n========== ESTRUTURA HIERÁRQUICA ==========")
    cos = estrutura_hierarquica()
    cos.exibir()
    pausar()


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
            buscar_sensor(controller)

        elif opcao == "5":
            mostrar_hierarquia()

        elif opcao == "6":
            print("\nRelatórios - ainda não implementados.")
            pausar()

        elif opcao == "0":
            print("\nEncerrando o PowerGrid Core...")
            break

        else:
            print("\nOpção inválida. Escolha um número do menu.")
            pausar()


if __name__ == "__main__":
    main()