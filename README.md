## Calassificação Binária

### Conjunto de dados de câncer de mama:

**A classificação binária** é uma tarefa importante em aprendizado de máquina e tem muitas aplicações práticas, desde diagnósticos médicos até previsões financeiras. Neste código, vou apresentar um algoritmo de classificação binária usando o conjunto de dados de câncer de mama disponível no repositório da biblioteca Scikit-Learn.

**O conjunto de dados de câncer de mama** é composto por 569 amostras de tecido mamário, cada uma com 30 características. As características incluem o raio, textura, perímetro, área, suavidade, compacidade, concavidade, pontos côncavos, simetria e dimensão fractal dos núcleos celulares. Cada amostra é rotulada como "maligna" ou "benigna", tornando-o um conjunto de dados de classificação binária.

**Nesse algoritmo de classificação binária** começa importando as bibliotecas necessárias, incluindo o conjunto de dados de câncer de mama usando a biblioteca Scikit-Learn. Em seguida, dividimos o conjunto de dados em um conjunto de treinamento e um conjunto de teste, usando a função `train_test_split`. Depois disso, normalizamos os dados usando a função `StandardScaler` para garantir que cada característica tenha uma escala comparável.

**O próximo passo é criar um modelo de classificação usando o algoritmo de Máquina de Vetores de Suporte (SVM)** linear, que é uma técnica popular em aprendizado de máquina para problemas de classificação binária. Em seguida, treinamos o modelo usando o conjunto de treinamento e avaliamos sua precisão usando o conjunto de teste.

**Finalmente, usamos o modelo treinado para fazer previsões** em um conjunto de dados de teste separado e avaliamos a precisão do modelo usando a métrica de acurácia.

**Em resumo**, o algoritmo de classificação binária usando o conjunto de dados de câncer de mama ilustra uma aplicação prática de aprendizado de máquina em um problema real. A biblioteca Scikit-Learn oferece muitas funções e algoritmos úteis para a análise de dados, e o conjunto de dados de câncer de mama é uma fonte valiosa para o desenvolvimento e teste de algoritmos de classificação binária.

Lista de Processos:

1. **Importação das bibliotecas** necessárias (load_breast_cancer, train_test_split, SVC e accuracy_score) através do comando "from sklearn".
2. **Carregamento dos dados** de câncer de mama através do comando "load_breast_cancer()" e armazenamento na variável "dados".
3. **Definição das features** (X) e dos rótulos (y) através das propriedades "data" e "target" da variável "dados".
4. **Separação dos dados** em conjuntos de treinamento e teste (X_train, X_test, y_train e y_test) utilizando a função "train_test_split". A separação é feita de forma aleatória, com 20% dos dados reservados para teste.
5. **Criação de um modelo SVM** com kernel linear através do comando "SVC(kernel='linear')", armazenando na variável "model".
6. **Treinamento do modelo** com o conjunto de treinamento através do comando "model.fit(X_train, y_train)".
7. **Realização da predição** dos rótulos de teste através do comando "model.predict(X_test)" e armazenamento na variável "y_pred".
8. **Cálculo da acurácia** do modelo utilizando a função "accuracy_score(y_test, y_pred)" e armazenamento na variável "accuracy".
9. **Impressão da acurácia** na tela utilizando o comando "print(f'Acurácia: {accuracy:.2f}')".
