from model.hierarquia import inserir, em_ordem, altura, esta_balanceada


class Relatorio:

    @staticmethod
    def gerar(leituras):

        if not leituras:
            return "Nenhuma leitura disponível para gerar o relatório."

        raiz = None

        for leitura in leituras:
            raiz = inserir(raiz, leitura)

        linhas = []

        linhas.append("")
        linhas.append("========================================")
        linhas.append("       RELATÓRIO POWERGRID CORE")
        linhas.append("========================================")

        linhas.append("")
        linhas.append(f"Total de leituras: {len(leituras)}")

        nos = em_ordem(raiz)

        linhas.append(f"Total de sensores: {len(nos)}")

        linhas.append("")
        linhas.append("---------- ESTRUTURA HIERÁRQUICA ----------")

        for no in nos:
            linhas.append(
                f"Sensor ID: {no.sensor_id} | "
                f"Leituras: {len(no.leituras)}"
            )

        linhas.append("")
        linhas.append("---------- ÁRVORE ----------")

        linhas.append(f"Altura da árvore: {altura(raiz)}")

        if esta_balanceada(raiz):
            linhas.append("Árvore balanceada: SIM")
        else:
            linhas.append("Árvore balanceada: NÃO")

        linhas.append("")
        linhas.append("========================================")

        return "\n".join(linhas)
