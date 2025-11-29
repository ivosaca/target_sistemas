from infrastructure.df_estoque_mov import movEstoque

moveestoque = movEstoque()
mov_loop = 1
while mov_loop == 1:
    inicio = input("Deseja iniciar uma movimentação? (s/n)")
    if inicio.lower() == "s":
        print("\n\nEstoque Inicial: \n")
        estoque_atual = moveestoque.df_estoque_inicial()
        print(estoque_atual)
        while mov_loop == 1:
            produto_selecionado = input("\nDigite o código do produto: \n")
            try:
                produto_selecionado = int(produto_selecionado)
            except ValueError:
                print("Código inválido.")
                while not isinstance(produto_selecionado, int):
                    try:
                        produto_selecionado = int(
                            input("Digite o código do produto: \n")
                        )
                    except ValueError:
                        print("Código não encontrado na tabela.")
            mov_loop, produto_selecionado = moveestoque.item_selecionado(
                produto_selecionado
            )
            if mov_loop == 0:
                break
            mov = input("\nDigite 'e' para entrada ou 's' para saída de produtos: ")
            while mov.lower() not in ["e", "s"]:
                mov = input(
                    "Tipo de movimentação inválido. Use 'e' para entrada ou 's' para saída."
                )
            qtidade_mov = input("Digite a quantidade a ser movimentada: \n")
            try:
                qtidade_mov = int(qtidade_mov)
            except ValueError:
                print("Quantidade inválida. Deve ser um número inteiro maior que zero.")
                while not isinstance(qtidade_mov, int):
                    try:
                        qtidade_mov = int(
                            input("Digite a quantidade a ser movimentada: \n")
                        )
                    except ValueError:
                        print(
                            "Quantidade inválida. Deve ser um número inteiro maior que zero."
                        )

            while qtidade_mov <= 0:
                try:
                    qtidade_mov = int(qtidade_mov)
                finally:
                    print("Quantidade inválida. Deve ser maior que zero.")
                    qtidade_mov = input("Digite a quantidade a ser movimentada: ")

            #
            #
            moveestoque.movimentar_estoque(
                produto_selecionado["codigoProduto"].values[0],
                "entrada" if mov.lower() == "e" else "saida",
                qtidade_mov,
            )
            mov_loop = 1

    elif inicio.lower() == "n":
        print("Encerrando o programa.")
        mov_loop = 0
    else:
        print("Entrada inválida. Por favor, digite 's' ou 'n'.")
