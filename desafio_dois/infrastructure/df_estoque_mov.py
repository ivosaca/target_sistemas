import pandas as pd
import os
import datetime


class movEstoque:
    def __init__(self):
        self.cwd = os.getcwd()
        self.estoque_inicial_json = os.path.join(
            self.cwd + "/desafio_dois/dados/estoque_inicial.json"
        )
        self.horario_mov = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.estoque_atual_json = os.path.join(
            self.cwd + "/desafio_dois/dados/estoque_atual.json"
        )

    def df_estoque_inicial(self):
        """Geração do dataframe de estoque a partir do arquivo JSON."""
        data = pd.read_json(self.estoque_inicial_json)
        df_estoque = pd.json_normalize(data["estoque"])
        df_estoque["horario_mov"] = self.horario_mov

        return df_estoque

    def df_estoque_atual(self):
        """Geração do dataframe de estoque atual a partir do arquivo JSON."""
        data = pd.read_json(self.estoque_atual_json)
        df_estoque = pd.json_normalize(data["estoque"])
        df_estoque["horario_mov"] = self.horario_mov
        return df_estoque

    def item_selecionado(self, produto):
        """Filtragem do dataframe pelo código do produto selecionado."""
        df_estoque = self.df_estoque_atual()
        df_produto_selecionado = df_estoque.loc[df_estoque["codigoProduto"] == produto]
        if df_produto_selecionado.empty:
            continuar = input(
                "Erro: Código do produto não encontrado no estoque. Gostaria de tentar novamente? (s/n)\n"
            )
            if continuar.lower() == "s":
                novo_produto = int(input("Digite o código do produto novamente: \n"))
                return 1, self.item_selecionado(novo_produto)
            else:
                return 0, print("Operação encerrada pelo usuário.\n")
        else:
            return print(df_produto_selecionado), df_produto_selecionado

    def movimentar_estoque(self, produto, tipo_mov, quantidade_mov):
        """Atualização do estoque com base na movimentação."""
        df_estoque = self.df_estoque_atual()
        df_mov
        print(f"\nMovimentando produto...\n")
        if tipo_mov.lower() == "entrada":

            df_estoque.loc[
                df_estoque["codigoProduto"] == produto, "estoque"
            ] += quantidade_mov
            print(
                f"Entrada de {quantidade_mov} unidades do produto '{produto}' realizada com sucesso."
            )
        elif tipo_mov.lower() == "saida":
            while (
                df_estoque.loc[
                    df_estoque["codigoProduto"] == produto, "estoque"
                ].values[0]
                <= quantidade_mov
            ):
                print(
                    f"Erro: Quantidade insuficiente em estoque para o produto '{produto}'."
                )
                quantidade_mov = int(input("Digite a quantidade a ser movimentada: "))

            if (
                df_estoque.loc[
                    df_estoque["codigoProduto"] == produto, "estoque"
                ].values[0]
                >= quantidade_mov
            ):
                df_estoque.loc[
                    df_estoque["codigoProduto"] == produto, "estoque"
                ] -= quantidade_mov
                print(
                    f"Saída de {quantidade_mov} unidades do produto '{produto}' realizada com sucesso."
                )

        else:
            print("Tipo de movimentação inválido. Use 'entrada' ou 'saida'.")

        print("\nEstoque atualizado:")
        print(df_estoque)


# print(movEstoque().df_estoque_atual())
# print(movEstoque().item_selecionado(106))
