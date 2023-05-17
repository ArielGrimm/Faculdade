#Entrada
print("Digite a quantidade livre do HD em megabytes")
quantlivre = float(input())
#Processamento
perclivre = (quantlivre * 100) / 40000
#Saída
print("O percentual do espaço livre do HD é de %.2f" %perclivre, "%")