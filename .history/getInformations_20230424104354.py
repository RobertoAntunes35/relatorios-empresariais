import importlib.util 

spec = importlib.util.spec_from_file_location('frame_excel', 'C:/Users/marcelo/Desktop/projetos-em-andamento/controle-estoque/libs/frame_excel.py')
foo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(foo)

import pandas as pd
import numpy as np
import datetime
import os
import sys 
import copy

from config import vendedores, path, FILE_CLIENTES, FILE_PEDIDO_ITENS

class Clientes(foo.Excel):
    def __init__(self, nome_arquivo: str, listaVendedores: list, **columns_select) -> None:
        super().__init__(nome_arquivo, **columns_select)
        self.__matrizDados = self.filter_frame()
        self._listaVendedores = listaVendedores
        self._vendedores = {}
        if not isinstance(self._listaVendedores, list):
            raise TypeError("Atribua uma lista de códigos dos vendedores.")
        for codVendedor in self._listaVendedores:
            if codVendedor not in vendedores.values():
                raise ValueError("O código %s não está na lista de vendedores cadastrados." % codVendedor)
            for nome, codigo in vendedores.items():
                if codigo == codVendedor:
                    self._vendedores[nome] = codigo

    @property
    def matrizDados(self):
        return self.__matrizDados
    
    @property
    def listaVendedores(self):
        return self._listaVendedores
    
    @listaVendedores.setter
    def listaVendedores(self, newValue: int):
        if newValue not in vendedores.values():
            raise ValueError("O valor a ser incluso, não é um vendedor cadastrado.")
        self._listaVendedores.append(newValue)
    
    def clientesEmCadastro(self, codigoVendedor: list) -> pd.DataFrame:
        dados = copy.deepcopy(self.__matrizDados)
        valorFiltro = {}
        for codigo in codigoVendedor:
            if codigo not in self._listaVendedores:
                raise ValueError("O vendedor %s solicitado para analise, não foi passado como parâmetro." % codigo)
        for chave_vendedor, valor_vendedor in vendedores.items():
            for codVendedor in codigoVendedor:
                if valor_vendedor == codVendedor:
                    dataFrame = dados.loc[dados['nome_vendedor'] == chave_vendedor, ['codigo_cliente', 'nome_fantasia', 'cidade', 'dia_visita', 'nome_vendedor']]
                    valorFiltro[chave_vendedor] = dataFrame                    
                    break
        self.valuesDataFrame = pd.concat(valorFiltro.values())

        return self.valuesDataFrame

    def __str__(self) -> str:
        return f'DATA FRAME DE CLIENTES: \n {self.valuesDataFrame}'

class AnaliseGeralVendedores(foo.Excel):
    
    def __init__(self, nome_arquivo: str, codigosVendedor: list, inicio_mes_analise: str, **columns_select) -> None:
        super().__init__(nome_arquivo, **columns_select)
        self._codigoVendedor = codigosVendedor
        self.__matrizDados = self.filter_frame()

        try:
            data = datetime.datetime.strptime(inicio_mes_analise, "%Y-%m-%d")
            self._inicioMesAnalise = data.replace(day=1).date()
        except:
            raise TypeError("Erro ao formatar a data de entrada como um tipo de data, informe a data da seguinte forma: YEAR-MONTH-DAY")
        
        self._finalMesAnalise = self.finalMes(data)
        
        if not isinstance(self._codigoVendedor, list):
            raise TypeError("Atribua uma lista de informações.")

        if len(self._codigoVendedor) == 0:
            raise ValueError("Atribua ao menos um codigo de vendedor para iniciar a analise") 

        for codVendedor in self._codigoVendedor:
            if codVendedor not in vendedores.values():
                raise ValueError("O código %s não está na listagem de vendedores cadastrados." % codVendedor)

    def __str__(self) -> str:
        return super().__str__()

    def finalMes(self, inicioMes):
        return datetime.date(inicioMes.year, inicioMes.month + 1, 1) - datetime.timedelta(days=1)


    # Setters / Getters
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
        return self._inicioMesAnalise.date(), self._finalMesAnalise
    
    @mesAnalise.setter
    def mesAnalise(self, newValue):
        data = datetime.datetime.strptime(newValue, "%Y-%m-%d").replace(day=1)
        try:
            self._inicioMesAnalise = data
            self._finalMesAnalise = self.finalMes(data)
        except:
            raise ValueError("Erro no valor atribuido ao mês.")
    

    # Functions
    def retornoDadosVendedores(self, listaInformacao):
        listaDados = {}
        if isinstance(listaInformacao, (list)):
            for chave, valor in vendedores.items():
                if isinstance(listaInformacao[0], str):
                    for dados in listaInformacao:
                        if dados == chave:
                            listaDados[dados] = valor
                if isinstance(listaInformacao[0], int):
                    for dados in listaInformacao:
                        if dados == valor:
                            listaDados[chave] = dados
        return listaDados

    def positivacaoCliente(self, clientesVendedor: pd.DataFrame) -> dict:
        dados_matriz = copy.deepcopy(self.__matrizDados)
        dados = clientesVendedor
        dados_vendedores = self.retornoDadosVendedores(self._codigoVendedor)
        
        def clientesporDiaVisita():
            clientes_dia = {}
            vendedor_final = {}
            df_positivacao = {}
            for nome_vendedor, codigo_vendedor in dados_vendedores.items():
                dias_de_visita = set(np.array(dados.loc[dados['nome_vendedor'] == nome_vendedor]['dia_visita']))
                for dia in dias_de_visita:
                    quantidade_clientes_por_dia_visita = dados.loc[(dados['dia_visita'] == dia) & (dados['nome_vendedor'] == nome_vendedor), ['nome_fantasia', 'dia_visita']]
                    print(quantidade_clientes_por_dia_visita)
                    # print(f'Vendedor: {nome_vendedor} Dia de Visita: {dia} Quantidade em cadastro: {quantidade_clientes_por_dia_visita}')
                    # clientes_dia[dia] = quantidade_clientes_por_dia_visita  
                # vendedor_final[codigo_vendedor] = clientes_dia

            




        
        def positivacaoGeral():        
            df_positivacao = {}
            for nome_vendedor, codigo_vendedor in dados_vendedores.items():
                positivacao = set(np.array(dados_matriz.loc[dados_matriz['codigo_vendedor'] == codigo_vendedor]['nome_fantasia']))
                clientes_em_cadastro = set(np.array(dados.loc[dados['nome_vendedor'] == nome_vendedor]['nome_fantasia']))
                porcentagem_positivacao = (len(positivacao) / len(clientes_em_cadastro))            
                df_positivacao[nome_vendedor] = (len(clientes_em_cadastro), len(positivacao), round(porcentagem_positivacao, 3))
            return df_positivacao

        return positivacaoGeral(), clientesporDiaVisita()

if __name__ == '__main__':
    
    # Primeiro Arquivo
    file_pedido_itens = os.path.join(path, FILE_PEDIDO_ITENS)
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

    # Segundo Arquivo
    file_clientes = os.path.join(path, FILE_CLIENTES)
    rename_file_clientes = {
        'D01_Cod_Cliente':'codigo_cliente',
        'D01_Nome':'razao_social',
        'Fantasia':'nome_fantasia',
        'D01_Cidade':'cidade',
        'xregiao':'dia_visita',
        'D01_Vendedor':'nome_vendedor',
        'Latitude':'latitude',
        'Longitude':'longitude',
        'xDesconto_Condicional':'desconto_condicional',  
    }

    Cliente = Clientes(
        nome_arquivo=file_clientes,
        listaVendedores=[10,11,12,13,15,16,21],
        **rename_file_clientes
    )
    clientes = Cliente.clientesEmCadastro([11,10,12,13,15,16,21])

    Relatorio = AnaliseGeralVendedores(
        nome_arquivo=file_pedido_itens,
        codigosVendedor=[10,11,12,13,15,16,21],
        inicio_mes_analise="2022-10-05",
        **rename_file_pedidoItens
    )

    a, b = Relatorio.positivacaoCliente(clientes)

    

