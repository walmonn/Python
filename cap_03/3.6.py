# Escreva uma expressão que será utilizada para decidir se um aluno foi ou não aprovado. Para ser aprovado, todas as médias do aluno devem ser maiores que 7. Considere que o aluno cursa apenas três matérias, e que a nota de cada uma está armazenada nas seguintes variáveis: matéria1, matéria2 e matéria3.

materia1 = float(input("Digite a nota da Matéria 1: "))
materia2 = float(input("Digite a nota da Matéria 2: "))
materia3 = float(input("Digite a nota da Matéria 3: "))

media = (materia1 + materia2 + materia3) / 3

if media >= 7:
    print("O Aluno foi aprovado com média {:.2f}".format(media))
else:
    print("O Aluno teve uma média {:.2f} abaixo de 7.0 e não foi aprovado".format(media))
