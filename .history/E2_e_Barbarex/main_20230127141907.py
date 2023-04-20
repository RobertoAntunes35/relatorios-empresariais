

import pandas as pd 
import numpy 

import matplotlib.pyplot as plt 
import seaborn as sns 

import os 
import sys 


file_path = os.path.abspath('Pedidos_Itens.xls')

frame_geral = pd.read_excel(file_path)

# Arquivo para dezembro 

frame_dezembro = frame_geral.loc[(frame_geral['Data_Importacao'] > '01/12/2022') & (frame_geral['Data_Importacao'] < '01/01/2023')]
print(frame_dezembro)






