from dotenv import load_dotenv
import os 

from getInformations import Clientes, AnaliseGeralVendedores, file_clientes, file_pedido_itens, rename_file_clientes, rename_file_pedidoItens




if __name__ == '__main__':
    load_dotenv()

    Cliente = Clientes(
            nome_arquivo=file_clientes,
            listaVendedores=[10,11,12,13,15,16,21],
            **rename_file_clientes
        )
    clientes = Cliente.clientesEmCadastro([11,10,12,13,15,16,21])

    Relatorio = AnaliseGeralVendedores(
        nome_arquivo=file_pedido_itens,
        codigosVendedor=[10,11,12,13,15,16],
        inicio_mes_analise="2022-10-05",
        **rename_file_pedidoItens)
    
    (a,c),b = Relatorio.positivacaoCliente(clientes, '2023-04-01', '2023-04-30')
    print(a[10])