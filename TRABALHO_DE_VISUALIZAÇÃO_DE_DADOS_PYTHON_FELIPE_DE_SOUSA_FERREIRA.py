#!/usr/bin/env python
# coding: utf-8

# # IMPORTANDO BIBLIOTÉCAS NECESSÁRIAS PARA RODAR O CÓDIGO:

# In[1]:


import pandas as pd #IMPORTANDO O PANDAS PARA LEITURA E TRATAMENTO DO DF
import plotly.express as px #BIBLIOTÉCA PARA CRIAÇÃO DOS GRÁFICOS.
import numpy as np


# In[2]:


tabela = pd.read_csv("caso.csv") #LENDO O DF.


# ## FAZENDO MODELAGEM DOS DADOS:

# In[3]:


tabela['city_ibge_code'] = tabela['city_ibge_code'].replace(np.nan, 0) #CONVERTENDO TODOS OS VALORES NAN POR 0
tabela['city_ibge_code'] = tabela['city_ibge_code'].astype(int) #CONVERTE TODA A COLUNA EM INTEIRO


# # CRIANDO GRÁFICO DE BARRAS

# In[4]:


#passa os dados dos ESTADOS BRASILEIROS(states) e a QUANTIDADE DE CASOS CONFIRMADOS(confirmed)
graficobarra = px.histogram(tabela, x="state", y="confirmed", color="state", 
                       title="TOTAL DE CASOS DE COVID-19 POR ESTADOS BRASILEIROS").update_xaxes(categoryorder="total ascending")
graficobarra.update_yaxes(title = "TOTAL DE CASOS POR ESTADO") #altera o nome do eixo Y
graficobarra.update_xaxes(title = "CASOS CONFIRMADOS POR ESTADO")#altera o nome do eixo X
graficobarra.show() #Mostra o grafico completo


# ## CRIANDO GRÁFICO DE LINHAS:
# 

# In[5]:


Data_Mortes = tabela[['date','deaths']] #Criando o dataframe com colunas especificas
Dados_tratados = Data_Mortes.groupby('date',as_index=False)[['date','deaths']].sum()#agrupando os dados, e evitando a contatenação e fazendo a soma dos dados
df_agrupado = Dados_tratados #passando os dados para o data Frame


# In[12]:


graficolinha = px.line(df_agrupado, x="date", y="deaths", title='MORTES POR PERÍODO')
graficolinha.update_yaxes(title = "MORTES POR COVID-19") #altera o nome do eixo Y
graficolinha.update_xaxes(title = "PERÍODO")#altera o nome do eixo X
graficolinha.show()


# # GRÁFICO GEOGRÁFICO

# In[7]:


#CRUZANDO UM DF COM O DF ABAIXO:
ibge = pd.read_csv("estados.csv",encoding='latin-1') #LENDO O DF.


# In[8]:


#CRUZAMENTO DE BASES - IGUAL AO PROCV NO EXCEL
base1 = ibge[['Códigos','UFs']]#LENDO COLUNAS ESPECÍFICAS
#FAZENDO PROCV
nova_base = tabela.merge(base1, left_on='city_ibge_code', right_on='Códigos', how='left')
#nova_base.drop('primeira_coluna', axis = 1, inplace = True) #RETIRANDO COLUNA ['primeira_coluna']


# In[9]:


#CRIANDO UM NOVO DF AGRUPADO POR ESTADOS.
df1 = nova_base[['UFs','deaths']] #Criando o dataframe com colunas especificas
estado = df1.groupby('UFs',as_index=False)[['UFs','deaths']].sum()#agrupando os dados, e evitando a contatenação e fazendo a soma dos dados


# In[10]:


import json
with open('estados_brasil.geojson') as data: # carregando o arquivo ".geojson"
    limites_brasil = json.load(data)
    
for feature in limites_brasil ['features']: # adicionado o ID aos dados
    feature['id'] = feature['properties']['name']


# In[11]:


fig = px.choropleth_mapbox(
    estado, # data frame com os dados
    locations = "UFs", # coluna com o ID, neste caso, o
    geojson = limites_brasil, # arquivo com os limites do mapa
    color = "deaths", # coluna do data frame para os valores reais
    mapbox_style = "carto-positron", # define o estilo do mapa
    center={"lat":-14, "lon": -55}, # define a posição do mapa que será gerado
    zoom = 3, # zoom inicial
    opacity = 0.5, # adiciona opacidade para que apareça o fundo
)
fig.show()

