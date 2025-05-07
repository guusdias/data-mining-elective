import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# criando o dataset
np.random.seed(42)
n_amostras = 1000
renda_mensal = np.random.normal(5, 2, n_amostras)
idade = np.random.normal(35, 10, n_amostras)
score_credito = np.random.uniform(0, 100, n_amostras)
probabilidade = 1 / (1 + np.exp(-(0.5 * renda_mensal + 0.03 * score_credito - 0.1 * idade)))
contratou_emprestimo = np.random.binomial(1, probabilidade)

dataset = pd.DataFrame({
    'Renda_Mensal': renda_mensal,
    'Idade': idade,
    'Score_Credito': score_credito,
    'Contratou_Emprestimo': contratou_emprestimo
})

dataset.to_csv('dataset_emprestimo_1000.csv', index=False)
print("Dataset gerado e salvo como 'dataset_emprestimo_1000.csv'")
print(dataset.head())

# treinando o modelo
X = dataset[['Renda_Mensal', 'Idade', 'Score_Credito']]
y = dataset['Contratou_Emprestimo']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) # (80% treino, 20% teste)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

modelo = LogisticRegression(random_state=42)
modelo.fit(X_train_scaled, y_train)

y_pred = modelo.predict(X_test_scaled)

acuracia = accuracy_score(y_test, y_pred)
print(f'\nAcurácia do modelo: {acuracia:.2f}')

matriz_confusao = confusion_matrix(y_test, y_pred)
print('\nMatriz de Confusão:')
print(matriz_confusao)

relatorio = classification_report(y_test, y_pred)
print('\nRelatório de Classificação:')
print(relatorio)

print('Coeficientes do modelo:', modelo.coef_)
print('Intercepto:', modelo.intercept_)