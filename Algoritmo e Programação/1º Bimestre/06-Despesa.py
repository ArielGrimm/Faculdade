#Entrada
print("Digite o seu salário total")
salario = float(input())
print("Digite o valor da despesa")
valdespesa = float(input())
#Processamento
percentual = (valdespesa / salario) * 100
#Saída
print("O percentual da despesa é de", percentual, "%")