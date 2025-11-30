import pandas as pd
import os
import datetime
import json


class movEstoque:
    def __init__(self):
        self.cwd = os.getcwd()
        self.estoque_inicial_json = os.path.join(
            self.cwd + "/desafio_dois/dados/estoque_inicial.json"
        )
        self.estoque_atual_json = os.path.join(
            self.cwd + "/desafio_dois/dados/estoque_atual.json"
        )

    def df_estoque_inicial(self):
        """Geração do dataframe de estoque a partir do arquivo JSON."""
        data = pd.read_json(self.estoque_inicial_json)
        df_estoque = pd.json_normalize(data["estoque"])
        horario = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        df_estoque["horario_mov"] = horario
        df_estoque["codigoProduto"] = df_estoque["codigoProduto"].astype(int)
        df_estoque["estoque"] = df_estoque["estoque"].astype(int)
        return df_estoque

    def df_estoque_atual(self):
        """Geração do dataframe de estoque a partir do arquivo JSON."""
        data = pd.read_json(self.estoque_atual_json)
        df_estoque = pd.json_normalize(data["estoque"])
        df_estoque["codigoProduto"] = df_estoque["codigoProduto"].astype(int)
        df_estoque["estoque"] = df_estoque["estoque"].astype(int)
        return df_estoque

    def item_selecionado(self, produto):
        """Filtragem do dataframe pelo código do produto selecionado."""
        df_estoque = self.df_estoque_atual()
        df_produto_selecionado = df_estoque.loc[df_estoque["codigoProduto"] == produto]
        df_produto_selecionado = df_produto_selecionado.iloc[-1:]
        df_produto_selecionado["horario_mov"] = datetime.datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
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
        print(f"\nMovimentando produto...\n")
        if tipo_mov.lower() == "entrada":
            df_mov = df_estoque.loc[df_estoque["codigoProduto"] == produto]
            df_mov = df_mov.iloc[-1:]
            df_mov["horario_mov"] = datetime.datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
            df_mov.loc[
                df_estoque["codigoProduto"] == produto, "estoque"
            ] += quantidade_mov
            df_estoque = pd.concat([df_estoque, df_mov], ignore_index=True)
            print(
                f"Entrada de {quantidade_mov} unidades do produto '{produto}' realizada com sucesso."
            )
            self.salvar_estoque_atual(df_estoque)
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
                df_mov = df_estoque.loc[df_estoque["codigoProduto"] == produto]
                df_mov = df_mov.iloc[-1:]
                df_mov["horario_mov"] = datetime.datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
                df_mov.loc[
                    df_estoque["codigoProduto"] == produto, "estoque"
                ] -= quantidade_mov
                df_estoque = pd.concat([df_estoque, df_mov], ignore_index=True)
                print(
                    f"Saída de {quantidade_mov} unidades do produto '{produto}' realizada com sucesso."
                )
                self.salvar_estoque_atual(df_estoque)

        else:
            print("Tipo de movimentação inválido. Use 'entrada' ou 'saida'.")

        print("\nEstoque atualizado:")
        print(df_estoque)

    def salvar_estoque_atual(self, dataframe):
        """Salva o dataframe atualizado de estoque em um arquivo JSON."""
        df_estoque = dataframe
        estoque_dict = {"estoque": df_estoque.to_dict(orient="records")}
        # estoque_dict = pd.DataFrame(estoque_dict)
        with open(self.estoque_atual_json, "w") as f:
            json.dump(estoque_dict, f, indent=4)

    def reset_estoque_atual(self):
        """Reseta o estoque atual para o estoque inicial."""
        df_estoque_inicial = self.df_estoque_inicial()
        estoque_dict = {"estoque": df_estoque_inicial.to_dict(orient="records")}
        with open(self.estoque_atual_json, "w") as f:
            json.dump(estoque_dict, f, indent=4)
        print("Estoque atual resetado para o estoque inicial com sucesso.")
