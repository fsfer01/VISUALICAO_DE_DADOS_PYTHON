# VISUALIZAÇÃO DE DADOS COM PYTHON

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

## 2º: ADICIONANDO CHAVE PRIMÁRIA EM OUTRAS TABELAS PARA CRUZAMENTOS FUTUROS.
![image](https://user-images.githubusercontent.com/78058494/165651768-f78bb241-90eb-429c-b7e2-67d1438a0766.png)

## 3º: DATA EM FORMATO AMERICANO E EXTENSO.
![image](https://user-images.githubusercontent.com/78058494/166162213-46d48ad2-37db-4c78-9671-f8c5755466e9.png)

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

Gráfico de Linha:
![image](https://user-images.githubusercontent.com/78058494/171269835-d8820e3f-305d-47d2-9807-e88babd2ce61.png)

Mapa de calor:
![image](https://user-images.githubusercontent.com/78058494/171269915-31bc8631-bf04-4575-bf42-d6efba6f7db7.png)

