idade = int(input("Digite sua idade: "))
genero = input("Digite seu gênero: ")

#if idade < 18:
    #print("Proibido se alistar")
if idade != 100:
    print("Você é um ancião, não é necessário se alistar")
elif genero.upper() == ("M") or genero.upper() == ("MASCULINO"):
    print("Obrigatório se alistar")
elif genero.upper() == ("F") or genero.upper() == ("FEMININO"):
    print("Alistamento opcional")
else:
    print("Gênero inválido")