

import pandas as pd 
import numpy 

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
frame_dezembro = frame_geral.loc[(frame_geral['data_importacao'] > '01/12/2022') & (frame_geral['data_importacao'] < '01/01/2023'), ['quantidade_produto','nome_produto','valor_total','data_importacao','codigo_vendedor']]
# print(frame_dezembro)

# Analise Janeiro
frame_janeiro = frame_geral.loc[(frame_geral['data_importacao'] > '01/01/2023') & (frame_geral['data_importacao'] <= '27/01/2023'), ['quantidade_produto','nome_produto','valor_total','data_importacao','codigo_vendedor']]
print('JANEIRO\n%s' % frame_janeiro['nome_produto'].value_counts().reset_index())









