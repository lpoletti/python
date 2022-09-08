"""
Formatando valores modificadores - aula 5

:s - Texto (strings)
:d - inteiros (int)
:f - números de ponto flutuante (float)
:.(número)f - quantidade de casas decimais (float
:(CARACTERE)(> ou < ou ^)(Quantidade)(Tipo - s,d ou f)

> - esquerda
< - direita
^ - centro
"""

num_1 = 1150
print(f'{num_1:0>10.2f}')

nome = 'Luan Poletti'
namo = 'Bruna'
print(len(nome))
print(f'{nome:#^20}')
nome_formatado = '{:@>50}'.format(nome)
print(nome_formatado)
nome_formatado2 = '{0:@^20} {1:#^20}'.format(nome, namo)
print(nome_formatado2)