class No:
    def __init__(self, nome):
        self.nome = nome
        self.filhos = []

    def adicionar(self, filho):
        self.filhos.append(filho)

    def exibir(self, nivel=0):
        print("  " * nivel + "└── " + self.nome)
        for filho in self.filhos:
            filho.exibir(nivel + 1)


cos = No("Centro de Operações (COS)")

norte = No("Subestação Norte")
sul = No("Subestação Sul")

cos.adicionar(norte)
cos.adicionar(sul)

transformador = No("Transformador")
disjuntor = No("Disjuntor")

norte.adicionar(transformador)
sul.adicionar(disjuntor)

transformador.adicionar(No("Sensor de Temperatura"))
transformador.adicionar(No("Sensor de Tensão"))
disjuntor.adicionar(No("Sensor de Corrente"))
disjuntor.adicionar(No("Logs da Rede"))

cos.exibir()