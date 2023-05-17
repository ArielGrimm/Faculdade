print("Digite a altura")
altura = float(input())
print("Digite o sexo M/F")
sexo = input()
if sexo == 'm' or sexo == 'M':
    peso = (72.7 * altura) - 58
else:
    if sexo == 'f' or sexo == 'F':
        peso = (62.1 * altura) - 44.7
    else:
        print("Sexo Inválido")    
print("O peso ideal e ", peso)