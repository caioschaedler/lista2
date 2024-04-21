###
# atividade 8
# Aluno: caio schaedler
# data 08/04/2024
###

num1 = float(input("digite o primeiro numero: "))
num2 = float(input("digite o segundo numero: "))
media = (num1 + num2) / 2
if media >= 0.0 and media <= 10.0:
    print(f"a media eh {media:.2f}")
else:
    print("esses numeros sao invalidos")