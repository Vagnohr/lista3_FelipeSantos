nome = input("Insira o nome do lutador: ")
peso = int(input("Insira o peso do lutador: "))
if peso < 52:
    print("O seu lutador é invalido para lutar")
    print("Felipe Bortoluzz dos Santos")
elif peso >=52 and peso <65:
    print("O seu lutador está na categoria pena")
    print("Felipe Bortoluzz dos Santos")
elif peso >=65 and peso <72:
    print("O seu lutador está na categoria leve")
    print("Felipe Bortoluzz dos Santos")
elif peso >=72 and peso <79:
    print("O seu lutador está na categoria ligeiro")
    print("Felipe Bortoluzz dos Santos")
elif peso >=79 and peso <86:
    print("O seu lutador está na categoria meio-médio")
    print("Felipe Bortoluzz dos Santos")
elif peso >=86 and peso <90:
    print("O seu lutador está na categoria médio")
    print("Felipe Bortoluzz dos Santos")
elif peso >=90 and peso <100:
    print("O seu lutador está na categoria meio-pesado")
    print("Felipe Bortoluzz dos Santos")
elif peso >=100:
    print("O seu lutador está na categoria pesado")
    print("Felipe Bortoluzz dos Santos")