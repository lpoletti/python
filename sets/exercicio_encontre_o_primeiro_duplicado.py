"""
-> É uma lista de listas de números inteiros
-> As listas internas tem o tamanho de 10 elementos
-> As listas internas contém números entre 1 a 10 e eles podem ser duplicados

Exercício

-> Crie uma função que encontra o primeiro duplicado considerando o segundo
    número como a duplicação. Retorne a duplicação considerada.
        Requisitos:
            A ordem do número duplicado é considerada a partir da segunda
            ocorrência do número, ou seja, o número duplicado em si.
            Exemplo:
                [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
                [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)

            Se não encontrar duplicados na lista, retorne -1
"""
lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

"""
Primeiro tentativa de enncontrar o primeiro duplicado
"""
def func(lista_de_listas):
    arr = []
    rpt = []
    for v in lista_de_listas:
        if list == type(v):
            for r in v:
                try:
                    arr.index(r)
                    rpt.append(r)
                    break
                except:
                    if len(arr) == 9:
                        rpt.append(-1)
                    else:
                        arr.append(r)
            arr.clear()
    return rpt

print("Primeiro tentativa de enncontrar o primeiro duplicado \n",func(lista_de_listas_de_inteiros))

"""
Segudno jeito de enncontrar o primeiro duplicado otimizado
"""
def func2(lista_simples):
    numeros_checados = set()
    primeiro_duplicado = -1

    for num in lista_simples:
        if num in numeros_checados:
            primeiro_duplicado = num
            break
        numeros_checados.add(num)
    
    return primeiro_duplicado


print("Segudno jeito de enncontrar o primeiro duplicado otimizado")
for res in lista_de_listas_de_inteiros:
    print(func2(res))