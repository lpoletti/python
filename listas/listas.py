"""
listas em python
fatiamento
append, insert, pop(o ultimo elemento é excluido), del, clear, extend, +
min, max
range
"""

# lista = ['a','b','c','d','e']
# print(lista)
# lista.insert(0,'banana')
# print(lista)
# del(lista[2:4])
# print(lista)
# lista = range(1,10)
# print(lista)
# lista = list(range(1,10))
# print(lista)
# lista = ["String", True, 10, -20.5]
#
# for elem in lista:
#     print(f'o tipo de elem é {type(elem)} e o seu valor é {elem}')

#########
#Jogo da forca
palavra = 'chocolate'
digitadas=[]
while True:
    letra = input("Digite uma letra? ")

    if len(letra)>1:
        print("Letra inválida!")
        continue

    digitadas.append(letra)

    if letra in palavra:
        print('Uhul acertou')
    else:
        print("Quem sabe na próxima :(")
        digitadas.pop()

    p_temp=''
    for l in palavra:
        if l in digitadas:
            p_temp += l
        else:
            p_temp+='*'

    print(p_temp)
    if p_temp == palavra:
        print("Parabéns vc descobriu a palavra!")
        break
"""AULA 67 - list comprehension"""
l1 = [1,2,3,4,5,6,7,8,9]
ex1 = [variavel for variavel in l1]

ex2 = [v*2 for v in l1]
ex3 = [(v, v2) for v in l1 for v2 in range(3)]

l2 = ['Luiz', 'Mauro', "Maria", 'Luan']
ex4 = [v.replace('a','@').upper() for v in l2]

tupla = (
    ('chave','valor'),
    ('chave2', 'valor2'),
    )
ex5 = [(x,y) for x,y in tupla]
ex5 = dict(ex5)

print(ex5)