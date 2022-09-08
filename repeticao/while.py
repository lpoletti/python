"""
utilizado para realizar uma ação enquanto uma condição
for verdadeira
"""

x=0

# while x<10:
#     # if x == 3:
#     #     x += 1
#     #     continue ## NESSE CASO ELE PULA TODA VEZ Q X FOR 3
#     #     break ## PULA FORA DO WHILE
#     print(x)
#     x+=1

##############################################

# while x<10:
#     y=0
#     while y<5:
#        print(f'({x},{y})')
#        y+=1
#     x+=1

##############################################
#Calculadora

# while True:
#     print()
#     num_1 = input("Digite um numero? ")
#     num_2 = input("Digite outro? ")
#     operador = input("Digite um operador? ")
#     sair = input("Quer sair? [s]im ou [n]ão")
#
#     if sair == 's':
#         break
#
#     num_1 = int(num_1)
#     num_2 = int(num_2)
#
#     if operador == '+':
#         print(num_1+num_2)
#     elif operador == '-':
#         print(num_1-num_2)
#     elif operador == '*':
#         print(num_1*num_2)
#     elif operador == '/':
#         print(num_1/num_2)
#     else:
#         print("Operador inválido!")

##############################################
#contador e acumulador
# contador = 1
# acumulador = 1
#
# while contador<10:
#     print(contador,acumulador)
#     acumulador = acumulador + contador
#     contador +=1
# else:
#     print('cheguei no else')
#############################################
#indices

frase = 'o rato roeu a roupa do rei de roma'
tamanho_da_frase = len(frase)
contador = 0
nova_string = ''

while contador < tamanho_da_frase:
    letra = frase[contador]
    if letra == 'r':
        nova_string += 'R'
    else:
        nova_string+= letra
    contador+=1

print(nova_string)






