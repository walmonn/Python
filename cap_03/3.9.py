# Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuario. Calcule o Total em Segundos.

dias = int(input("Digite a quantidade de dias: "))
horas = int(input("Digite as horas: "))
minutos = int(input("Digite os minutos: "))
segundos = int(input("Digite os Segundos: "))

total_dias = dias * 24 * 3600
total_horas = horas * 3600
total_minutos = minutos * 60
total_segundos = segundos

total = total_dias + total_horas + total_minutos + total_segundos

print(f"O Total digitado é {total}")
