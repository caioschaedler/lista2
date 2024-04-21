###
# atividade 13
# Aluno: caio schaedler
# data 20/04/2024
###

tl = float(input("digite a nota do trabalho do laboratorio: "))
avs = float(input("digite a nota da avaliacao semestral: "))
ef = float(input("digite a nota do exame final "))
nf = (tl + avs + ef) / 2
if nf >= 3.0 and nf <= 5.0:
    print("o aluno esta aprovado")
elif nf >= 0.0 and nf <= 2.9:
    print("o aluno esta reprovado")
else:
    print("resultado invalido")