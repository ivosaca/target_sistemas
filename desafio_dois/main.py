import json

with open("desafio_dois/dados/estoque_inicial.json", "r") as file:
    data = json.load(file)

estoque_inicial = data["estoque"]


mov_loop = 1
while mov_loop == 1:
    inicio = input("Deseja iniciar uma movimentação? (s/n)")
    if inicio.lower() == "s":
        print("\n\nEstoque Inicial: \n")
        for i in estoque_inicial:
            print(
                "Produto:",
                i["codigoProduto"],
                "-",
                i["descricaoProduto"],
                "-",
                " Estoque: ",
                i["estoque"],
            )
        mov = input("\nDigite 'e' para entrada ou 's' para saída de produtos: ")
        qtidade_mov = int(input("Digite a quantidade a ser movimentada: "))
        while qtidade_mov <= 0:
            print("Quantidade inválida. Deve ser maior que zero.")
            qtidade_mov = int(input("Digite a quantidade a ser movimentada: "))
        cod_produto = int(input("Digite o código do produto a ser movimentado: "))
        while cod_produto not in [item["codigoProduto"] for item in estoque_inicial]:
            print("Código de produto inválido.")
            cod_produto = int(input("Digite o código do produto a ser movimentado: "))
            continue
        print(f"\nMovimentando produto...\n {cod_}")
        for item in estoque_inicial:
            if item["codigoProduto"] == cod_produto:
                if mov.lower() == "e":
                    item["estoque"] += qtidade_mov
                    print(
                        f"Entrada de {qtidade_mov} unidades do produto '{cod_produto}' realizada com sucesso."
                    )
                elif mov.lower() == "s":
                    if item["estoque"] >= qtidade_mov:
                        item["estoque"] -= qtidade_mov
                        print(
                            f"Saída de {qtidade_mov} unidades do produto '{cod_produto}' realizada com sucesso."
                        )
                    else:
                        print(
                            f"Erro: Quantidade insuficiente em estoque para o produto '{cod_produto}'."
                        )
                else:
                    print(
                        "Tipo de movimentação inválido. Use 'e' para entrada ou 's' para saída."
                    )

    elif inicio.lower() == "n":
        print("Encerrando o programa.")
        mov_loop = 0
    else:
        print("Entrada inválida. Por favor, digite 's' ou 'n'.")
