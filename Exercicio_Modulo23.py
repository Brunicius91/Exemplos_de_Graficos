import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc
from matplotlib.pyplot import title

df = pd.read_csv('ecommerce_estatistica.csv') # Lendo arquivo para criação do DF

def cria_graficos(df):
    # Gráfico de Histograma com Parâmetros - OK
    # Cria um gráfico de Histograma com a relação entre o 'Gênero' e a 'Quantidade' de itens vendidos

    fig1 = px.histogram(df, x='Gênero', y='Qtd_Vendidos', nbins=10, title='Gêneros mais vendidos', color='Gênero')
    fig1.update_layout(title='Gráfico de Histograma com relação entre Gênero e Quantidade de itens vendidos')
    fig1.update_yaxes(title_text='Quantidades Vendidas')

    # Gráfico de Dispersão
    # Cria um gráfico de Dispersão com a relação entre 'Preço' e 'Qtd_Vendidos_Cod'

    fig2 = px.scatter(df, x='Preço', y='Qtd_Vendidos_Cod')
    fig2.update_yaxes(title_text='Código de Quantidades Vendidas')
    fig2.update_layout(title='Gráfico de dispersão com a relação entre Preço e Quantidade Vendidas')

    # Mapa de calor - OK
    # Cria uma mapa de calor relacionando 'Marca_Cod', 'Temporada_Cod', 'Material_Cod'
    df_corr = df[['Marca_Cod', 'Temporada_Cod', 'Material_Cod']].corr()
    fig3 = px.imshow(df_corr, title='Mapa de calor de Correlação')
    fig3.update_layout(title='Gráfico de mapa de calor com a relação entre a marca, temporada e material')


    # Gráfico de Barras - OK
    # Cria um gráfico de baras mostrando o 'Material' mais vendidas

    fig4 = px.bar(df, x='Material_Cod', y='Qtd_Vendidos', color='Gênero', barmode="group", orientation='h',color_discrete_sequence=px.colors.qualitative.Dark24)
    fig4.update_yaxes(title_text='Código de Quantidades Vendidas')
    fig4.update_xaxes(title_text='Código do Material')
    fig4.update_layout(height=700)
    fig4.update_xaxes(tickangle=90)
    fig4.update_layout(title='Gráfico de barras mostrando o material mais vendido')

    # Gráfico pizza - OK
    # Cria um gráfico pizza mostrando a % de cada 'Temporada_Cod' vendida

    fig5 = px.pie(df, names='Temporada', color='Temporada', hole=0.2, color_discrete_sequence=px.colors.sequential.RdBu)
    fig5.update_layout(title_text='Gráfico pizza mostrando a % de cada temporada vendida')

    # Gráfico de Densidade - OK
    # Cria um gráfico ilustrando a densidade das 'Notas' dos produtos

    fig6 = px.violin(df, y='Nota', box=True, points='all')
    fig6.update_layout(title_text='Gráfico de densidade sobre as notas dos produtos')

    # Gráfico de Regressão - OK
    # Cria um gráfico de regressão com a relação entre 'Preço' e 'Desconto'

    fig7 = px.scatter(df, x='Preço', y='Desconto', size='Qtd_Vendidos_Cod', color='Qtd_Vendidos_Cod', size_max=60)
    fig7.update_layout(title_text='Gráfico de regressão entre preço e desconto')

    return fig1, fig2, fig3, fig4, fig5, fig6, fig7

# Cria função do APP
def cria_app(df):
    app = Dash(__name__)

    fig1, fig2, fig3, fig4, fig5, fig6, fig7 = cria_graficos(df)

    app.layout = html.Div([
        dcc.Graph(figure=fig1),
        dcc.Graph(figure=fig2),
        dcc.Graph(figure=fig3),
        dcc.Graph(figure=fig4),
        dcc.Graph(figure=fig5),
        dcc.Graph(figure=fig6),
        dcc.Graph(figure=fig7)
    ])
    return app

df = pd.read_csv('ecommerce_estatistica.csv')

# Cria a main
if __name__ == '__main__':
    app = cria_app(df)
    # Execute App
    app.run(debug=True, port=8050) # Default 8050