print("Digite o valor da hora aula")
valhora = float(input())
print("Digite o numero de horas trabalhadas no mês")
numhoras = float(input())
print("Digite o percentual de desconto do INSS")
descinss = float(input())
salbruto = valhora * numhoras
print("O valor do salário bruto é:", salbruto)
valimposto = (salbruto * descinss) / 100
print("O valor do imposto é: ", valimposto)
salliq = salbruto - valimposto
print("O salario líquido do professor é %.2f" % salliq)