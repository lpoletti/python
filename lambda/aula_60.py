a = lambda x, y: x*y
print(a(2,2))

lista = [
    ['P1',13],
    ['P2',26],
    ['P1',15],
    ['P3',39],
]
lista.sort(key=lambda item:item[1])
print(lista)

