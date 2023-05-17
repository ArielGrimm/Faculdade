print("Digite o preço do produto")
valpreco = float(input())
if valpreco < 50:
    valpreco = valpreco + ((valpreco * 5) / 100)
else:
    if valpreco >= 50 and valpreco <=100:
        valpreco = valpreco + ((valpreco * 10) / 100)
    else: 
        valpreco = valpreco + ((valpreco * 15) / 100)
print("O valor do novo preco do produto é", valpreco)
if valpreco <= 80:
    print("Barato")
else:
    if valpreco > 80 and valpreco <= 120:
        print("Normal")
    else:
        if valpreco > 120 and valpreco <= 200:
            print("Caro")
        else:
            print("Muito Caro")