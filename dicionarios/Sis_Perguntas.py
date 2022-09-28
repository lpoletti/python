
print()
respostas_certas = 0

perguntas = {
    'Pergunta 1': {
        'pergunta' : 'Quanto é 2+2?',
        'respostas' : {
            'a' : '1',
            'b' : '4',
            'c' : '5'
        },
        'resposta_certa' : 'b',
    },
    'Pergunta 2': {
        'pergunta' : 'Quanto é 3*2?',
        'respostas' : {'a' : '6','b' : '7','c' : '5'},
        'resposta_certa' : 'a',
    },
}

for pk, pv in perguntas.items():
    print(f'{pk} : {pv["pergunta"]}')

    print("Respostas: ")
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}] : {rv}')

    resposta = input("Sua resposta é: ")

    if resposta == pv['resposta_certa']:
        print("EEEHHH!!! VOCÊ ACERTOU!!!")
        respostas_certas += 1
    else:
        print("VIXI VOCÊ ERROU!!!")

    print()
porcentagem = respostas_certas / len(perguntas) * 100
print(f'Você acertou {porcentagem}% das questões')
