print("Digite o valor da prestacao em atraso")
valor = float(input())
print("Digite o valor da multa")
taxa = float(input())
print("Digite o numero de dias")
tempoemdias = int(input())
prestacao = valor + (valor * (taxa/ 100) * tempoemdias)
print("O valor da prestacao e R$", prestacao)