
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

import requests

# definir os pontos de coleta e entrega
points = [
    {"name": "Ponto de Coleta", "lat": -22.9068, "lng": -43.1729},
    {"name": "Entrega 1", "lat": -22.9112, "lng": -43.1808},
    {"name": "Entrega 2", "lat": -22.9025, "lng": -43.1734},
    {"name": "Entrega 3", "lat": -22.9021, "lng": -43.1826},
    {"name": "Entrega 4", "lat": -22.9102, "lng": -43.1696},
    {"name": "Ponto de Entrega", "lat": -22.9106, "lng": -43.1738}
]

# criar o mapa com Leaflet JS
from IPython.display import display, HTML
html = """
<div id="mapid" style="height: 400px;"></div>
<script>
    var map = L.map('mapid').setView([-22.9068, -43.1729], 13);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: 'Map data © <a href="https://openstreetmap.org">OpenStreetMap</a> contributors',
        maxZoom: 18,
    }).addTo(map);
</script>
"""
display(HTML(html))

# adicionar marcadores ao mapa
for i, point in enumerate(points):
    html = f"""
    <script>
        L.marker([{point["lat"]}, {point["lng"]}]).addTo(map)
            .bindPopup('{point["name"]}').openPopup();
    </script>
    """
    display(HTML(html))

# calcular a rota entre os pontos de coleta e entrega usando a API de roteamento
for i in range(1, len(points)-1):
    start = f'{points[i]["lat"]},{points[i]["lng"]}'
    end = f'{points[i+1]["lat"]},{points[i+1]["lng"]}'
    url = f'https://router.project-osrm.org/route/v1/driving/{start};{end}?overview=full&geometries=geojson'
    response = requests.get(url)
    data = response.json()
    route = data['routes'][0]['geometry']

    # desenhar a rota no mapa
    html = f"""
    <script>
        L.geoJSON({route}).addTo(map);
    </script>
    """
    display(HTML(html))
