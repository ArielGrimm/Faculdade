#Entrada
print("Digite a quantidadede ração consumida por refeição")
quantconsum = int(input())
print("Digite o número de refeições por dia")
refdia = int(input())
#Processamento
totaldia = quantconsum * refdia
totalmes = totaldia * 30
#Saída
print("A quantidade total de ração consumida por mês é de", totalmes)