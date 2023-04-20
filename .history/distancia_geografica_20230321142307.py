import math

def distance(lat1, lon1, lat2, lon2):
    # Raio da Terra em metros
    R = 6371e3

    # Conversão de graus para radianos
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    # Cálculo da distância entre os pontos
    a = math.sin(delta_phi / 2)**2 + \
        math.cos(phi1) * math.cos(phi2) * \
        math.sin(delta_lambda / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = R * c

    return d


# Exemplo de uso da função
distancia_ipeuna_rio_claro = distance(-22.435179014007506, -47.71567497693415, -22.43608224347925, -47.71392123874381)
# retorna aproximadamente 343km
print(distancia_ipeuna_rio_claro/1000)
