import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# importando os dados, lendo o data frame
df = pd.read_excel('dados_vendas_empresa_1.xlsx')
df.columns = (
    df.columns.str.strip().str.lower()
    .str.replace(' ', '_').str.replace('ê', 'e')
    .str.replace('ç', 'c').str.replace('ã', 'a')
    .str.replace('á', 'a').str.replace('é', 'e')
    .str.replace('í', 'i').str.replace('ó', 'o')
    .str.replace('ú', 'u')
)
print(df.columns.tolist())
print(df.head())

# Visualizar as primeiras linhas do data frame
print(df.head())

# Conhecer os dados
print(f"\nSeu dataset tem {df.shape[0]} linhas e {df.shape[1]} colunas")

# nomes das colunas
print(df.columns.tolist())

# verificar se tem dados faltando
dados_faltantes = df.isnull().sum()
print(dados_faltantes)

# resumo estatístico simples
print(df.describe())

# valores zerados em colunas numericas
df[['quantidade', 'preco_unitario', 'total_da_venda', 'ano', 'mes', 'dia', 'dia_da_semana']].eq(0).sum()

# operações simples
# somar uma coluna
print(df['total_da_venda'].sum())

# Remove commas and periods and convert 'preco_unitario' to numeric
df['preco_unitario'] = (
    df['preco_unitario']
    .astype(str)
    .str.replace('.', '', regex=False)
    .str.replace(',', '.', regex=False)
)
# converte o preço unitário para float
df['preco_unitario'] = pd.to_numeric(df['preco_unitario'], errors='coerce')

# converte a quantidade caso seja necessário
df['quantidade'] = pd.to_numeric(df['quantidade'], errors='coerce')

# multiplicando colunas
df['total_da_venda'] = df['quantidade'] * df['preco_unitario']
print(df['total_da_venda'])

# média da coluna total venda
print(df['total_da_venda'].mean())

# média da coluna quantidade
print(df['quantidade'].mean())

# aprendizado de filtros

# filtrar itens da categoria Eletrônicos
print(df[df['categoria'] == 'Eletrônicos'])

# filtros compostos ou combinados
print(df[(df['categoria'] == 'Eletrônicos') & (df['quantidade'] == 10)])

# Agrupamentos

# média de quantidade vendida por categoria
print(df.groupby('categoria')['quantidade'].mean())

# soma de quantidade vendida por categoria
print(df.groupby('categoria')['quantidade'].sum())

# multiplas estatísticas por categoria
print(df.groupby('categoria')['quantidade'].agg(['mean', 'sum', 'count', 'max', 'min']))

# Gráficos

# gráfico simples de barras
df['categoria'].value_counts().plot(kind='bar')
plt.show()

# histograma de distribuição dos valores de venda 'total_da_venda'
df['total_da_venda'].plot(kind='hist', bins=20)
plt.show()

# histograma versão 2.0
plt.figure(figsize=(8, 6))
df['total_da_venda'].hist(bins=20)
edgecolor = 'black'
plt.xlabel('Valor da Venda')
plt.ylabel('Frequência')
plt.title('Distribuição dos Valores de Venda')
plt.show()

# gráfico de barras horizontais com o total_da_venda
df['categoria'].value_counts().plot(kind='barh')
plt.show()

# gráfico de pizza com o total_da_venda
df['categoria'].value_counts().plot(kind='pie')
plt.show()

# gráfico de área com o total_da_venda
df['categoria'].value_counts().plot(kind='area')
plt.show()

# Criar uma nova coluna STATUS DO CLIENTE
df['Status'] = np.where(df['total_da_venda'] > 10000, 'VIP', 'Não VIP')

# visualizar novamente as colunas do data set
print(df.head())

# Trabalhando com datas

# Garantir que as informações de data estão no formato datetime
df['data_da_venda'] = pd.to_datetime(df['data_da_venda'])

# extrair as informações de data
df['ano'] = df['data_da_venda'].dt.year
df['mes'] = df['data_da_venda'].dt.month
df['dia'] = df['data_da_venda'].dt.day
df['dia_da_semana'] = df['data_da_venda'].dt.dayofweek

# Analise de oportunidades

# qual o total de vendas?
print(df['total_da_venda'].sum())

# qual a media de vendas?
print(df['total_da_venda'].mean())

# qual categoria vende mais?
print(df.groupby('categoria')['total_da_venda'].sum())

# maior venda individual
print(df['total_da_venda'].max())

# dia da semana com a maior venda
print(df.groupby('dia_da_semana')['total_da_venda'].sum())

# Analise Final

# gráfico de vendas totais por mes
df.groupby('mes')['total_da_venda'].sum().plot(kind='bar')
plt.show()

# grafico de pizza do percentual de vendas por categoria
df['categoria'].value_counts(normalize=True).plot(kind='pie')
plt.show()

# grafico de media de vendas em cada dia da semana
df.groupby('dia_da_semana')['total_da_venda'].mean().plot(kind='bar')
plt.show()

# gráfico de dispersão do dia da semana com o total de venda
df.plot(x='dia_da_semana', y='total_da_venda', kind='scatter')
plt.show()

# boxplot da distribuição de vendas por dia
df.boxplot(column='total_da_venda', by='dia_da_semana')
plt.show()

# boxplot por total de vendas por categoria
df.boxplot(column='total_da_venda', by='categoria')
plt.show()

# boxplot por total de vendas por mes
df.boxplot(column='total_da_venda', by='mes')
plt.show()

# comparando o valor medio de vendas entre vip e não vip
print(df.groupby('Status')['total_da_venda'].mean())

# comparando o valor total da venda entre vip e não vip
print(df.groupby('Status')['total_da_venda'].sum())

# comparando a quantidade vendida entre vip e não vip
print(df.groupby('Status')['quantidade'].sum())

# comparando as compras dos vips e não vips por categoria
print(df.groupby(['Status', 'categoria'])['quantidade'].sum())

# conclusão da estratégia

# gerar um gráfico de barras comparando as compras dos vips e não vips por categoria
ax = df.groupby(['Status', 'categoria'])['total_da_venda'].sum().unstack().plot(kind='bar')
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()
