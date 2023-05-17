print("Digite um número")
num1 = int(input())
print("Digite outro número")
num2 = int(input())

if num1 == num2:
    print("São iguais")
    media = (num1 + num2) /2
    print("A media é %.2f" %media)
else:
    if num1 > num2:
        print("O número maior é", num1, "e o menor é",num2)
    else:
        print("O número maior é", num2, "e o menor é",num1)
