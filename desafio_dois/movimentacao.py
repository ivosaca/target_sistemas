from infrastructure.df_estoque_mov import movEstoque

moveestoque = movEstoque()

inicio = input("Olá. Deseja iniciar uma movimentação? (s/n) ")
if inicio.lower() == "s":
    estoque_atual = moveestoque.df_estoque_atual()
    print(f"\nEstoque atual:\n {estoque_atual}\n")
    produto = input("Digite o código do produto: ")
    produto_selecionado, loop = moveestoque.item_selecionado(produto)  # resolvido

    tipo_mov = input("Digite o tipo de movimentação (entrada/saida): ")
    quantidade_mov = int(input("Digite a quantidade a ser movimentada: "))

    if tipo_mov.lower() == "entrada":
        estoque_atual.loc[
            estoque_atual["codigoProduto"] == produto, "estoque"
        ] += quantidade_mov
        print(
            f"Entrada de {quantidade_mov} unidades do produto '{produto}' realizada com sucesso."
        )
    elif tipo_mov.lower() == "saida":
        if (
            estoque_atual.loc[
                estoque_atual["codigoProduto"] == produto, "estoque"
            ].values[0]
            >= quantidade_mov
        ):
            estoque_atual.loc[
                estoque_atual["produto"] == produto, "estoque"
            ] -= quantidade_mov
            print(
                f"Saída de {quantidade_mov} unidades do produto '{produto}' realizada com sucesso."
            )
        else:
            print(
                f"Erro: Quantidade insuficiente em estoque para o produto '{produto}'."
            )
    else:
        print("Tipo de movimentação inválido. Use 'entrada' ou 'saida'.")

    print("\nEstoque atualizado:")
    print(estoque_atual)
