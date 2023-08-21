# Escreva um programa que calcule a soma de três variáveis e imprima o resultado na tela.

n1 = float(input('Digite o Primeiro Numero: '))
n2 = float(input('Digite o Segundo Numero: '))
n3 = float(input('Digite o Terceiro Numero: '))

soma = n1 + n2 + n3

print('O resultado da soma de {:.2f} + {:.2f} + {:.2f} é igual a {:.2f}'.format(n1, n2, n3, soma))
