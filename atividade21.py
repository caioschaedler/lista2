###
# atividade 21
# Aluno: caio schaedler
# data 20/04/2024
###

ano = int(input("digite um ano:"))

if ano % 4 == 0 or ano % 400 == 0:
    print(f"{ano} eh um ano bissexto")
else:
    print(f"{ano} nao eh um ano bissexto")