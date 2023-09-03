#Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, e calcule quantos dias de vida um fumante perderá. Exiba o total em dias.

cigarros_por_dia = int(input("Quantos cigarros você fuma por dia: "))
anos_fumando = float(input("Por quantos anos você fumou: "))

reducao_em_minutos = anos_fumando * 365 * cigarros_por_dia * 10
reducao_em_dias = reducao_em_minutos / (24 * 60)

print(f"Você terá uma redução no seu tempo de vida de {reducao_em_dias:.0f} dias")
