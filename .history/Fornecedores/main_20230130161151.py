

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


frame_pedido_itens = pd.read_excel(os.path.join(diretorio_arquivos_estaticos, file_pedido_itens))

frame_fornecedores = pd.read_excel(os.path.join(diretorio_arquivos_estaticos, file_fornecedores))
# print(os.path.join(diretorio_arquivo, file))

print(frame_fornecedores)













        




