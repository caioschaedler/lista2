###
# atividade 6
# Aluno: caio schaedler
# data 08/04/2024
###

num1 = float(input("digite o primeiro numero: "))
num2 = float(input("digite o segundo numero: "))
dif = num1-num2
print(f"a diferença entre os dois eh:{dif:.2f}")
if num1 > num2:
    print(f"{num1} eh maior")
else:
    print(f"{num2} eh maior")