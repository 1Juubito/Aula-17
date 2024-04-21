#Contador

totalPedido = 0
while True:
    valor = float(input("Digite o valor do produto: "))
    totalPedido += valor

    continuar = input("Deseja comprar algo mais? (S/N) ").upper()
    if continuar != ("S"):
        break

print(f"Total Pedido: R$ {totalPedido}")
