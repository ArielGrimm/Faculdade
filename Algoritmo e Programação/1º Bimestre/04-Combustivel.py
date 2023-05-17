#Entrada
print("Digite a distância percorrida em KM")
distancia = float(input())
#Processamento
qtdgasolina = distancia / 13
reembolso = qtdgasolina * 2.20
#Saída
print("O valor do reembolso é de R$%.2f" %reembolso)