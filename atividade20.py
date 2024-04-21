###
# atividade 20
# Aluno: caio schaedler
# data 20/04/2024
###

idade = int(input("Digite a idade do trabalhador: "))
tempo_de_servico = int(input("Digite o tempo de serviço (em anos) do trabalhador: "))

if idade >= 65 or tempo_de_servico >= 30 or (idade >= 60 and tempo_de_servico >= 25):
    print("O trabalhador pode se aposentar.")
else:
    print("O trabalhador ainda não pode se aposentar.")
