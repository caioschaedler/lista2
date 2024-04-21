###
# atividade 18
# Aluno: caio schaedler
# data 20/04/2024
###

numero = int(input("digite um numero inteiro: "))
if numero % 3 == 0 and numero % 5 == 0:
    print("o numero é divisivel por 3 e por 5 ")
elif numero % 3 == 0:
    print("o numero e divisivel por 3, mas nao por 5")
elif numero % 5 == 0:
    print("o numero é divisivel por 5, mas nao por 3")
else:
    print("o numero nao e divisivel nem por 3 nem por 5 ")
    