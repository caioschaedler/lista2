###
# atividade 23
# Aluno: caio schaedler
# data 20/04/2024
###

idade = int(input("Digite a idade do atleta: "))

if idade >= 5 and idade <= 7:
    print("Categoria: Infantil A")
elif idade >= 8 and idade <= 10:
    print("Categoria: Infantil B")
elif idade >= 11 and idade <= 13:
    print("Categoria: Juvenil A")
elif idade >= 14 and idade <= 17:
    print("Categoria: Juvenil B")
else:
    print("Categoria: Sênior")