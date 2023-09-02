# Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o Valor do desconto e o preço a pagar.

valor_mercadoria = float(input("Digite o valor da mercadoria: "))
desconto = int(input("Digite a porcentagem de desconto caso o valor seja pago a vista: "))
valor_a_vista = valor_mercadoria - (valor_mercadoria * desconto / 100 )  
print(f"Você obteve um desconto de {desconto}% e irá pagar um valor à vista de {valor_a_vista}")
