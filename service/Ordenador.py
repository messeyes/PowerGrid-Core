
class Ordenador:

    #ordena uma leitura por vez
    @staticmethod
    def insertion_sort(leituras, chave):
        for i in range(1, len(leituras)):
            key = leituras[i]
            j = i - 1
            while j >= 0 and chave(key) < chave(leituras[j]):
                leituras[j + 1] = leituras[j]
                j -= 1
            leituras[j + 1] = key

        return leituras


    #busca o menor valor
    @staticmethod
    def selection_sort(leituras, chave):
        n = len(leituras)

        for i in range(n - 1):
            index = i

            for j in range(i + 1, n):
                if chave(leituras[j]) < chave(leituras[index]):
                    index = j

            if index != i:
                leituras[i], leituras[index] = leituras[index], leituras[i]

        return leituras

    #divide as leituras em listas menores até que cada sublista tenha um único elemento, e então combina elas ordenando
    @staticmethod
    def merge_sort(leituras, chave):
       if len(leituras) > 1:
           mid = len(leituras) // 2

           esquerda = leituras[:mid]
           direita = leituras[mid:]

           Ordenador.merge_sort(esquerda, chave)
           Ordenador.merge_sort(direita, chave)

           i = j = k = 0

           while i < len(esquerda) and j < len(direita):
               if chave(esquerda[i]) < chave(direita[j]):
                   leituras[k] = esquerda[i]
                   i += 1

               else:
                   leituras[k] = direita[j]
                   j += 1

               k += 1

           while i < len(esquerda):
                leituras[k] = esquerda[i]
                i += 1
                k += 1

           while j < len(direita):
               leituras[k] = direita[j]
               j += 1
               k += 1

       return leituras


    #parecido com o merge, ele acha o meio, divide e só depois vai ordenar
    @staticmethod
    def quick_sort(leituras, chave):
        if len(leituras) <= 1:
            return leituras
        pivo = leituras[len(leituras) // 2]

        menores = [
            x for x in leituras
            if chave(x) < chave(pivo)]
        iguais = [
            x for x in leituras
            if chave(x) == chave(pivo)]

        maiores = [
            x for x in leituras
            if chave(x) > chave(pivo)]

        return (
            Ordenador.quick_sort(menores, chave) +
            iguais +
            Ordenador.quick_sort(maiores, chave)
        )