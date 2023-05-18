from dotenv import load_dotenv
import os 
import pandas as pd
from getInformations import Clientes, AnaliseGeralVendedores, file_clientes, file_pedido_itens, rename_file_clientes, rename_file_pedidoItens




if __name__ == '__main__':
    load_dotenv()

    while True:

        Cliente = Clientes(
                nome_arquivo=file_clientes,
                listaVendedores=[10,11,12,13,15,16,21],
                **rename_file_clientes
            )
        clientes = Cliente.clientesEmCadastro([11,10,12,13,15,16,21])

        mes_analise = input(str('Digite o mês de analise, sendo ele da seguinte forma: year-month-day: \n'))

        Relatorio = AnaliseGeralVendedores(
            nome_arquivo=file_pedido_itens,
            codigosVendedor=[10, 11, 12, 13, 15, 16],
            inicio_mes_analise=mes_analise,
            **rename_file_pedidoItens)
        
        inicio_semana = input(str('Digite a data de início da semana, sendo ela da seguinte forma: year-mont-day: \n'))
        termino_da_semana = input(str('Digite a data de término da semana, sendo ela da seguinte forma: year-mont-day: \n'))


        (a,_, c),b = Relatorio.positivacaoCliente(clientes, inicio_semana, termino_da_semana)
        listaFrame = []
        for key, value in a.items():
            listaFrame.append(pd.DataFrame(value))
            print(f'Vendedor: {key} Positivações: {value}')
        # print(c)
        frameFinal = pd.concat(listaFrame)

        print(frameFinal)

        valor_termino = input('Digite 1 para sair do laço!')
        if valor_termino == '1':
            break