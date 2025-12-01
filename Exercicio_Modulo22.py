import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('ecommerce_estatistica.csv') # Lendo arquivo para criação do DF
print(df.head().to_string())
print('Dados nulos:\n', df.isnull().sum())


# Gráfico de Histograma com Parâmetros - OK
# Cria um gráfico de Histograma com a relação entre o 'Gênero' e a 'Quantidade' de itens vendidos
plt.figure(figsize=(8, 9))
plt.hist(df['Gênero'], bins=100, color='#032954', alpha=0.8)
plt.title('Gêneros mais vendidos')
plt.xlabel('Gêneros')
plt.xticks(rotation=70)
plt.ylabel('Quantidade')
plt.grid(True)
plt.show()


# Gráfico de Dispersão
# Cria um gráfico de Dispersão com a relação entre 'Preço' e 'Qtd_Vendidos_Cod'
sns.jointplot(x='Preço', y='Qtd_Vendidos_Cod', data=df, kind='scatter')
plt.xlabel('Preço dos produtos')
plt.ylabel('Quantidade de vendidos')
plt.show()


# Mapa de calor - OK
# Cria uma mapa de calor relacionando 'Marca_Cod', 'Temporada_Cod', 'Material_Cod'
df_corr = df[['Marca_Cod', 'Temporada_Cod', 'Material_Cod']].corr()
plt.figure(figsize=(10, 6))
sns.heatmap(df_corr, annot=True, fmt=".2f")
plt.title('Mapa de Calor com a relação entre Marca, Temporada e Material')
plt.show()


# Gráfico de Barras - OK
# Cria um gráfico de baras mostrando as 'Marcas' mais vendidas
plt.figure(figsize=(20, 10))
df['Marca'].value_counts().plot(kind='bar', color='#66CDAA')
plt.title('Marcas mais vendidas')
plt.xlabel('Produto')
plt.ylabel('Quantidade')
plt.xticks(rotation=90)
plt.show()

# Gráfico pizza - OK
# Cria um gráfico pizza mostrando a % de cada 'Temporada_Cod' vendida
x = df['Temporada_Cod'].value_counts().index
y = df['Temporada_Cod'].value_counts().values
labels_legenda = df.drop_duplicates(subset=['Temporada_Cod']) \
                    .set_index('Temporada_Cod')['Temporada'] \
                    .loc[x]

plt.figure(figsize=(15, 10))
fatias, textos, porcentagens = plt.pie(y, labels=x, autopct='%.1f%%',
                                       startangle=0, rotatelabels=True)

plt.title('Temporadas mais vendidas')

plt.legend(fatias, labels_legenda, title="Temporadas",
           loc="center left", bbox_to_anchor=(1, 0.5))

plt.tight_layout()
plt.show()

# Gráfico de Densidade - OK
# Cria um gráfico ilustrando a densidade das 'Notas' dos produtos
plt.figure(figsize=(10, 6))
sns.kdeplot(df['Nota'], fill=True, color='#66CDAA')
plt.title('Densidade das notas')
plt.xlabel('Nota')
plt.show()

# Gráfico de Regressão - OK
# Cria um gráfico de regressão com a relação entre 'Preço' e 'Desconto'
sns.regplot(x='Preço', y='Desconto', data=df, color='#66CDAA', scatter_kws={'alpha': 0.5, 'color': '#032e1f'})
plt.title('Regressão de preço por Desconto')
plt.xlabel('Preço')
plt.ylabel('Desconto')
plt.show()