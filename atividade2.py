nome = input("Insira o nome do lutador: ")
peso = input("Insira o peso do lutador: ")
if peso < 52:
    print("O seu lutador está na categoria invalido")
elif peso >=52 and peso <65:
    print("O seu lutador está na categoria pena")
elif peso >=65 and peso <72:
    print("O seu lutador está na categoria leve")
elif peso >=72 and peso <79:
    print("O seu lutador está na categoria ligeiro")
elif peso >=79 and peso <86:
    print("O seu lutador está na categoria meio-médio")
elif peso >=86 and peso <90:
    print("O seu lutador está na categoria médio")
elif peso >=90 and peso <100:
    print("O seu lutador está na categoria meio-pesado")
elif peso >=100:
    print("O seu lutador está na categoria pesado")