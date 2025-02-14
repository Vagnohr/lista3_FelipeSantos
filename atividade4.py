nome = input("Insira o seu nome: ")
idade = int(input("Insira a sua idade: "))
sexo = input("Insira o seu sexo: ")
if "f" in sexo or "F" in sexo:
    if idade >=21 and idade <=34:
        print("Você sera aceita para servir")
        print("Felipe Bortoluzz dos Santos")
    else:
        print("Você não sera aceita para servir")
        print("Felipe Bortoluzz dos Santos")
elif "m" in sexo or "M" in sexo:
    if idade >=18 and idade <=39:
        print("Você sera aceito para servir")
        print("Felipe Bortoluzz dos Santos")
    else:
        print("Você não sera aceito para servir")
        print("Felipe Bortoluzz dos Santos")
else:
    print("sexo invalido")
    print("Felipe Bortoluzz dos Santos")