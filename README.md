## Calassificação Binária

### Conjunto de dados de câncer de mama:

**A classificação binária** é uma tarefa importante em aprendizado de máquina e tem muitas aplicações práticas, desde diagnósticos médicos até previsões financeiras. Neste código, vou apresentar um algoritmo de classificação binária usando o conjunto de dados de câncer de mama disponível no repositório da biblioteca Scikit-Learn.

**O conjunto de dados de câncer de mama** é composto por 569 amostras de tecido mamário, cada uma com 30 características. As características incluem o raio, textura, perímetro, área, suavidade, compacidade, concavidade, pontos côncavos, simetria e dimensão fractal dos núcleos celulares. Cada amostra é rotulada como "maligna" ou "benigna", tornando-o um conjunto de dados de classificação binária.

**Nesse algoritmo de classificação binária** começa importando as bibliotecas necessárias, incluindo o conjunto de dados de câncer de mama usando a biblioteca Scikit-Learn. Em seguida, dividimos o conjunto de dados em um conjunto de treinamento e um conjunto de teste, usando a função `train_test_split`. Depois disso, normalizamos os dados usando a função `StandardScaler` para garantir que cada característica tenha uma escala comparável.

**O próximo passo é criar um modelo de classificação usando o algoritmo de Máquina de Vetores de Suporte (SVM)** linear, que é uma técnica popular em aprendizado de máquina para problemas de classificação binária. Em seguida, treinamos o modelo usando o conjunto de treinamento e avaliamos sua precisão usando o conjunto de teste.

**Finalmente, usamos o modelo treinado para fazer previsões** em um conjunto de dados de teste separado e avaliamos a precisão do modelo usando a métrica de acurácia.

**Em resumo**, o algoritmo de classificação binária usando o conjunto de dados de câncer de mama ilustra uma aplicação prática de aprendizado de máquina em um problema real. A biblioteca Scikit-Learn oferece muitas funções e algoritmos úteis para a análise de dados, e o conjunto de dados de câncer de mama é uma fonte valiosa para o desenvolvimento e teste de algoritmos de classificação binária.

### Segue abaixo a lista das etapas realizadas no algoritmo de classificação binária utilizando SVM:

1. Importação da biblioteca Scikit-Learn do Python.
2. Carregamento do dataset Breast Cancer.
3. Definição das variáveis X e y, onde X é um array com as informações das características das células cancerosas e y é um array com as informações sobre a natureza do tumor (benigno ou maligno).
4. Divisão dos dados em conjuntos de treinamento e teste, utilizando a função train_test_split da biblioteca Scikit-Learn.
5. Importação da classe SVC (Support Vector Classification) da biblioteca Scikit-Learn.
6. Criação de um objeto model da classe SVC com kernel linear.
7. Treinamento do modelo com os dados de treinamento utilizando o método fit.
8. Utilização do modelo treinado para fazer previsões em dados de teste, utilizando o método predict.
9. Cálculo da acurácia do modelo, utilizando a função accuracy_score da biblioteca Scikit-Learn.
10. Impressão do valor da acurácia.
