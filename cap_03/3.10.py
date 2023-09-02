# Faça um Programa que calcule o aumento de um salário. Ele deve solicitar o valor do Salário e a porcentagem do aumento. Exiba o valor do aumento e o novo salário.

sal = float(input("Digite seu salário atual: "))
p_aumento = float(input("Digite qual a porcentagem de aumento: "))
aumento = (sal * p_aumento) / 100
novo_salario = sal + aumento
print(f"Você recebeu um aumento de {p_aumento:.0f}% no seu atual salário de R${sal:.2f} sendo assim seu novo salário será de R${novo_salario:.2f}")