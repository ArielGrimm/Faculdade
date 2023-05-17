print("Digite o primeiro numero")
numA = int(input())
print("Digite o segundo numero")
numB = int(input())
print("Digite o terceiro numero")
numC = int(input())

if numA > numB:
    if numA > numC:
        print("O maior e",numA)
        if numB > numC:
            print("O do meio e", numB)
            print("O menor e", numC)
        else:
            print("O do meio e", numC)
            print("O menor e", numB)            
    else:
        print("O maior e", numC)
        print("O do meio e", numA)
        print("O menor e", numB)
else:
    if numB > numC:
        print("O maior e",numB)
        if numA > numC:
            print("O do meio e", numA)
            print("O menor e", numC)
        else:
            print("O do meio e", numC)
            print("O menor e", numA)                
    else:
        print("O maior e", numC)
        print("O do meio e", numB)
        print("O do menor e", numA)