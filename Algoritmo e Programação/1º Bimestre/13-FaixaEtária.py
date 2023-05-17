print("Digite sua idade:")
idade = int(input())
if idade <= 20:
    print("Jovem")
else:
    if idade >20 and idade <70:
        print("Adulto")
    else:
        print("Idoso")