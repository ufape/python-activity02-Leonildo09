# -*- coding: utf-8 -*-

# YOUR FULL NAME
# UAG00098
# Problem Set 2 - Problem 2
# Description:

"""
Inputs, Processes and Output (IPO)
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Input(s):
Leia três valores de ponto flutuante A, B e C.
Digite o valor A: 
Digite o valor B:
Digite o valor C:

Processes:
Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossível calcular.”, caso haja uma divisão por 0 ou raiz de numero negativo.

Output(s):
Se não houver possibilidade de calcular as raízes, apresente a mensagem "Impossível calcular.". Caso contrário, imprima o resultado das raízes com 3 dígitos após o ponto, com uma mensagem correspondente conforme exemplo abaixo.
Exemplo 1:
R1 = -0.297
R2 = -2.712
"""

import match

def main():
    a = float(input('Digite o valor A: '))
    b = float(input('Digite o valor B: '))
    c = float(input('Digite o valor C: '))

    delta = b**2 - 4*a*c

    if a == 0 or delta < 0:
      print('Impossível Calcular')      
    else:
      R1 = (-b + delta**0.5) / (2*a)
      R2 = (-b - delta**0.5) / (2*a)
      print(f'R1 = {R1:.3f}')
      print(f'R2 = {R2:.3f}')

if __name__ == '__main__':
    main()
