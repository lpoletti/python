"""
funções def em python - *args **kwargs
"""

def func(*args, **kwargs):
    print(args)

    nome = kwargs.get('nome') # utiliza-se o get no caso de eu não saber se a chave existe de verdade
    if nome is not None:
        print(nome)


lista = [1,2,3,4,5]
lista2 = [10,20,30,40]
func(*lista, *lista2, apelido="Luan", sobrenome='Poletti')



