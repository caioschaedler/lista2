###
# atividade 9
# Aluno: caio schaedler
# data 15/04/2024
###

salario = float(input("digite o salario: "))
prestação = float(input("digite o valor da prestação: "))
if prestação > (salario * 0.20):
    print("emprestimo nao concedido")
else:
    print("emprestimo concedido")