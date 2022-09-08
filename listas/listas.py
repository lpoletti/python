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