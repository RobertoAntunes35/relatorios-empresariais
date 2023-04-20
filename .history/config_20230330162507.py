
import os 

FILE_STATIC = 'static'
FILE_PEDIDO_ITENS = 'Pedidos_Itens.xls'
FILE_CLIENTES = 'D01_Cliente.xls'

from app import ano

path = os.path.abspath(FILE_STATIC)

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
