
class Leitura:

    def __init__(self, sensor_id, timestamp, temperatura, tensao):
        self.sensor_id = sensor_id
        self.timestamp = timestamp
        self.temperatura = temperatura
        self.tensao = tensao
        self.severidade = self.calcular_severidade()


    def calcular_severidade(self):

        if self.temperatura >= 140:
            return "CRITICO"

        elif self.temperatura >= 90:
            return "ALERTA"

        else:
            return "NORMAL"

    def __str__(self):
        return (
            f"Sensor: {self.sensor_id} |"
            f"Timestamp: {self.timestamp} |"
            f"Temperatura: {self.temperatura} |"
            f"Tensao: {self.tensao} |"
            f"Severidade: {self.severidade}"
        )
