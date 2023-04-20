

import pandas as pd 
import numpy as np 

import matplotlib.pyplot as plt 
import seaborn as sns 

import os 
import sys 



file_path = os.path.abspath('static')
arquivo_fornecedores = 'D08_Fornecedores.xls'


fornecedores = pd.read_excel(f'{file_path}\{arquivo_fornecedores}')

print(fornecedores)














        




