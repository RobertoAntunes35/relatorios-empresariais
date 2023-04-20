import importlib.util 

spec = importlib.util.spec_from_file_location('frame_excel', 'C:/Users/marcelo/Desktop/projetos-em-andamento/controle-estoque/libs/frame_excel.py')
foo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(foo)

import pandas as pd
import numpy as np
import datetime
import os
import sys 

from config import vendedores, path, FILE_CLIENTES, FILE_PEDIDO_ITENS

class Clientes(foo.Excel):
    def __init__(self, nome_arquivo: str, listaVendedores: list, **columns_select) -> None:
        super().__init__(nome_arquivo, **columns_select)
        self._matrizDados = self.filter_frame()
        self._listaVendedores = listaVendedores
        self.vendedores = {}
        if not isinstance(self._listaVendedores, list):
            raise TypeError("Atribua uma lista de códigos dos vendedores.")
        

        for codVendedor in self._listaVendedores:
            if codVendedor not in vendedores.values():
                raise ValueError("O código %s não está na lista de vendedores cadastrados." % codVendedor)
            for nome, codigo in vendedores.items():
                if codigo == codVendedor:
                    self.vendedores[nome] == codigo
        print(self.vendedores)


class AnaliseGeralVendedores(foo.Excel):
    
    def __init__(self, nome_arquivo: str, codigosVendedor: list, inicio_mes_analise: str, **columns_select) -> None:
        super().__init__(nome_arquivo, **columns_select)
        self._codigoVendedor = codigosVendedor
        self._matrizDados = self.filter_frame()

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
        listaVendedores=[10],
        **rename_file_clientes
    )

    Relatorio = AnaliseGeralVendedores(
        nome_arquivo=file_pedido_itens,
        codigosVendedor=[10,11],
        inicio_mes_analise="2022-10-05",
        **rename_file_pedidoItens
    )

