###
# atividade 15
# Aluno: caio schaedler
# data 20/04/2024
###

opt = int(input("digite um numero de 1 a 12: "))

match opt:
    case 1:
        print("janeiro")
    case 2:
        print("fevereiro")
    case 3:
        print("março")
    case 4:
        print("abril")
    case 5:
        print("maio")
    case 6:
        print("junho")
    case 7: 
        print("julho")
    case 8:
        print("agosto")
    case 9:
        print("setembro")
    case 10:
        print("outubro")
    case 11:
        print("novembro")
    case 12:
        print("dezembro")
    case _:
        print("esse numero eh invalido")