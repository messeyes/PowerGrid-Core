
class Sensor:

    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
        self.leituras = []

    def adicionar_leitura(self, leitura):
        self.leituras.append(leitura)

    def obter_leituras(self):
        return self.leituras

    def __str__(self):
        return (
            f"Sensor: {self.id} | "
            f"Nome: {self.nome} | "
            f"Quantidade de leituras: {len(self.leituras)} | "
        )