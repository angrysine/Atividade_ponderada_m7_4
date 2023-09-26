# Ponderada 3 - Alberto

## modelo

Foi utilizado o dataset do kaggle de customer segmentation, que pode ser encontrado [aqui](https://www.kaggle.com/vjchoudhary7/customer-segmentation-tutorial-in-python). Um label encoding foi aplicado na coluna "Gender" e renomeamos a coluna "Annual Income (k$)" para Income. O dataset foi dividido em 80% para treino e 20% para teste usando o Sklearn. A coluna de resposta escolhida foi Spending Score (1-100), que é uma pontuação de 1 a 100 que o shopping dá para cada cliente com base em seus comportamentos e natureza de compra. O modelo foi escolhido usando pycaret, que é uma biblioteca de machine learning que automatiza o processo de treino e teste de vários modelos. O modelo escolhido foi o LGBMRegressor. Foi usada a função create_api para gerar nosso backend.

## API

temos duas rotas na api que se encontra em <http://localhost:5000>

### / (get)

retorna um json com a mensagem "API is working!".

### /predict (post)

recebe um json com os dados de entrada e retorna um json com a resposta do modelo. segue aqui um exemplo de input:

```python
{"CustomerID": 82, "Gender": 0, "Age": 38, "Income": 54}
```

e um exemplo de output:

```python
{"prediction": 51.0}
```

## Docker

Para rodar o docker, basta rodar o comando:

```bash
docker run -p 5000:5000 angrysine/ponderada3
```

## Estrutura do projeto

.
├── app.py
├── archive
│   └── Mall_Customers.csv
├── Dockerfile
├── model.ipynb
├── read.md
├── requirements.txt
├── teste_api.pkl
├── teste_api.py
└── teste.txt

## Vídeo 

