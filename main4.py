quantidadeProdutoEstoque = 100
quantidadeEstoqueOriginal = 100
while quantidadeProdutoEstoque > 0:
    qtd = int(input("Digite quantos produtos deseja: "))

    if quantidadeProdutoEstoque - qtd < 0:
        print(f'Quantidade Indisponível! Estoque atual {quantidadeProdutoEstoque}')
        continue
    quantidadeProdutoEstoque -= qtd

    continuar = input("Deseja algo mais? (S/N)").upper()
    if continuar != ("S"):
        break

porcentagem = 100*(quantidadeEstoqueOriginal-quantidadeProdutoEstoque)/quantidadeEstoqueOriginal
print(f'Total Estoque: {quantidadeProdutoEstoque}')
print(f'Porcentagem Vendida: {porcentagem:.0f}%')
