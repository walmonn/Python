# Escreva um expressão para determinar se uma pessoa deve ou não paga imposto. Considere que pagam imposto pessoas cujo salário é maior que R$1200,00.

sal = float(input("Digite seu Salário: "))

if sal >= 1200:
    print("Você deve pagar Imposto")
else:
    print("Você é isento de imposto")     
