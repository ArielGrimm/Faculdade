#Entrada
print("Digite o valor do Boleto")
valboleto = float(input())
print("Digite o percentual da multa")
percmulta = float(input())
#Processamento
valmulta = (percmulta * valboleto) / 100
totboleto = valboleto + valmulta
#Saída
print("O valor do boleto com atraso é de R$ %.2f" %totboleto)