'''Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento.
 Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, 
de15%'''

salario = float(input("Digite seu Salário: "))
pc_aumento = 0.15
if salario > 1250:
    pc_aumento = 0.10
aumento = salario * pc_aumento
novo_salario = salario + aumento
print(f"Seu aumento será de: R$ {aumento:7.2f}")
print(f"Seu novo salario será de: R$ {novo_salario:7.2f}")
