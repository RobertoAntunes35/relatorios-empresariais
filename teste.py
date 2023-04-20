
import datetime

import math

def haversine(lat1, lon1, lat2, lon2):
    r = 6371.0  # raio médio da Terra em km
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = r * c
    return d


# Exemplo de uso
lat1 = -22.437051193063535
lon1 = -47.70836804713386
lat2 = -22.436231696735174
lon2 = -47.72015542480665
distancia = haversine(lat1, lon1, lat2, lon2)
print(f"A distância entre os pontos é de {distancia:.2f} km")

import folium

# Coordenadas iniciais do mapa
coordenadas_iniciais = [-23.550520, -46.633309]

# Criação do mapa
mapa = folium.Map(location=coordenadas_iniciais, zoom_start=12)

# Coordenadas dos locais de entrega
coordenadas_entrega = [
    [-23.550520, -46.633309], # Primeira entrega
    [-23.551507, -46.635116], # Segunda entrega
    [-23.552603, -46.633361], # Terceira entrega
    [-23.551067, -46.631844], # Quarta entrega
    [-23.548438, -46.632032]  # Quinta entrega
]

# Adição dos marcadores no mapa
for coordenada in coordenadas_entrega:
    folium.Marker(
        location=coordenada,
        icon=folium.Icon(color='red', icon='truck', prefix='fa')
    ).add_to(mapa)


import geopy.distance
import geopy.geocoders

# Criação do objeto geolocator
geolocator = geopy.geocoders.Nominatim(user_agent='myapplication')

# Cálculo da rota
rota = []
for i, coordenada in enumerate(coordenadas_entrega):
    # Adição da coordenada no início da rota
    if i == 0:
        rota.append(coordenada)
        continue
    
    # Cálculo da distância e duração da rota
    origem = geolocator.reverse(f'{coordenadas_entrega[i-1][0]}, {coordenadas_entrega[i-1][1]}')
    destino = geolocator.reverse(f'{coordenadas_entrega[i][0]}, {coordenadas_entrega[i][1]}')
    distancia = geopy.distance.distance(origem.point, destino.point).km
    duracao = distancia / 30 # Velocidade média de 30 km/h
    
    # Adição da coordenada na rota
    rota.append(coordenada)
    
    # Adição do ponto intermediário na rota
    ponto_intermediario = geopy.distance.distance(origem.point, destino.point).destination(point=origem.point, bearing=0)
    rota.append([ponto_intermediario.latitude, ponto_intermediario.longitude])

# Exibição do mapa
mapa.show_in_browser()
