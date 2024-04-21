###
# atividade 17
# Aluno: caio schaedler
# data 20/04/2024
###

num1 = float(input("digite o primeiro numero: "))
num2 = float(input("digite o segundo numero: "))
operador = int(input("se deseja somar digite: 1 \n se deseja diminuir digite: 2 \n se deseja dividir digite: 3 \n se deseja multiplicar digite: 4 \n digite a operaçao desejada: "))

if operador == 1:
    soma = num1 + num2
    print(f"o resultado da soma eh: {soma:.2f}")
elif operador == 2:
    dimi = num1 - num2
    print(f"o resultado da diminuiçao eh: {dimi:.2f}")
elif operador == 3:
    divi = num1 / num2
    print(f"o valor da divisao eh: {divi:.2f}")
elif operador == 4:
    multi = num1 * num2
    print(f"o resultado da multiplicaçao eh: {multi:.2f}")