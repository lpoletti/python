# add(adciona), update (atualiza), clear, discard
# union | (une)
# intersection & (todos os elementos presentes nos dois sets)
# difference - (elementos apenas no set da esquerda)
# symmetric_difference ^ (Elementos que estão nos dois sets mas não em ambos)
# set normalmente utilizado para remover elementos duplicados
# elementos a cada execução aparecem numa ordem aleatória

# forma utilizada na pratica
l1 = ['Luan', 'Pedro', 'João']
l2 = ['João', 'Luan', 'Pedro', 'Luan', 'Pedro']

#importante esse exemplo
l1 = set(l1)
l2 = set(l2)

print(l1 == l2)

#exemplos
s1 = {1,2,3,4,5}
s2 = {5,6,7,8,9,0}
s3 = s1 | s2

print(s3)

s4 = s1 & s2

print(s4)

s5 = s1 - s2

print(s5)

s6 = s1 ^ s2
print(s6)