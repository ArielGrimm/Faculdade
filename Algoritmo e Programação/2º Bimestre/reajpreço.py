print("Digite a venda média mensal do produto")
vmm = float(input())
print("Digite o preço atual do produto")
precoatual = float(input())
if vmm < 500 and precoatual <30:
    valreajuste = precoatual + ((precoatual * 12) /100)
else:
    if vmm >= 500 and vmm < 1600 and precoatual >= 30 and precoatual < 80:
        valreajuste = precoatual + ((precoatual * 15) /100)
    else:
        if vmm >= 1600 and precoatual >= 80:
            valreajuste = precoatual - ((precoatual * 25) /100)   
        else:
            print("O produto não terá reasjute")
print("O valor do produto com reajuste é R$", valreajuste)