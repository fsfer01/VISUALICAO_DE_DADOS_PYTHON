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

## 1º: COLUNAS COMO UMA ESPÉCIE DE DICIONÁRIO, SEGUE IMAGEM ABAIXO:
![image](https://user-images.githubusercontent.com/78058494/165187939-8954dd36-0236-4071-a228-41a392cdf5c0.png)

As colunas entities  e user estão do modo mostrado no anexo acima. Para resolver esse problema, foi utilizado a biblioteca flatten_json para gerar outra tabela de dados através dessas colunas. Segue link da biblioteca e de sua documentação abaixo:

link: https://github.com/amirziai/flatten

![image](https://user-images.githubusercontent.com/78058494/165192557-cbc012c2-fb71-43fb-8a10-1764927b2de9.png)

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

