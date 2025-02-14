salario = int(input("Insira a quantia do seu salario: "))
imprestimo = int(input("Insira a quantia do seu imprestimo: "))
conta = (salario/100)*8
if conta >= imprestimo:
    print("Você não recebera o seu imprestimo")
if conta < imprestimo:
    print("Você recebera o seu imprestimo")