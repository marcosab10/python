import os
import sys
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

caminho_do_arquivo = os.path.abspath(sys.argv[0])
diretorio_dos_arquivos = os.path.dirname(caminho_do_arquivo)

print("Caminho do arquivo:", caminho_do_arquivo)
print("Diretório do arquivo:", diretorio_dos_arquivos)


for dirname, _, filenames in os.walk(diretorio_dos_arquivos ):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session

# Leitura dos arquivos CSV
train_data = pd.read_csv(diretorio_dos_arquivos + '\\playground-series-s3e5\\train.csv')
test_data = pd.read_csv(diretorio_dos_arquivos + '\\playground-series-s3e5\\test.csv')


# Exibindo as primeiras linhas dos dados de treino (opcional)
print("Dados de Treino:")
train_data.head(2)

# Exibindo as primeiras linhas dos dados de teste (opcional)
print("\nDados de Teste:")
test_data.head(2)

len(test_data)
