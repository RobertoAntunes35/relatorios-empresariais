

import pandas as pd 
import numpy as np 

import matplotlib.pyplot as plt 
import seaborn as sns 

import os 
import sys 

FILE_STATIC = [
    'static'
]

# diretorio_arquivo = os.path.basename()
diretorio_arquivo = os.path.abspath(FILE_STATIC[0])
file = 'Pedido_Itens.xls'

read = pd.read_excel('%s/%s' % (diretorio_arquivo, file))

print(diretorio_arquivo)















        




