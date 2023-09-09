# Lê dois valores e imprime qual é o maior

a = int(input("Primeiro Valor :"))
b = int(input("Segundo Valor :"))

if a > b:
    print("O Primeiro Valor é maior!")
if b > a:
    print("O Segundo Valor é maior!")

# Se os valores forem iguais, nada será impresso.
# Isso acontece porque a > b e b > a são falsas quando a = b.
# Assim, nem o print de 2, nem o print de 3 serão executados, logo nada será impresso.
