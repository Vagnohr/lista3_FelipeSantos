nome = print("Insira o seu nome: ")
idade = print("Insira a sua idade: ")
sexo = print("Insira o seu sexo: ")
if "f" or "F" in sexo:
    if idade >=21 and idade <=34:
        print("Você sera aceita para servir")
    else:
        print("Você não sera aceita para servir")
if "m" or "M" in sexo:
    if idade >=18 and idade <=39:
        print("Você sera aceita para servir")
    else:
        print("Você não sera aceito para servir")
else:
    print("sexo invalido")