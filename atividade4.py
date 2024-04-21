###
# atividade 4
# Aluno: caio schaedler
# data 08/04/2024
###
import math

num = float(input("digite o numero: "))
if (num > 0):
    raiz = math.sqrt(num)
    qua = (num * num)
    print(f"o numero ao quadrado eh: {qua:.2f}")
    print(f"a raiz quadrada desse numero eh: {raiz:.2f}")
elif num < 0:
    print("esse numero eh invalido")