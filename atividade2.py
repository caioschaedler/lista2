import math

numf = float(input("digite um numero:"))
if numf >= 0:
    raiz = math.sqrt (numf)
    print(f"a raiz do seu numero eh: {raiz:.2f}")
elif (numf < 0):
    print("esse numero eh invalido")