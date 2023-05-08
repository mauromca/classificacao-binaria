from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Carrega os dados de câncer de mama
dados = load_breast_cancer()

# Define as features e os rótulos
X = dados.data
y = dados.target

# Separa os dados em treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Cria o modelo SVM
model = SVC(kernel='linear')

# Treina o modelo
model.fit(X_train, y_train)

# Realiza a predição no conjunto de teste
y_pred = model.predict(X_test)

# Calcula a acurácia do modelo
accuracy = accuracy_score(y_test, y_pred)

# Imprime a acurácia
print(f'Acurácia: {accuracy:.2f}')
