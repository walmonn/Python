# Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distancia a percorrer e a velocidade media esperada para a viagem.

distancia = float(input("Digite a distância percorrida em Km: "))
velocidade = float(input("Digite a velocidade média em Km/h: "))
tempo  = distancia / velocidade
tempo_s = int(tempo * 3600)
horas = int(tempo_s / 3600)
tempo_s = int(tempo_s % 3600)
minutos = int(tempo_s / 60)
segundos = int(tempo_s % 60)
print(f"O Tempo total de Viagem de uma distancia percorrida de {distancia:.0f}Km a uma velocidade de {velocidade:.0f}Km/h é de {horas}horas , {minutos}minutos e {segundos}segundos.")
