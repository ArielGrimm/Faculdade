print("Digite o seu nome")
nome = input()
print("Digite o salário base")
salbase = float(input())
print("Digite o tempo de serviço")
tempo = float(input())
imposto = 0
if salbase > 200 and salbase <= 450:
    imposto = (salbase * 3) / 100
else:
    if salbase > 450 and salbase < 700:
        imposto = (salbase * 8) / 100
    else:
        if salbase == 700:
            imposto = (salbase * 10) / 100
        else:
            if salbase > 700:
                imposto = (salbase * 12) / 100
if salbase > 500 and tempo <= 3:
    grat = ((salbase * 2) / 100) + 50
else:
    if salbase > 500 and tempo > 3:
        grat = ((salbase * 3) / 100) + 60
    else:
        if salbase <= 500 and tempo <= 3:
           grat = ((salbase * 5) / 100) + 23
        else:
            if salbase <= 500 and tempo > 3 and tempo < 6:
                grat = ((salbase * 6) / 100) + 35
            else:
                if salbase <= 500 and tempo >= 6:
                    grat = ((salbase * 10) / 100) + 33
if tempo <= 10:
    aux = (salbase * 4) / 100
else:
    if tempo > 10:
        aux = (salbase * 6) / 100
salliq = salbase + grat  + aux - imposto
print("O valor do salario liquido do", nome, "é R$", salliq)