###
# atividade 14
# Aluno: caio schaedler
# data 20/04/2024
###

opt = int(input("digite um numero de 1 a 7: "))

match opt:
    case 1:
        print("domingo")
    case 2:
        print("segunda-feira")
    case 3:
        print("terça-feira")
    case 4:
        print("quarta-feira")
    case 5:
        print("quinta-feira")
    case 6:
        print("sexta-feira")
    case 7: 
        print("sabado")
    case _:
        print("esse numero eh invalido")