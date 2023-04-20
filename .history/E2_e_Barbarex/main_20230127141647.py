

import pandas as pd 
import numpy 

import matplotlib.pyplot as plt 
import seaborn as sns 

import os 
import sys 


file_path = os.path.abspath('Pedidos_Itens.xls')

frame_geral = pd.read_excel(file_path)

# Arquivo para dezembro 

columns_dezembro = frame_geral.columns
print(columns_dezembro)







