
import os 
FILE_STATIC = 'static'
FILE_PEDIDO_ITENS = 'Pedidos_Itens.xls'
FILE_CLIENTES = 'D01_Cliente.xls'

path = os.path.abspath(FILE_STATIC)

# Formato errado json
vendedores = {
    'ANTONIO MONIS JUNIOR':10,
    'BALCAO':1,
    'DALMO LEVI GOMES NOGUEIRA':15,
    'LUIZ ANTONIO SANTOS':12,
    'MARCELO THADEU MONDINI':2,
    'MARCO ANTONIO NUNES DE SOUZA':11,
    'NILSON ANTONIO NASCIMENTO':13,
    'RUBENS URUBATA DE OLIVEIRA':21,
    'SAC':14,
    'WAHIB HUSSNI JUNIOR':16
}

file_perfect = [
    {
        "vendedor":"Antonio Monis", 
        "mesAnalise":"Janeiro",    
        "positivacao":[
            {
                "ClientesEmCadastro":150,# Ok
                "PositivacaoTotal":75, # Ok
                "PorcentagemPositivacao":0.5, # Ok
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



file = [
    {
    'Vendedor':'Nome Vendedor',
    'ClientesDia':[
            {
            'Segunda-Feira':(14,7,0.5, []),
            'Terca-Feira':(14,7,0.5, []),
            'Quarta-Feira':(14,7,0.5, []),
            'Quinta-Feira':(14,7,0.5, []),
            'Sexta-Feira':(14,7,0.5, [])
            }
        ]
    }
]


file_positivao_diaria = [
    {
    'vendedor':'Antonio Monis Junior',
    'segunda-feira':(14, 7, 0.5, []),
    'terca-feira':(14, 7, 0.5, []),
    'quarta-feira':(14, 7, 0.5, []),
    'quinta-feira':(14, 7, 0.5, []),
    'sexta-feira':(14, 7, 0.5, [])
    }
]
       