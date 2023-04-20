
import os 
FILE_STATIC = 'static'
FILE_PEDIDO_ITENS = 'Pedidos_Itens.xls'
FILE_CLIENTES = 'D01_Cliente.xls'

path = os.path.abspath(FILE_STATIC)

# Formato errado json
vendedores = {
    'antonio_monis':10,
    'balcao':1,
    'dalmo_levi':15,
    'luiz_antonio':12,
    'marcelo_thadeu':2,
    'marco_antonio':11,
    'nilson_antonio':13,
    'rubens_urubata':21,
    'sac':14,
    'wahib':16
}

file_perfect = [
    {
        "vendedor":"Antonio Monis", 
        "mesAnalise":"Janeiro",    
        "positivacao":[
            {
                "ClientesEmCadastro":150,
                "PositivacaoTotal":75,
                "PorcentagemPositivacao":0.5,
                "rankingMaioresCidade":[
                    {
                        "Primeira":50,
                        "Segunda":40,
                        "Terceira":30
                    }
                ],
                "rankingMenoresCidade":[
                    {
                        "Primeira":1,
                        "Segunda":3,
                        "Terceira":4,
                        "Quarta":5,
                        "Quinta":6
                    }
                ]
            }
        ],
        "faturamento":[
            {
                "ticketMedio":350.00,
                "maiorDiaVenda":['Segunda-Feira', 15000.00],
                "menorDiaVenda":['Sexta-Feira', 1500.00],
                "maioresFornecedores":[
                    {
                        "Primeiro":5000.00,
                        "Segundo":2000.00,
                        "Terceiro":1500.00
                    }
                ],
                "menoresFornecedoes":[
                    {
                        "Primeiro":150.00,
                        "Segundo":200.00,
                        "Terceiro":250.00,
                        "Quarto":300.00,
                        "Quinta":350.00
                    }
                ],
                "maioresClientesFaturamento":[
                    {
                        "Primeiro":30000.00,
                        "Segundo":20000.00,
                        "Terceiro":10000.00
                    }
                ],
                "menoresClientesFaturamento":[
                    {
                        "Primeiro":300.00,
                        "Segundo":350.00,
                        "Terceiro":400.00,
                        "Quarto":450.00,
                        "Quinto":500.00
                    }
                ]
            }
        ],
        "clientesPositivadosForaDiaVenda":50,
    }
]