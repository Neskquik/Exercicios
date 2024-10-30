def busca_binaria(lista, alvo):
    esquerda, direita = 0, len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1

lista = [1, 2, 3, 9, 33]
alvo = 5
resultado = busca_binaria(lista, alvo)
print(f"Índice do elemento {alvo}: {resultado}")
