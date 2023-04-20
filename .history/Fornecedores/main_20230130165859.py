

import pandas as pd 
import numpy as np 

import matplotlib.pyplot as plt 
import seaborn as sns 

import os 
import sys 

FILE_STATIC = {
    'arquivos_estaticos':'static'
}

diretorio_arquivos_estaticos = os.path.abspath(FILE_STATIC.get('arquivos_estaticos', None))

file_pedido_itens = 'Pedidos_Itens.xls'
file_fornecedores = 'D08_Fornecedor.xls'


# Dataframes Gerais
frame_fornecedores = pd.read_excel(os.path.join(diretorio_arquivos_estaticos, file_fornecedores))
frame_pedido_itens = pd.read_excel(os.path.join(diretorio_arquivos_estaticos, file_pedido_itens))

print(frame_fornecedores.columns)
fornecedores = {}

for codigo, fornecedor in zip(np.array(frame_fornecedores['D01_Cod_Cliente']), np.array(frame_fornecedores['D01_Fantasia'])):
    fornecedores[fornecedor] = codigo

print(fornecedores)
















        



D01_Fantasia
D01_Cod_Cliente
