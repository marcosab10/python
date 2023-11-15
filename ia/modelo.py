# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session

# Leitura dos arquivos CSV
train_data = pd.read_csv('/kaggle/input/playground-series-s3e5/train.csv')
test_data = pd.read_csv('/kaggle/input/playground-series-s3e5/test.csv')


# Exibindo as primeiras linhas dos dados de treino (opcional)
print("Dados de Treino:")
train_data.head(2)

# Exibindo as primeiras linhas dos dados de teste (opcional)
print("\nDados de Teste:")
test_data.head(2)

len(test_data)


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Separando os dados em características (X) e rótulo (y)
X = train_data.drop('quality', axis=1)  # Características
y = train_data['quality']  # Rótulo

# Dividindo os dados em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criando o modelo de regressão linear
model = LinearRegression()

# Treinando o modelo
model.fit(X_train, y_train)


# Fazendo predições no conjunto de teste
y_pred = model.predict(X_test)

# Avaliando o desempenho do modelo
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print('-----------------------------------------------------------------------------')
print(f'Mean Squared Error (MSE): {mse}')
print(f'R-squared (R2): {r2}')
print('-----------------------------------------------------------------------------')


# Visualizando a qualidade das predições
plt.scatter(y_test, y_pred)
plt.xlabel('True Quality')
plt.ylabel('Predicted Quality')
plt.title('True Quality vs Predicted Quality')
plt.show()