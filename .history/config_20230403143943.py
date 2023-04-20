
import os 

FILE_STATIC = 'static'
FILE_PEDIDO_ITENS = 'Pedidos_Itens.xls'
FILE_CLIENTES = 'D01_Cliente.xls'

# from app import ano

path = os.path.abspath(FILE_STATIC)

ano = '2022'



# Formato errado json
datas = {
    'JANEIRO':[f'{ano}-01-01', f'{ano}-01-31'],
    'FEVEREIRO':[f'{ano}-02-01', f'{ano}-02-28'],
    'MARCO':[f'{ano}-03-01', f'{ano}-03-31'],
    'ABRIL':[f'{ano}-04-01', f'{ano}-04-30'],
    'MAIO':[f'{ano}-05-01', f'{ano}-05-31'],
    'JUNHO':[f'{ano}-06-01', f'{ano}-06-30'],
    'JULHO':[f'{ano}-07-01', f'{ano}-07-31'],
    'AGOSTO':[f'{ano}-08-01', f'{ano}-08-31'],
    'SETEMBRO':[f'{ano}-09-01', f'{ano}-09-30'],
    'OUTUBRO':[f'{ano}-10-01', f'{ano}-10-31'],
    'NOVEMBRO':[f'{ano}-11-01', f'{ano}-11-30'],
    'DEZEMBRO':[f'{ano}-12-01', f'{ano}-12-31'],
}

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
# Formato correto json


analise_dados_correta = [
    {
    'fornecedores':[
            {
                '6 DO AVESSO COM DE BEB EIRELI':1,
                'BEBIDAS ASTECA LTDA':2,
                'BELLPAR REFRESCOS - EIRELI':3,
                'CACHAÇA DOS AMIGOS':4,
                'CACHAÇA PALMITALZINHO':5,
                'CAFE TERRA DO REI LTDA ME':6,
                'Capri Industria e Comercio de Produtos Alimenticio':7,
                'CARVAO EL SHADDAY':8,
                'CEPAL - CERVEJARIA PAULISTANA LTDA.':9,
                'CHOCOLATES':10,
                'COMERCIAL ZARAGOZA IMP. E EXP. LTDA':11,
                'COMEXIM BEBIDAS':12,
                'CONVENCAO SAO PAULO INDUSTRIA DE BEBIDAS E CONEXOS':13,
                'DANILLA FOODS BRASIL LTDA - PARANA':14,
                'DISTRIBUIDORA':15,
                'E. DEZANI - BEBIDAS':16,
                'E2 DISTRIBUIDORA DE BEBIDAS LTDA':17,
                'ECOBRAZA':18,
                'EDENCOCO COMERCIAL IMPORTADORA E EXPORTADORA LTDA':19,
                'FLORAO ALIMENTOS LTDA':20,
                'FS FOREST SUN INDUSTRIA E COMERCIO DE IMPORTACAO E':21,
                'INDUSTRIA E COMERCIO DE BEBIDAS FORNAZIERO LTDA-EP':22,
                'LEVISSIMA':23,
                'LIOTECNICA TECNOLOGIA EM ALIMENTOS S.A.':24,
                'MAKRO ATACADISTA SA':25,
                'MARCUS PRATES DE LIMA':26,
                'MARQUES BEBIDAS E PARTICIPACOES EIRELI':27,
                'MOCOTOP':28,
                'MONTREAL ENGARRAFADORA DE BEBIDAS LTDA':29,
                'NEWAGE INDUSTRIA DE BEBIDAS LTDA':30,
                'PORTAO DE CAMBUI DOCES E LATICINIOS LTDA':31,
                'PURO SUMO LTDA':32,
                'REFRIX ENVASADORA DE BEBIDAS LTDA':33,
                'SENDAS DISTRIBUIDORA S/A LJ24':34,
                'SENIR EMBALAGENS LTDA':35,
                'SOCORRO INDUSTRIA DE BEBIDAS LTDA.':36,
                'STILUS IND. E COMERCIO DE BEBIDAS LTDA':37,
                'VINHOS BELTRAME INDUSTRIA E COMERCIO LTDA':38,
                'WEW COMERCIO DE PRODUTOS ALIMENTICIOS LTDA':39
            }
        ],
    'tipos':[],
    }
]

analise_dados = {
        'fornecedores':[
            '6 DO AVESSO COM DE BEB EIRELI',
            'BEBIDAS ASTECA LTDA',
            'BELLPAR REFRESCOS - EIRELI',
            'CACHAÇA DOS AMIGOS',
            'CACHAÇA PALMITALZINHO',
            'CAFE TERRA DO REI LTDA ME',
            'Capri Industria e Comercio de Produtos Alimenticio',
            'CARVAO EL SHADDAY',
            'CEPAL - CERVEJARIA PAULISTANA LTDA.',
            'CHOCOLATES',
            'COMERCIAL ZARAGOZA IMP. E EXP. LTDA',
            'COMEXIM BEBIDAS',
            'CONVENCAO SAO PAULO INDUSTRIA DE BEBIDAS E CONEXOS',
            'DANILLA FOODS BRASIL LTDA - PARANA',
            'DISTRIBUIDORA',
            'E. DEZANI - BEBIDAS',
            'E2 DISTRIBUIDORA DE BEBIDAS LTDA',
            'ECOBRAZA',
            'EDENCOCO COMERCIAL IMPORTADORA E EXPORTADORA LTDA',
            'FLORAO ALIMENTOS LTDA',
            'FS FOREST SUN INDUSTRIA E COMERCIO DE IMPORTACAO E',
            'INDUSTRIA E COMERCIO DE BEBIDAS FORNAZIERO LTDA-EP',
            'LEVISSIMA',
            'LIOTECNICA TECNOLOGIA EM ALIMENTOS S.A.',
            'MAKRO ATACADISTA SA',
            'MARCUS PRATES DE LIMA',
            'MARQUES BEBIDAS E PARTICIPACOES EIRELI',
            'MOCOTOP',
            'MONTREAL ENGARRAFADORA DE BEBIDAS LTDA',
            'NEWAGE INDUSTRIA DE BEBIDAS LTDA',
            'PORTAO DE CAMBUI DOCES E LATICINIOS LTDA',
            'PURO SUMO LTDA',
            'REFRIX ENVASADORA DE BEBIDAS LTDA',
            'SENDAS DISTRIBUIDORA S/A LJ24',
            'SENIR EMBALAGENS LTDA',
            'SOCORRO INDUSTRIA DE BEBIDAS LTDA.',
            'STILUS IND. E COMERCIO DE BEBIDAS LTDA',
            'VINHOS BELTRAME INDUSTRIA E COMERCIO LTDA',
            'WEW COMERCIO DE PRODUTOS ALIMENTICIOS LTDA'
        ],

        'tipos':{
            'agua': [
    
        ]},
        'produtos':[
            
        ],
        'clientes_com_desconto_financeiro':[
            'EXAMINE RIO CLARO',
            'EXAMINE SUPERMERCADO (FILIAL)',
            'ANTONIO LEMBO JUNIOR EIRELI',
            'EXAMINE IPEUNA',
            'BALAN SUPERMERCADO EIRELI',
            'PANTOJA LOJA 1',
            'PANTOJA LOJA 2'
        ]
    }

# Formato correto json
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
                "maiorDiaVenda":['Segunda-Feira', 15000.00],
                "menorDiaVenda":['Sexta-Feira', 1500.00],
                "maioresFornecedores":[
                    {
                        "Refrix":5000.00,
                        "Bellpar":2000.00,
                        "Pompeia":1500.00
                    }
                ],
                "menoresFornecedoes":[
                    {
                        "Askov":150.00,
                        "Acquissima":200.00,
                        "Leonoff":250.00
                    }
                ]
            }
        ],
        "clientesPositivadosForaDiaVenda":50,
    }
]