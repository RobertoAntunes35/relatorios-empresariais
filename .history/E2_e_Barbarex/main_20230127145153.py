

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
print(frame_geral)

# frame_dezembro = frame_geral.loc[(frame_geral['Data_Importacao'] > '01/12/2022') & (frame_geral['Data_Importacao'] < '01/01/2023'), ['quantidade']]
# print(frame_dezembro)






