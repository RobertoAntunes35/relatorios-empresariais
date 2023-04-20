import importlib.util 

spec = importlib.util.spec_from_file_location('frame_excel', 'C:/Users/marcelo/Desktop/projetos-em-andamento/controle-estoque/libs/frame_excel.py')
foo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(foo)

import pandas as pd
import numpy as np
import datetime





class AnaliseGeralVendedores(foo.Excel):
    
    def __init__(self, nome_arquivo: str, codigosVendedor: list, inicio_mes_analise: str, **columns_select) -> None:
        super().__init__(nome_arquivo, **columns_select)
        self._codigoVendedor = codigosVendedor
        
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