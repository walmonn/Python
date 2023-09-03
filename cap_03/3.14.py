# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.

qtd_dias = float(input("Digite a quantidade de dias que você irá alugar o carro: "))
km_rodada = float(input("Digite a quantidade de KM rodados durante o tempo alugado: "))
preco_por_dia = 60
preco_por_km = 0.15
preco_a_pagar = (qtd_dias * 60) + (km_rodada * 0.15) 

print(f"Você usou o carro durante {qtd_dias:.0f} dias e rodou KM{km_rodada:.0f} e irá pagar um total de R${preco_a_pagar:.2f} pelo aluguel do carro")
