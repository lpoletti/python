"""
Manipulando strings - aula 6
string indices
fatiamento de strings[inicio:fim:passo]
funções built-in len, abs, type, print, etc...

https://docs.python.org/3/library/stdtypes.html (tipos de built-in)
https://docs.python.org/3/library/functions.html (funções built-in)
"""

# positivos  [012345678]
texto      = 'Python s2'
# negativos -[987654321]

url = 'www.google.com.br/'
print(url[:-1])#dois pontos para excluir o ultimo caracter nesse exemplo

nova_string = texto[2:6]
print(nova_string)
nova_string = texto[:6]
print(nova_string)
nova_string = texto[7:]
print(nova_string)
nova_string = texto[-9:-3]
print(nova_string)
nova_string = texto[0:6:2]
print(nova_string)

for letra in texto:
    print(letra)