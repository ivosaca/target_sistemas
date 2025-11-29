import pandas as pd
import os
import datetime


class movEstoque:
    def __init__(self):
        self.cwd = os.getcwd()
        self.json_path = os.path.join(
            self.cwd + "/desafio_dois/dados/estoque_inicial.json"
        )
        self.horario_mov = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def df_estoque_atual(self):
        """Geração do dataframe de estoque a partir do arquivo JSON."""
        data = pd.read_json(self.json_path)
        df_estoque = pd.json_normalize(data["estoque"])
        df_estoque["horario_mov"] = self.horario_mov
        return df_estoque

    def item_selecionado(self, produto):
        """Filtragem do dataframe pelo código do produto selecionado."""
        df_estoque = self.df_estoque_atual()
        df_produto_selecionado = df_estoque.loc[df_estoque["codigoProduto"] == produto]
        if df_produto_selecionado.empty:
            continuar = input(
                "Erro: Código do produto não encontrado no estoque. Gostaria de tentar novamente? (s/n)"
            )
            if continuar.lower() == "s":
                novo_produto = int(input("Digite o código do produto novamente: "))
                return self.item_selecionado(novo_produto), 0
            else:
                return print("Operação encerrada pelo usuário."), 1
        return df_produto_selecionado


# print(movEstoque().df_estoque_atual())
# print(movEstoque().item_selecionado(106))
