"""
For in em python
iterando strings com for
Função range(start=0, stop, step=1)
"""

texto='Python'
nova = ''
#Continue - ele pula pra próxima iteração
#Break - cai fora do laço
for letra in texto:
    if letra == 't':
        nova += 'T'
    elif letra == 'h':
        nova += 'H'
    else:
        nova += letra

print(nova)