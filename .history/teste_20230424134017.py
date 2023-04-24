import pandas as pd 
# Cria um dataframe de exemplo
df = pd.DataFrame({
    'id': [1, 2, 3],
    'nome': ['João', 'Maria', 'Pedro'],
    'idade': [25, 30, 35]
})

# Cria um dicionário vazio para armazenar os dados
dicionario = {}

# Loop for aninhado para iterar sobre as linhas e colunas do dataframe
for index, row in df.iterrows():
    # Cria um dicionário com os valores da linha atual do dataframe
    linha_dict = {}
    for coluna, valor in row.items():
        linha_dict[coluna] = valor
    # Adiciona o dicionário da linha ao dicionário geral
    dicionario[index] = linha_dict

# Imprime o dicionário resultante
print(dicionario)