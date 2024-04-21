###
# atividade 3
# Aluno: caio schaedler
# data 08/04/2024
###
import math

num = float(input("digite o numero: "))
if num > 0 :
    raiz = math.sqrt (num)
    print(f"a raiz do seu numero eh: {raiz:.2f}")
elif (num < 0):
    quadrado = (num * num)
    print(f"o quadrado do seu numero eh: {quadrado:.2f}")
