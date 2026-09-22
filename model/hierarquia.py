class NoSensor:
    def __init__(self, leitura):
        self.sensor_id = leitura.sensor_id
        self.leituras = [leitura]
        self.esquerda = None
        self.direita = None


def inserir(raiz, leitura):
    if raiz is None:
        return NoSensor(leitura)

    if leitura.sensor_id < raiz.sensor_id:
        raiz.esquerda = inserir(raiz.esquerda, leitura)
    elif leitura.sensor_id > raiz.sensor_id:
        raiz.direita = inserir(raiz.direita, leitura)
    else:
        raiz.leituras.append(leitura)

    return raiz


def buscar(raiz, sensor_id):
    if raiz is None:
        return None
    if sensor_id == raiz.sensor_id:
        return raiz
    if sensor_id < raiz.sensor_id:
        return buscar(raiz.esquerda, sensor_id)
    return buscar(raiz.direita, sensor_id)


def em_ordem(raiz, resultado=None):
    if resultado is None:
        resultado = []
    if raiz:
        em_ordem(raiz.esquerda, resultado)
        resultado.append(raiz)
        em_ordem(raiz.direita, resultado)
    return resultado


def pre_ordem(raiz, resultado=None):
    if resultado is None:
        resultado = []
    if raiz:
        resultado.append(raiz)
        pre_ordem(raiz.esquerda, resultado)
        pre_ordem(raiz.direita, resultado)
    return resultado


def pos_ordem(raiz, resultado=None):
    if resultado is None:
        resultado = []
    if raiz:
        pos_ordem(raiz.esquerda, resultado)
        pos_ordem(raiz.direita, resultado)
        resultado.append(raiz)
    return resultado


def altura(raiz):
    if raiz is None:
        return 0
    return 1 + max(altura(raiz.esquerda), altura(raiz.direita))


def esta_balanceada(raiz):
    if raiz is None:
        return True

    fb = altura(raiz.esquerda) - altura(raiz.direita)

    if abs(fb) > 1:
        return False

    return esta_balanceada(raiz.esquerda) and esta_balanceada(raiz.direita)