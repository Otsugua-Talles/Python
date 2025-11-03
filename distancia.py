from geopy.geocoders import Nominatim
from geopy.distance import geodesic

# Inicializa o geocodificador (usa dados do OpenStreetMap)
geolocator = Nominatim(user_agent="calc_distancia")

# Função para buscar coordenadas de uma cidade
def obter_coordenadas(cidade):
    local = geolocator.geocode(cidade)
    if local:
        return (local.latitude, local.longitude)
    else:
        return None

# Entrada do usuário
origem = input("Digite a cidade de ORIGEM: ")
destino = input("Digite a cidade de DESTINO: ")

# Busca coordenadas
coord_origem = obter_coordenadas(origem)
coord_destino = obter_coordenadas(destino)

# Verifica se encontrou
if coord_origem and coord_destino:
    distancia = geodesic(coord_origem, coord_destino).kilometers
    print(f"\nDistância entre {origem} e {destino}: {distancia:.2f} km")
else:
    print("Não foi possível localizar uma das cidades.")
