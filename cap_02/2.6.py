# Modifique o Programa 2.2, de forma que ele calcule um aumento de 15% para um salário de R$750,00.

salario = float(input('Digite o seu Salário: '))
aumento = (salario * 15) / 100
salario_real = salario + aumento

print('O Valor do Salário com aumento é de {}'.format(salario_real))
