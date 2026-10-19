import pandas as pd

dados = pd.read_csv("vgsales.csv")

print("PRIMEIRAS LINHAS:")
print(dados.head())

print("\nDIMENSÕES:")
print(dados.shape)

print("\nCOLUNAS:")
print(dados.columns.tolist())

print("\nINFORMAÇÕES GERAIS:")
dados.info()

print("\nRESUMO ESTATÍSTICO:")
print(dados.describe())

print("\nVALORES AUSENTES:")
print(dados.isnull().sum())

print("\nREGISTROS DUPLICADOS:")
print(dados.duplicated().sum())

print("\n1. GÊNEROS MAIS COMUNS:")
print(dados["Genre"].value_counts().head())

print("\n2. PLATAFORMAS COM MAIS JOGOS:")
print(dados["Platform"].value_counts().head())

print("\n3. ANOS COM MAIS LANÇAMENTOS:")
print(dados["Year"].value_counts().head())

print("\n4. JOGOS COM MAIORES VENDAS:")
print(dados.sort_values("Global_Sales", ascending=False)
        [["Name", "Global_Sales"]].head())

print("\n5. EMPRESAS QUE PUBLICARAM MAIS JOGOS:")
print(dados["Publisher"].value_counts().head())


print("\nQUANTIDADE DE JOGOS POR GÊNERO:")
print(dados["Genre"].value_counts())

print("\nQUANTIDADE DE JOGOS POR PLATAFORMA:")
print(dados["Platform"].value_counts())


print("\nJOGOS DO GÊNERO ACTION:")
print(dados[dados["Genre"] == "Action"][["Name", "Platform"]].head(10))

print("\nJOGOS COM VENDAS MUNDIAIS ACIMA DE 20 MILHÕES:")
print(dados[dados["Global_Sales"] > 20][["Name", "Global_Sales"]])

print("\n" + "=" * 40)
print("ETAPA 4 - LIMPEZA E TRATAMENTO")
print("=" * 40)


dados_tratados = dados.copy()


print("\nVALORES AUSENTES ANTES DO TRATAMENTO:")
print(dados_tratados.isnull().sum())


for coluna in dados_tratados.select_dtypes(include="object").columns:
    dados_tratados[coluna] = dados_tratados[coluna].str.strip()


print("\nVALORES AUSENTES DEPOIS DA LIMPEZA:")
print(dados_tratados.isnull().sum())

dados_tratados.to_csv(
    "vgsales_tratado.csv",
    index=False
)

print("\nBase tratada salva como vgsales_tratado.csv")


import matplotlib.pyplot as plt
import seaborn as sns


jogos_genero = dados_tratados["Genre"].value_counts()

plt.figure(figsize=(10, 6))
jogos_genero.plot(kind="bar")
plt.title("Quantidade de Jogos por Genero")
plt.xlabel("Genero")
plt.ylabel("Quantidade de Jogos")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("grafico_generos.png")
plt.show()

jogos_plataforma = dados_tratados["Platform"].value_counts().head(10)

plt.figure(figsize=(10, 6))
jogos_plataforma.plot(kind="bar")
plt.title("10 Plataformas com Mais Jogos")
plt.xlabel("Plataforma")
plt.ylabel("Quantidade de Jogos")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("grafico_plataformas.png")
plt.show()

print("\nGraficos salvos com sucesso!")


print("\nVENDAS TOTAIS POR ANO:")

dados_ano = dados_tratados.dropna(subset=["Year"]).copy()

vendas_ano = dados_ano.groupby("Year")["Global_Sales"].sum()
print(vendas_ano.sort_values(ascending=False).head(10))

plt.figure(figsize=(10, 6))
vendas_ano.sort_index().plot(kind="line", marker="o")
plt.title("Vendas Globais de Jogos por Ano")
plt.xlabel("Ano de lancamento")
plt.ylabel("Vendas globais (em milhoes)")
plt.tight_layout()
plt.savefig("grafico_vendas_ano.png")
plt.show()

print("\nAnalise concluida!")



print("\n=== RECOMENDAÇÕES PARA O NEGÓCIO ===")


vendas_genero = dados_tratados.groupby("Genre")["Global_Sales"].sum()
vendas_genero = vendas_genero.sort_values(ascending=False)

print("\nGêneros com maiores vendas globais:")
print(vendas_genero.head(5))


vendas_plataforma = dados_tratados.groupby("Platform")["Global_Sales"].sum()
vendas_plataforma = vendas_plataforma.sort_values(ascending=False)

print("\nPlataformas com maiores vendas globais:")
print(vendas_plataforma.head(5))
print("TESTE DA ETAPA 6")
