class Buscador:

    @staticmethod
    def busca_binaria(leituras, sensor_id):
        #devolve todas as leituras do sensor / exige ordem por sensor_id

        #retorna uma lista vazia quando não tem nada
        
        inicio = 0
        fim = len(leituras)

        # acha o início do intervalo do sensor ppela busca binária
        while inicio < fim:
            meio = (inicio + fim) // 2
            if leituras[meio].sensor_id < sensor_id:
                inicio = meio + 1
            else:
                fim = meio

        primeiro = inicio
        fim = len(leituras)

        # acha o fim do intervalo, até os ids repetidos
        while inicio < fim:
            meio = (inicio + fim) // 2
            if leituras[meio].sensor_id <= sensor_id:
                inicio = meio + 1
            else:
                fim = meio

        return leituras[primeiro:inicio]
