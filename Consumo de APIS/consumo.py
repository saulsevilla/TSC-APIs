import requests

def obtener_info_spacex():
    url = "https://api.spacexdata.com/v4/launches/latest"
    response = requests.get(url)
    data = response.json()
    return data

def obtener_chiste():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)
    data = response.json()
    return data['value']

from bs4 import BeautifulSoup

def buscar_wikipedia(consulta):
    url = f"https://es.wikipedia.org/w/api.php?action=query&format=json&list=search&srsearch={consulta}"
    response = requests.get(url)
    data = response.json()
    resultados = data['query']['search']
    if resultados:
        snippet = resultados[0]['snippet']
        soup = BeautifulSoup(snippet, 'html.parser')
        return soup.get_text()
    else:
        return "No se encontraron resultados."

if __name__ == "__main__":
    
    print("Información sobre la última misión de SpaceX:")
    info_spacex = obtener_info_spacex()
    print("Nombre de la misión:", info_spacex['name'])
    print("Fecha de lanzamiento:", info_spacex['date_utc'])
    print("Detalles:", info_spacex['details'])

    print("\nObteniendo un chiste de Chuck Norris:")
    print(obtener_chiste())

    consulta = input("\nIntroduce un tema para buscar en Wikipedia: ")
    print("\nBuscando en Wikipedia...")
    print(buscar_wikipedia(consulta))