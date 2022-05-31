# VISUALIZAÇÃO DE DADOS COM PYTHON

![GITHUB (1)](https://user-images.githubusercontent.com/78058494/171275250-0287faa7-4265-4c20-9bbd-08a9358a0db5.gif)

Um projeto público simples para demonstrar meu conhecimento na área de dados. O Objetivo deste projeto é:

• Ler um CSV

• Modelar os dados necessários

• Criar gráficos em cima dos dados disponíveis.

# TECNOLOGIAS USADAS:

• PYTHON

• Plotly Express - LINK DA DOCUMENTAÇÃO: [Documentação Plotly Express](https://plotly.com/python/plotly-express/)

# REQUISITOS:

Para conseguir rodar esse código localmente, será necessário instalar algumas bibliotecas! Execute os seguintes comandos abaixo:

```python
pip install pandas
pip install plotly-express
pip install numpy
```
# DESAFIOS:

## 1º: COLUNAS COM NAN:
![image](https://user-images.githubusercontent.com/78058494/171271989-77470313-63a8-4d6d-ac45-875ccc0bd6c0.png)


A coluna city_ibge_code tem várias regristros NAN, e por causa desses registros, não é possível converter a coluna para o tipo inteiro. Então, com o código abaixo, conseguimos substituir os NAN por 0, e após isso, conseguimos normalmente converter a coluna para o tipo inteiro.

```python
tabela['city_ibge_code'] = tabela['city_ibge_code'].replace(np.nan, 0) #CONVERTENDO TODOS OS VALORES NAN POR 0
tabela['city_ibge_code'] = tabela['city_ibge_code'].astype(int) #CONVERTE TODA A COLUNA EM INTEIRO
```

## 2º: CRIANDO UM SEGUNDO DF AGRUPADO PARA CRIAR O GRÁFICO DE LINHAS:
![image](https://user-images.githubusercontent.com/78058494/171273065-71117c05-eab0-4a0a-aa33-f4d3ad497901.png)


Para criar um gráfico de linhas, foi necessário criar um segundo DF agrupando as datas e mortes. Segue código abaixo:
```python
Data_Mortes = tabela[['date','deaths']] #Criando o dataframe com colunas especificas
Dados_tratados = Data_Mortes.groupby('date',as_index=False)[['date','deaths']].sum()#agrupando os dados, e evitando a contatenação e fazendo a soma dos dados
df_agrupado = Dados_tratados #passando os dados para o data Frame
```
Após criar o segundo DF agrupado como mostrado acima, vamos plotar o gráfico utilizando o código abaixo:
```python
graficolinha = px.line(df_agrupado, x="date", y="deaths", title='MORTES POR PERÍODO')
graficolinha.update_yaxes(title = "MORTES POR COVID-19") #altera o nome do eixo Y
graficolinha.update_xaxes(title = "PERÍODO")#altera o nome do eixo X
graficolinha.show()
```
Após isso, segue resultado abaixo:

![image](https://user-images.githubusercontent.com/78058494/171269835-d8820e3f-305d-47d2-9807-e88babd2ce61.png)


## 3º: CRUZANDO UM DF COM OUTRO PARA PEGAR O NOME CORRETO DOS ESTADOS ATRAVÉS DA COLUNA city_ibge_code
![image](https://user-images.githubusercontent.com/78058494/171277899-0ea38259-9527-451c-a439-ddbe4396ace7.png)

No DF casos, não temos os nomes dos estados em um formato apropriado para que o gráfico seja plotado corretamente, para isso, vamos cruzar com outro DF para pegar o nome correto dos estados. Segue código e explicação abaixo:

```python
#CRUZAMENTO DE BASES - IGUAL AO PROCV NO EXCEL
base1 = ibge[['Códigos','UFs']]#LENDO COLUNAS ESPECÍFICAS
#FAZENDO PROCV
nova_base = tabela.merge(base1, left_on='city_ibge_code', right_on='Códigos', how='left')
```

Podemos ver que criamos um DF temporário chamado base1, ele será usado como base para o cruzamento. Após isso, vamos fazer o merge, que é o cruzamento entre as bases. Vamos usar a coluna city_ibge_code que está no DF casos como chave de pesquisa e cruzar com a coluna Códigos que está no DF base1, e o termo left é da esquerda para direita, vai ficar melhor o entendimento vendo o resultado abaixo:

![image](https://user-images.githubusercontent.com/78058494/171280571-b9c66103-9fe0-4a54-9241-4d5b7b95ba5e.png)

E após isso, conseguimos criar o gráfico geográfico usando o código abaixo:

```python
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
```

E o resultado será:

![image](https://user-images.githubusercontent.com/78058494/171269915-31bc8631-bf04-4575-bf42-d6efba6f7db7.png)

4º: GRÁFICO DE BARRAS:

Esse gráfico foi simples, só executar o código abaixo:

```python
#passa os dados dos ESTADOS BRASILEIROS(states) e a QUANTIDADE DE CASOS CONFIRMADOS(confirmed)
graficobarra = px.histogram(tabela, x="state", y="confirmed", color="state", 
                       title="TOTAL DE CASOS DE COVID-19 POR ESTADOS BRASILEIROS").update_xaxes(categoryorder="total ascending")
graficobarra.update_yaxes(title = "TOTAL DE CASOS POR ESTADO") #altera o nome do eixo Y
graficobarra.update_xaxes(title = "CASOS CONFIRMADOS POR ESTADO")#altera o nome do eixo X
graficobarra.show() #Mostra o grafico completo
```

Segue resultados abaixo:

![image](https://user-images.githubusercontent.com/78058494/171269794-5f53e2bc-b7db-4dff-b6cb-32b075f4d473.png)

Data da ultima atualização: 31/05/2022.



