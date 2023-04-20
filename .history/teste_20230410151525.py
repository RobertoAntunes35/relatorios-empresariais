
import datetime


'''
raio da terra = r
d = 2r * arcsin(sqrt(sin²((lat2-lat1)/2) + cos(lat1) * cos(lat2) * sin²((lon2-lon1)/2)))
lat1 = latitude*pi / 180 
lon1 = longitude*pi / 180
lat2 = latitude*pi / 180
lon2 = longitude*pi / 180

'''

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
lat1 = -22.906847
lon1 = -43.172897
lat2 = -23.548943
lon2 = -46.638818
distancia = haversine(lat1, lon1, lat2, lon2)
print(f"A distância entre os pontos é de {distancia:.2f} km")
