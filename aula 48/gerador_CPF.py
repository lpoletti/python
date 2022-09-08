"""
CPF = 168.995.350-09
------------------------------------------------
1 * 10 = 10           #    1 * 11 = 11 <-
6 * 9  = 54           #    6 * 10 = 60
8 * 8  = 64           #    8 *  9 = 72
9 * 7  = 63           #    9 *  8 = 72
9 * 6  = 54           #    9 *  7 = 63
5 * 5  = 25           #    5 *  6 = 30
3 * 4  = 12           #    3 *  5 = 15
5 * 3  = 15           #    5 *  4 = 20
0 * 2  = 0            #    0 *  3 = 0
                      # -> 0 *  2 = 0
         297          #             343
11 - (297 % 11) = 11  #     11 - (343 % 11) = 9
11 > 9 = 0            #
Digito 1 = 0          #   Digito 2 = 9
"""
from random import randint


numero = str(randint(100000000,999999999))

#cpf = '00904243010'
novo_cpf = numero
iterador_dez = 10
iterador_onze = 11
soma = 0
dig_1 = 0
dig_2 = 0

## Calculo primeiro dígito CPF
for n in novo_cpf:
    soma += int(n)*iterador_dez
    iterador_dez -= 1
    if iterador_dez < 2:
        break
if (11-(soma%11)) > 9:
    dig_1 = 0
    soma = 0
else:
    dig_1 = 11-(soma%11)
    soma = 0

novo_cpf += str(dig_1)

## Calculo último dígito CPF
for n2 in novo_cpf:
    soma += int(n2)*iterador_onze
    iterador_onze -= 1
    if iterador_onze < 2:
        break

if (11-(soma%11)) > 9:
    dig_2 = 0
else:
    dig_2 = 11-(soma%11)

novo_cpf += str(dig_2)
print(204%11)
print('Novo CPF: ',novo_cpf)
print('Numero: ',numero)