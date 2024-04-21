###
# atividade 19
# Aluno: caio schaedler
# data 20/04/2024
###

a = float(input("Digite o comprimento do primeiro lado do triângulo: "))
b = float(input("Digite o comprimento do segundo lado do triângulo: "))
c = float(input("Digite o comprimento do terceiro lado do triângulo: "))

if a >= b + c or b >= a + c or c >= a + b:
    print("Não é possível formar um triângulo com os lados fornecidos.")
elif a == b == c:
    print("O triângulo é equilátero.")
elif a == b or a == c or b == c:
    print("O triângulo é isósceles.")
else:
    print("O triângulo é escaleno.")


