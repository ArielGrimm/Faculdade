print("Digite a quantidade total de miligramas de colesterol:")
colesterol = int(input())

if colesterol <= 130:
    print("Você está saudável")
else:
    porcentagem = ((colesterol * 100) / 130) - 100
    print("A quantidade de colesterol está %.2f" %porcentagem, "% acima do ideal")