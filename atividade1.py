risco = input("Insira a quantidade de risco que estaria disposto a tomar: ")
valor = int(input("Insira a quantia de dinheiro que quer investir: "))
if risco == "BX":
    if valor <=1000:
        print("envista em uma conta poupança")
    else:
        print("envista em bitcoin")
elif risco == "AL":
    if valor <=1000:
        print("envista em uma renda fixa")
    else:
        print("envista em ações")
else:
    print("informação invalida")