# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais
n1 = int(input('Escreva um número inteiro: '))
n2 = int(input('Escreva outro número inteiro: '))
if n1 > n2:
    print('O PRIMEIRO ({}) é maior do que o SEGUNDO ({}).'.format(n1,n2))
elif n1 < n2:
    print('O SEGUNDO ({}) é maior do que o PRIMEIRO ({}).'.format(n2,n1))
elif n1 == n2:
    print('Não existe valor maior ou menor, os dois números são iguais!')
