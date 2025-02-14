nome = input("Insira o nome do municipio: ")
eleitores = int(input("Insira a quantidade de eleitores: "))
eleitor_votos = int(input("Insira quantos votos o eleitor recebeu: "))
votos = eleitores/2
if eleitores >= 200000:
    if eleitor_votos < votos:
        print("Havera segundo turno")
    elif eleitor_votos >= votos:
        print("Não havera segundo turno")
elif eleitor_votos > eleitores:
    print("quantidade de votos invalida")
else:
    print("não há eleitores suficientes para segundo turno")