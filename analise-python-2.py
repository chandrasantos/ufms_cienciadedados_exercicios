import pandas as pd  


df = pd.read_csv('train.csv')


df_limpo = df.dropna()


media = df_limpo['Age'].mean()
mediana = df_limpo['Age'].median()
desvio_padrao = df_limpo['Age'].std()
minimo = df_limpo['Age'].min()
maximo = df_limpo['Age'].max()

# Exibindo os cálculos individuais
print("--- Estatísticas Individuais (Idade) ---")
print(f"Média: {media:.2f}")
print(f"Mediana: {mediana:.2f}")
print(f"Desvio Padrão: {desvio_padrao:.2f}")
print(f"Mínimo: {minimo}")
print(f"Máximo: {maximo}")
print("-" * 40)

resumo_estatistico = df_limpo.describe()

print("\n--- Resumo Estatístico ---")
print(resumo_estatistico)