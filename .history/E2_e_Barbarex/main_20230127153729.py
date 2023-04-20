

import pandas as pd 
import numpy as np 

import matplotlib.pyplot as plt 
import seaborn as sns 

import os 
import sys 


file_path = os.path.abspath('Pedidos_Itens.xls')

frame_geral = pd.read_excel(file_path)

# Arquivo para dezembro 
rename_columns = {
    'QUANT':'quantidade_produto',
    'Texto28':'nome_produto',
    'Texto58':'valor_total',
    'Texto66':'cidade',
    'Data_Importacao':'data_importacao',
    'Texto14':'nome_cliente',
    'Combinação22':'codigo_vendedor',
    
}
frame_geral = frame_geral.rename(columns=rename_columns)


# Analise Dezembro
frame_dezembro = frame_geral.loc[(frame_geral['data_importacao'] >= '01/12/2022') & (frame_geral['data_importacao'] < '01/01/2023'), ['quantidade_produto','nome_produto','valor_total','data_importacao','codigo_vendedor']]

# Analise Janeiro
frame_janeiro = frame_geral.loc[(frame_geral['data_importacao'] >= '01/01/2023') & (frame_geral['data_importacao'] <= '26/01/2023'), ['quantidade_produto','nome_produto','valor_total','data_importacao','codigo_vendedor']]

# Codigo Vendedores
codigo_vendedores = set(np.array(frame_geral['codigo_vendedor']))

# Produtos 
produtos = set(np.array(frame_geral['nome_produto']))

suco_200_ml = []
suco_litro = []
for i in produtos:
    if '200ML' in i:
        suco_200_ml.append(i)
    else:
        suco_litro.append(i)

        




