# Exercício 80: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
lista = []
for c in range (0,5):
    num = int(input('Insira um número: '))
    if len(lista) == 0 or num > lista[-1]:
        lista.append(num)
        print(f'Número {num} adicionado na última posição.')
    else:
        for i, valor in enumerate(lista):
            if num < valor:
                lista.insert(i,num)
                print(f'Número {num} adicionado na posição {i}.')
                break # utilizado para reduzir tempo de processamento
print(lista)

