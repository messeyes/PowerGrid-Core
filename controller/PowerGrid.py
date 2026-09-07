
import random
import time

from model.Leitura import Leitura
from model.Sensor import Sensor
from service.Buscador import Buscador
from service.Ordenador import Ordenador


class PowerGrid:

    def __init__(self):
        self.sensor = Sensor(1, "Sensor 01")


    # sessão de telerimetria
    def adicionar_leitura(self, leitura):
        self.sensor.adicionar_leitura(leitura)

    def obter_leituras(self):
        return self.sensor.obter_leituras()

    def quantidade_leituras(self):
        return len(self.obter_leituras())


    # criando leituras
    def criar_leituras(self, quantidade):
        leituras = []

        for i in range(quantidade):

            leitura = Leitura(
                random.randint(1, quantidade),
                f"2026-09-10 12:{i % 60:02d}",
                random.randint(20, 160),
                random.randint(180, 250)
            )

            leituras.append(leitura)

        return leituras


    # chamando os ordenadores
    def ordenar_por_id(self, nome_algoritmo):

        algoritmos = {
            "insertion": Ordenador.insertion_sort,
            "selection": Ordenador.selection_sort,
            "merge": Ordenador.merge_sort,
            "quick": Ordenador.quick_sort
        }

        algoritmo = algoritmos.get(nome_algoritmo.lower())

        if algoritmo is None:
            raise ValueError("Algoritmo de ordenação inválido.")

        resultado = algoritmo(
            self.sensor.leituras,
            lambda x: x.sensor_id
        )


        if resultado is not None:
            self.sensor.leituras = resultado


    # pega a ordem do ordenar_por_id pra ser a mesma ordem da busca binaria
    def buscar_por_sensor_id(self, sensor_id):
        self.ordenar_por_id("merge")
        return Buscador.busca_binaria(self.obter_leituras(), sensor_id)


    # testes de tempo
    def medir_tempo(self, algoritmo, leituras):

        copia = leituras.copy()

        inicio = time.perf_counter()

        resultado = algoritmo(
            copia,
            lambda x: x.sensor_id
        )

        fim = time.perf_counter()

        tempo_ms = (fim - inicio) * 1000

        return tempo_ms


    # teste dos ordenadores
    def testar_algoritmos(self, quantidade):

        leituras = self.criar_leituras(quantidade)

        algoritmos = {
            "Insertion Sort": Ordenador.insertion_sort,
            "Selection Sort": Ordenador.selection_sort,
            "Merge Sort": Ordenador.merge_sort,
            "Quick Sort": Ordenador.quick_sort
        }

        resultados = {}

        for nome, algoritmo in algoritmos.items():

            tempo = self.medir_tempo(
                algoritmo,
                leituras
            )

            resultados[nome] = tempo

        return resultados


    # testes com diferentes quantidades de leituras
    def executar_testes(self):

        quantidades = [100, 500, 1000, 2000, 5000]

        resultados = []

        for quantidade in quantidades:

            tempos = self.testar_algoritmos(quantidade)

            resultados.append({
                "quantidade": quantidade,
                "Insertion Sort": tempos["Insertion Sort"],
                "Selection Sort": tempos["Selection Sort"],
                "Merge Sort": tempos["Merge Sort"],
                "Quick Sort": tempos["Quick Sort"]
            })

        return resultados


    def exibir_resultados(self, resultados):

        print(
            f"{'Leituras':<12}"
            f"{'Insertion':<16}"
            f"{'Selection':<16}"
            f"{'Merge':<16}"
            f"{'Quick':<16}"
        )

        print("-" * 75)

        for resultado in resultados:

            print(
                f"{resultado['quantidade']:<12}"
                f"{resultado['Insertion Sort']:<16.4f}"
                f"{resultado['Selection Sort']:<16.4f}"
                f"{resultado['Merge Sort']:<16.4f}"
                f"{resultado['Quick Sort']:<16.4f}"
            )

        print("=" * 75)
