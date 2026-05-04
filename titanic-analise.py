import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('train.csv')

df_limpo = df.dropna()


sns.set_theme(style="whitegrid")
plt.figure(figsize=(12, 5))


plt.subplot(1, 2, 1) 
sns.countplot(data=df_limpo, x='Pclass', hue='Survived')
plt.title('Sobrevivência por Classe de Passageiro')
plt.xlabel('Classe (1ª, 2ª, 3ª)')
plt.ylabel('Quantidade de Pessoas')
plt.legend(title='Sobreviveu', labels=['Não', 'Sim'])


plt.subplot(1, 2, 2) 
sns.countplot(data=df_limpo, x='Sex', hue='Survived')
plt.title('Sobrevivência por Sexo')
plt.xlabel('Sexo')
plt.ylabel('Quantidade de Pessoas')
plt.legend(title='Sobreviveu', labels=['Não', 'Sim'])

plt.tight_layout()
plt.savefig('analise_titanic.pdf')
plt.show()