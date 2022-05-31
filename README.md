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

Código abaixo:

```python
#CONVERTENDO DATA NO DATAFRAME:
import locale; locale.setlocale(locale.LC_TIME, 'en_US.UTF-8'); 
dfTweetstabelao['created_at'] = pd.to_datetime(dfTweetstabelao['created_at'], format='%a %b %d %H:%M:%S %z %Y').dt.strftime('%Y-%m-%d %H:%M:%S')

#CONVERTENDO A COLUNA PARA DATA
dfTweetstabelao['created_at'] = pd.to_datetime(dfTweetstabelao['created_at']) # TRANFORMANDO COLUNA DE STRING PARA DATATIME BR
dfTweetstabelao['created_at'] = dfTweetstabelao['created_at']-timedelta(hours=3) #SUBTRAINDO 3 HORAS (CONVERTENDO UTC PARA BR)
```














Segue resultados abaixo:

Gráfico de barras:
![image](https://user-images.githubusercontent.com/78058494/171269794-5f53e2bc-b7db-4dff-b6cb-32b075f4d473.png)



Mapa de calor:
![image](https://user-images.githubusercontent.com/78058494/171269915-31bc8631-bf04-4575-bf42-d6efba6f7db7.png)

