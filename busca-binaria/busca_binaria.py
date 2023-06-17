"""
O algoritmo de busca binária pega uma lista ordenada e retorna a posição 
do item que você deseja buscar.

Serve para quando você possui uma lista muito grande e deseja saber onde se encontra 
o item que você deseja desse array.
"""

import sys
from brand_list_makeup import brands_makeup

def busca_binaria_makeup(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo < alto:
        meio = int((baixo + alto)/2)
        chute = lista[meio]

        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1 

    return None

if __name__ == "__main__":
    marca_makeup = sys.argv[1]

    print(busca_binaria_makeup(brands_makeup, marca_makeup))