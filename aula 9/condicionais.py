"""
Condições if, elif e else
operadores relacionais ==, >, >=, <, <=, !=
operadores logicos and, or, not(inverte ou pode verificar se esta vazio), in, not in
"""
if True:
    print("verdadeiro")
nome = 'Luan'
letra = input("Digite uma letra: ")
if letra in nome:
    print(f'existe a letra "{letra}" em {nome}')
else:
    print("Não tem")
