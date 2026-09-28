excelente = 0
ruim = 0

for entrevistado in range(1, 11):
    print("\nEntrevistado", entrevistado)

    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))

    print("Opções de atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    opiniao = int(input("Digite sua opinião: "))

    if opiniao == 1:
        excelente += 1
    elif opiniao == 3:
        ruim += 1

print("\n--- RESULTADO DA PESQUISA ---")
print("Quantidade de respostas EXCELENTE:", excelente)
print("Quantidade de respostas RUIM:", ruim)