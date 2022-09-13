def func(funcao, *args, **kwargs):
    return funcao(*args,**kwargs)

def func2():
    return 'texto'

def saudacao(saudacao, nome):
    return f'{saudacao} {nome}'

exec = func(saudacao,nome='Luan',saudacao='Bom dia')
print(exec)