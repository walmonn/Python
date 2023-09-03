# Escreva um programa que converta uma temperatura digitada e °C em °F. A fórmula para essa conversão é:   F = ((9 X C) / 5) + 32.

temp_C = float(input("Digite a Temperatura em °C que deseja converter para °F: "))
temp_F = ((temp_C * 9) / 5) + 32
print(f"A Temperatura °C{temp_C:.0f} convertida é °F{temp_F:.0f}")
