risco = input("Insira a quantidade de risco que estaria disposto a tomar: ")
valor = int(input("Insira a quantia de dinheiro que quer investir: "))
if risco == "BX":
    if valor <=1000:
        print("envista em uma conta poupança")
        print("Felipe Bortoluzz dos Santos")
    else:
        print("envista em bitcoin")
        print("Felipe Bortoluzz dos Santos")
elif risco == "AL":
    if valor <=1000:
        print("envista em uma renda fixa")
        print("Felipe Bortoluzz dos Santos")
    else:
        print("envista em ações")
        print("Felipe Bortoluzz dos Santos")
else:
    print("informação invalida")
    print("Felipe Bortoluzz dos Santos")