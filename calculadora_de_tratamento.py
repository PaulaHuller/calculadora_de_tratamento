from time import sleep


def linha():
    print("-="*20)


linha()
print("        ENTENDA O SEU TRATAMENTO  ")
linha()
medicamento = str(input("Qual o medicamento? "))
linha()
apresentacao = int(input("Qual é o tipo:\n[1] Comprimido;\n[2] Gotas;\n[3] Solução ou Xarope;\nDigite o número correspondente da apresentação do seu medicamento(Somente números): "))
linha()
if apresentacao == 1:
    dose = float(input("Quantos comprimidos irá utilizar por vez?(Somente números): "))
    apresentacao = "Comprimidos"
elif apresentacao == 2:
    dose = int(input("Quantas gotas irá utilizar por vez?(Somente números): "))
    apresentacao = "Gotas"
elif apresentacao == 3:
    dose = float(input("Quantos MLs irá utilizar por vez?(Somente números): "))
    apresentacao = "ML"
else:
    print("Por favor, escreva apenas o número da opção selecionada!")
linha()
posologia = int(input("Quantas vezes ao dia?(somente números): "))
linha()
dia = int(input("Quantos dias será o tratamento?(somente números): "))
qtdtotal = dose * posologia * dia
linha()
print("Calculando...")
sleep(2)
print(f"Você irá tomar {medicamento}, {dose} {apresentacao} {posologia} vezes ao dia durante {dia} dias, totalizando {qtdtotal} {apresentacao}")
if apresentacao == "Gotas":
    qtd = qtdtotal / 20
    sleep(2)
    print(f"Considerando que cada ML equivale a 20 gotas, a quantidade de mls necessários será {qtd} mls.")
linha()
