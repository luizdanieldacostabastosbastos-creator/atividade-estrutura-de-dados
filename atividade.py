import random
import sys

sys.setrecursionlimit(10000)


def bubble(v):
    c = t = 0
    for i in range(len(v) - 1):
        trocou = False
        for j in range(len(v) - 1 - i):
            c += 1
            if v[j] > v[j + 1]:
                v[j], v[j + 1] = v[j + 1], v[j]
                t += 1
                trocou = True
        if not trocou:
            break
    return c, t


def insertion(v):
    c = m = 0
    for i in range(1, len(v)):
        x = v[i]
        j = i - 1
        while j >= 0:
            c += 1
            if v[j] > x:
                v[j + 1] = v[j]
                m += 1
                j -= 1
            else:
                break
        v[j + 1] = x
        m += 1
    return c, m


def selection(v):
    c = t = 0
    for i in range(len(v) - 1):
        menor = i
        for j in range(i + 1, len(v)):
            c += 1
            if v[j] < v[menor]:
                menor = j
        if menor != i:
            v[i], v[menor] = v[menor], v[i]
            t += 1
    return c, t


def quick(v):
    c = t = 0

    def ordenar(a, b):
        nonlocal c, t
        if a < b:
            pivo = v[b]
            i = a - 1

            for j in range(a, b):
                c += 1
                if v[j] <= pivo:
                    i += 1
                    if i != j:
                        v[i], v[j] = v[j], v[i]
                        t += 1

            if i + 1 != b:
                v[i + 1], v[b] = v[b], v[i + 1]
                t += 1

            ordenar(a, i)
            ordenar(i + 2, b)

    ordenar(0, len(v) - 1)
    return c, t


algoritmos = [
    ("Bubble", bubble),
    ("Insertion", insertion),
    ("Selection", selection),
    ("Quick", quick)
]


def testar(original):
    for nome, funcao in algoritmos:
        copia = original.copy()
        comparacoes, movimentos = funcao(copia)
        print(nome, "- Comparações:", comparacoes,
              "| Trocas/movimentações:", movimentos)


random.seed(42)

for tamanho in [10, 20, 1000]:
    original = [random.randint(1, 10000) for i in range(tamanho)]
    print("\nTamanho:", tamanho)
    testar(original)


# Desafio adicional
random.seed(99)
vetor = [random.randint(1, 10000) for i in range(1000)]

print("\nDesafio - vetor aleatório")
testar(vetor)

print("\nDesafio - vetor ordenado")
testar(sorted(vetor))

print("\nDesafio - vetor invertido")
testar(sorted(vetor, reverse=True))
