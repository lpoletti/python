
d1 = {
    'chave1' : 'Valor da chave',
    123 : 'outro valor',
    (1,2,3) : 'tupla'
}

d1['nova_chave'] = 'Novo valor da chave'
print('chave1' in d1)
print('tupla'in d1.values())
print('_________________________________________________')
for v in d1.values():
    print(v)
print('_________________________________________________')
for k in d1:
    print(k)
print('_________________________________________________')
for y in d1.items():
    print(y[0], y[1])

print('_________________________________________________')
for x, z in d1.items():
    print(x, z)
print('_________________________________________________')
print('_________________________________________________')
clientes = {
    'cliente1' : {
        'nome' : 'Luan',
        'sobrenome' : 'Poletti'
    },
    'cliente2' : {
        'nome' : 'Bruna',
        'sobrenome' : 'Bossler'
    },
    'cliente3' : {
        'nome' : 'Julia',
        'sobrenome' : 'Poletti'
    }
}

for k, v in clientes.items():
    print(k,v)
    for k1, v1 in v.items():
        print(f'\t{k1} = {v1}')