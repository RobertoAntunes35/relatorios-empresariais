

import pandas as pd 
import numpy as np 

import matplotlib.pyplot as plt 
import seaborn as sns 

import os 
import sys 

file_path = os.path.abspath('New_Suco_Itens.xls')
print(file_path)


# frame_geral = pd.read_excel(file_path)

# # Arquivo para dezembro 
# rename_columns = {
#     'QUANT':'quantidade_produto',
#     'Texto28':'nome_produto',
#     'Texto58':'valor_total',
#     'Texto66':'cidade',
#     'Data_Importacao':'data_importacao',
#     'Texto14':'nome_cliente',
#     'Combinação22':'codigo_vendedor',
    
# }
# frame_geral = frame_geral.rename(columns=rename_columns)

# # Analise Dezembro
# frame_dezembro = frame_geral.loc[(frame_geral['data_importacao'] >= '01/12/2022') & (frame_geral['data_importacao'] < '01/01/2023'), ['quantidade_produto','nome_produto','valor_total','data_importacao','codigo_vendedor']]

# # Analise Janeiro
# frame_janeiro = frame_geral.loc[(frame_geral['data_importacao'] >= '01/01/2023') & (frame_geral['data_importacao'] <= '26/01/2023'), ['quantidade_produto','nome_produto','valor_total','data_importacao','codigo_vendedor']]

# # Codigo Vendedores
# codigo_vendedores = set(np.array(frame_geral['codigo_vendedor']))

# # Produtos 
# produtos = set(np.array(frame_geral['nome_produto']))

# # Quantidade Produtos Janeiro
# dict_produtos_quantidade_janeiro = {}
# dict_produtos_quantidade_dezembro = {}

# for produto in produtos:
#     quantidade_produto_janeiro = sum(frame_janeiro.loc[frame_janeiro['nome_produto'] == produto]['quantidade_produto'])
#     dict_produtos_quantidade_janeiro[produto] = quantidade_produto_janeiro

# for produto in produtos:
#     quantidade_produto_dezembro = sum(frame_dezembro.loc[frame_dezembro['nome_produto'] == produto]['quantidade_produto'])
#     dict_produtos_quantidade_dezembro[produto] = int(quantidade_produto_dezembro)


# # Gráfico: Produtos Geral
# df_produtos_geral_dezembro = pd.DataFrame.from_dict(dict_produtos_quantidade_dezembro, orient='index', columns=['Quantidade']).reset_index().rename(columns={
#     'index':'Produtos'
# })

# # Dezembro
# df_produtos_geral_dezembro = df_produtos_geral_dezembro.sort_values(by='Quantidade', ascending=False)
# print(df_produtos_geral_dezembro)
# sns.barplot(
#     x='Quantidade',
#     y='Produtos', 
#     data = df_produtos_geral_dezembro)
# plt.show()

# # Janeiro 
# df_produtos_geral_janeiro = pd.DataFrame.from_dict(
#     dict_produtos_quantidade_janeiro, 
#     orient='index', 
#     columns=['Quantidade']).reset_index().rename(
#         columns={
#         'index':'Produtos'
# })

# sns.barplot(
#     x='nome_produto',
#     y='quantidade',
#     data=df_produtos_geral_janeiro
# )

# Gráfico: Positivação por Cidade



# Gráfico: Ranking Clientes















        




