import pandas as pd
import os

cwd = os.getcwd()

data = pd.read_json(cwd + "/desafio_um/dto/desafio_um.json")
df = pd.json_normalize(data["vendas"])


def comissao(row):
    if row["valor"] < 100:
        return 0
    elif row["valor"] >= 100 and row["valor"] < 500:
        return round(row["valor"] * 0.01, 2)
    else:
        return round(row["valor"] * 0.05, 2)


df["comissao"] = df.apply(comissao, axis=1)
print(df)
df_comissao_total = df.groupby("vendedor").sum()
df_comissao_total = df_comissao_total["comissao"].reset_index()
print(df_comissao_total)


df_comissao_total.to_json(
    cwd + "/desafio_um/resultado/resultado.json",
    orient="records",
    force_ascii=False,
)

with pd.ExcelWriter(cwd + "/desafio_um/resultado/resultado.xlsx") as f:
    df_comissao_total.to_excel(
        f,
        sheet_name="Comissão por Vendedor",
        index=False,
    )
    df.to_excel(
        f,
        sheet_name="Comissão por Venda",
        index=False,
    )
