# 48: Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de 3 e que se encontram no intervalo de 1 até 500.
import math
lista_numero = []
for numero in range (0,500,3):
    if numero % 2 != 0:
        lista_numero.append(numero)
print('Lista dos números ímpares múltiplos de 3 (de 0 a 500):')
print(lista_numero)
print('Soma entre todos os números: ')
print(math.fsum(lista_numero))


"""somatorio = 0
for numero in range (0,500,3):
    if numero % 2 != 0:
        somatorio += numero
print(somatorio)"""

