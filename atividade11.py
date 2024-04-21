###
# atividade 11
# Aluno: caio schaedler
# data 15/04/2024
###

import math

numero = int(input("digite um numero inteiro: "))

if numero <= 0:
    print("numero invalido")
else:
    resultado = math.log(numero)
    print("o logaritimo de ", numero, "eh", resultado)