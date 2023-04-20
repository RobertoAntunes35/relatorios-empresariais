import importlib.util 

spec = importlib.util.spec_from_file_location('frame_excel', 'C:/Users/marcelo/Desktop/projetos-em-andamento/controle-estoque/libs/frame_excel.py')
foo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(foo)

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import PyPDF2 as pdf 
import seaborn as sns
from copy import deepcopy
import datetime


import sys 
import os  
import copy
from time import sleep
from config import analise_dados, path, FILE_CLIENTES, FILE_PEDIDO_ITENS, FILE_STATIC

from config import vendedores



class Clientes(foo.Excel):
    def __init__(self, nome_arquivo, **columns_select):
        super().__init__(nome_arquivo, **columns_select)

    def filtroClientes(self, vendedor):
        pass 




class FornecedoresFiltro:

    def __init__(self, caminhoArquivo, listaFornecedores, **columns) -> None:
        self.frame_geral = pd.read_excel(caminhoArquivo)
        self.listaFornecedores = listaFornecedores
        self.new_frame = self.frame_geral.rename(columns=columns)
        
    def frameFiltradoPorDiaAnalise(self):
        if isinstance(self.listaFornecedores, list): 
            filtros = []
            dfs = {}
            for fornecedor in self.listaFornecedores:
                dfs[fornecedor] = self.new_frame.loc[self.new_frame['fornecedor'] == fornecedor]
                filtros.append(dfs)
            return pd.concat(dfs.values())

class RelatorioDestinado(FornecedoresFiltro):

    def __init__(self, caminhoArquivo, listaFornecedores, **columns) -> None:
        super().__init__(caminhoArquivo, listaFornecedores, **columns)
    
        self._matriz_dados = self.frameFiltradoPorDiaAnalise()

    def sumRelatorio(self, coluna_filtro, coluna_soma, valor_filtro, frame):
        return round(frame.loc[frame[coluna_filtro] == valor_filtro][coluna_soma].sum(), 3)
    
    def transformarDataFrameEmExcel(self, data_frame, nome_arquivo):
        return data_frame.to_excel(nome_arquivo)

    def faturamentoFornecedor(self, valor_filtro:str):
        dict_venda_fornecedor = dict()
        venda = dict()
        
        if isinstance(self._matriz_dados, pd.DataFrame):
            condicional_filtro = set(np.array(self._matriz_dados[valor_filtro]))
            for fornecedor in self.listaFornecedores:
                frame_analise = self._matriz_dados.loc[self._matriz_dados['fornecedor'] == fornecedor]
                for filtro in condicional_filtro:
                    venda[filtro] = self.sumRelatorio(valor_filtro, 'valor_venda_produto', filtro, frame_analise)
                dict_venda_fornecedor[fornecedor] = dict(sorted(venda.items(), key = lambda x: x[1]))
            
            return pd.DataFrame(dict_venda_fornecedor)

    def positivacaoDeProdutoPorCliente(self, clientesGeral:pd.DataFrame):
        clientes_nao_positivados = []
        dfs = {}
        
        clientesPositivados = np.array(self.frameFiltradoPorDiaAnalise()['nome_fantasia'])
        
        for cliente in np.array(clientesGeral['nome_fantasia']):
            if cliente not in clientesPositivados:
                dfs[cliente] = clientesGeral.loc[clientesGeral['nome_fantasia'] == cliente]
                clientes_nao_positivados.append(dfs)
            
        return pd.concat(dfs.values())

    def quantidadeProdutoPorValor(self, menor_valor: float, maior_valor: float, diferente = None):
        dict_produto = {}
        matriz_informacao = copy.deepcopy(self._matriz_dados)

        if diferente is not None:
            self.frame_analise = matriz_informacao.loc[
                (matriz_informacao['valor_venda_fardo'] >= menor_valor) & 
                (matriz_informacao['valor_venda_fardo'] <= maior_valor) & 
                (matriz_informacao['valor_venda_fardo'] != diferente)]
        else:
            self.frame_analise = matriz_informacao.loc[
                (matriz_informacao['valor_venda_fardo'] >= menor_valor) & 
                (matriz_informacao['valor_venda_fardo'] <= maior_valor)]

        for clientes_desconto in analise_dados.get('clientes_com_desconto_financeiro'):
            if clientes_desconto in np.array(self.frame_analise['nome_fantasia']):
                filtro = self.frame_analise['nome_fantasia'] == clientes_desconto
                self.frame_analise.loc[filtro, 'valor_venda_fardo'] *=0.97

        for produto in np.array(self.frame_analise['produtos'].drop_duplicates()):
            dict_produto[produto] = self.sumRelatorio('produtos', 'quantidade', produto,self.frame_analise)
        dict_produto = dict(sorted(dict_produto.items(), key=lambda x: x[0]))
        return pd.DataFrame(dict_produto.items()).rename(columns={0:'Produtos', 1:'Quantidade'})
        
    def dadosFiltradosParaVendedores(self, data_inicial: str, data_final: str, vendedor: int):
        dados = deepcopy(self._matriz_dados)
        frame_filtrado = dados.loc[(dados['codigo_vendedor'] == vendedor) & (dados['data_importacao'] >= data_inicial) & (dados['data_importacao'] <= data_final)]
        return frame_filtrado
    
    def clientesPositivados(self, data_inicial: str, data_final: str, vendedor: int):
        dados = self.dadosFiltradosParaVendedores(data_inicial, data_final, vendedor)
        clientesPositivados = set(np.array(dados['nome_fantasia'])) 
        return len(clientesPositivados)

    def faturamentoMensalVendedor(self, data_inicial: str, data_final: str, vendedor: int):
        dados = self.dadosFiltradosParaVendedores(data_inicial, data_final, vendedor)
        faturamentoMensal = dados['valor_venda_produto'].sum()
        return faturamentoMensal



class AnaliseGeralVendedores(foo.Excel):
    
    def __init__(self, nome_arquivo: str, codigosVendedor: list, inicio_mes_analise: str, **columns_select) -> None:
        super().__init__(nome_arquivo, **columns_select)
        self._codigoVendedor = codigosVendedor
        
        try:
            data = datetime.date.strftime(inicio_mes_analise, "Y%-%m-%d")
            self._inicioMesAnalise = data.replace(day=1)
        except:
            raise TypeError("Erro ao formatar a data de entrada como um tipo de data, informe a data da seguinte forma: YEAR-MONTH-DAY")
        
        self._finalMesAnalise = (datetime.date(self._inicioMesAnalise.year, self._inicioMesAnalise.month + 1, 1) - datetime.timedelta(days=1))

        
        if not isinstance(self._codigoVendedor, list):
            raise TypeError("Atribua uma lista de informações.")

        if len(self._codigoVendedor) == 0:
            raise ValueError("Atribua ao menos um codigo de vendedor para iniciar a analise") 

        for codVendedor in self._codigoVendedor:
            if codVendedor not in vendedores.values():
                raise ValueError("O código %s não está na listagem de vendedores cadastrados." % codVendedor)
    



    @property
    def codigoVendedor(self):
        return self._codigoVendedor
    
    @codigoVendedor.setter
    def codigoVendedor(self, newValue):
        
        if newValue not in vendedores.values() or not isinstance(newValue, int):
            raise ValueError("O valor a ser incluso, não é de um vendedor cadastrado.")
        self._codigoVendedor.append(newValue)


    @property
    def mesAnalise(self):
        return self._inicioMesAnalise
    
    



if __name__ == '__main__':

    arquivo_pedido_itens = os.path.join(path, FILE_PEDIDO_ITENS)
    arquivo_clientes = os.path.join(path, FILE_CLIENTES)



    rename_file_pedidoItens = {
        'Combinação47':'fornecedor',
        'Texto66':'cidades',
        'Texto28':'produtos',
        'Combinação22':'codigo_vendedor',
        'Vl_Prod':'valor_venda_produto',
        'Texto14':'nome_fantasia',
        'Texto45':'valor_custo_produto',
        'Texto73':'valor_venda_fardo',
        'QUANT':'quantidade',
        'Data_Importacao':'data_importacao'
    }

    rename_file_Clientes = {
        'D01_Nome':'razao_social',
        'Fantasia':'nome_fantasia',
        'D01_Cidade':'cidade',
        'D01_Vendedor':'vendedor',
        'Combinação47':'fornecedor'
    }
    
    '''
    relatorio_geral = RelatorioDestinado(arquivo_pedido_itens, analise_dados.get('fornecedores', []), **rename_file1)
    relatorio_geral.frameFiltradoPorDiaAnalise()
    
    segunda_condicao = relatorio_geral.quantidadeProdutoPorValor(
        menor_valor=20.94,
        maior_valor=21.60
    )
    relatorio_geral.transformarDataFrameEmExcel(segunda_condicao, "segunda_condicao_xereta.xlsx")
    relatorio_geral.transformarDataFrameEmExcel(relatorio_geral.frame_analise, "segunda_geral.xlsx")
    
    terceira_condicao = relatorio_geral.quantidadeProdutoPorValor(
        menor_valor=20.34,
        maior_valor=21.00,
        diferente=20.94
    )
    relatorio_geral.transformarDataFrameEmExcel(terceira_condicao, "terceira_condicao_xereta.xlsx")
    relatorio_geral.transformarDataFrameEmExcel(relatorio_geral.frame_analise, "terceira_geral.xlsx")
    
    for i in datas:
        faturamentoVendedor = relatorio_geral.faturamentoMensalVendedor(
        data_inicial=datas.get(i, 'Não Encontrado')[0],
        data_final=datas.get(i,'Não Encontrado')[1],
        vendedor=vendedores.get('antonio_monis','Não Encontrado')
    )
        print(f'Faturamento de {i}: {faturamentoVendedor:.2f}')
    '''
        

    Relatorio = AnaliseGeralVendedores(
        nome_arquivo=arquivo_pedido_itens,
        codigosVendedor=[11,78],
        inicio_mes_analise=='2022-01-30',
        **rename_file_pedidoItens
    )
    Relatorio.codigoVendedor = 78
    
    

