
import os 

FILE_STATIC = 'static'
FILE_PEDIDO_ITENS = 'Pedidos_Itens.xls'
FILE_CLIENTES = 'D01_Cliente.xls'

path = os.path.abspath(FILE_STATIC)

datas = {
    'JANEIRO':['2022-01-01', '2022-01-31'],
    'FEVEREIRO':['2022-02-01', '2022-02-28'],
    'MARCO':['2022-03-01', '2022-03-31'],
    'ABRIL':['2022-04-01', '2022-04-30'],
    'MAIO':['2022-05-01', '2022-05-31'],
    'JUNHO':['2022-06-01', '2022-06-30'],
    'JULHO':['2022-07-01', '2022-07-31'],
    'AGOSTO':['2022-08-01', '2022-08-31'],
    'SETEMBRO':['2022-09-01', '2022-09-30'],
    'OUTUBRO':['2022-10-01', '2022-10-31'],
    'NOVEMBRO':['2022-11-01', '2022-11-30'],
    'DEZEMBRO':['2022-12-01', '2022-12-31'],
}

vendedores = {
    'antonio_moni':10,
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
