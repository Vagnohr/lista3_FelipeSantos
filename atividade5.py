custo = int(input("Insira o preço de custo do produto: "))
if custo <=100:
    margem_bruta = (custo/100)*45
    venda=margem_bruta+custo
    print("O preço de venda do produto é {}".format(venda))
    print("Felipe Bortoluzz dos Santos")
elif custo >100:
    margem_bruta = (custo/100)*35
    venda=margem_bruta+custo
    print("O preço de venda do produto é {}".format(margem_bruta))
    print("Felipe Bortoluzz dos Santos")