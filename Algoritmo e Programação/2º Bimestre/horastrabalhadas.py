print("Digite o número de horas trabalhadas")
horastrab = int(input())
print("Digite o valor do salário mínimo")
salmin = float(input())
print("Digite o número de horas extras")
horasext = int(input())
valhorastrab = salmin / 8
valhorasext = salmin / 4
salbruto = horastrab * valhorastrab
print("O valor do salário bruto é", salbruto)
tothorasext = horasext * valhorasext
print("O valor a receber de horas extras é", tothorasext)
totsalario = salbruto + tothorasext
print("O valor total do salário é", totsalario)