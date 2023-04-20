

import pandas as pd 
import numpy as np 

import matplotlib.pyplot as plt 
import seaborn as sns 

import os 
import sys 

FILE_STATIC = {
    'arquivos_estaticos':'static'
}

# diretorio_arquivo = os.path.basename()
diretorio_arquivo = os.path.abspath(FILE_STATIC.get('arquivos_estaticos', None))

file = 'Pedidos_Itens.xls'

read = pd.read_excel(os.path.join(diretorio_arquivo, file))

# print(os.path.join(diretorio_arquivo, file))

print(read)













        




