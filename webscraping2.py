import re
import time
import string
import requests
import pandas as pd
import more_itertools  
from bs4 import BeautifulSoup

# Inicialización de variables

# Array con todos los caracteres alfanuméricos
alphanumeric_chars = ['A', 'B'] #list(string.digits + string.ascii_uppercase)
baseurl = "https://www.thecocktaildb.com/browse.php?b="
links = list()
dataframe = pd.DataFrame();
columns =  ["Bebida", "linkImagen", "Ingrediente1", "Medida1","Ingrediente2", "Medida2", "Ingrediente3", "Medida3", "Ingrediente4", "Medida4", "Ingrediente5", "Medida5", "Ingrediente6", "Medida6", "Ingrediente7", "Medida7", "Ingrediente8", "Medida8"]

# Obtenemos las bedidas de cada letra.
for char in alphanumeric_chars:
    # Se obtiene el html
    url = baseurl + char
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    # Se extraen los enlaces de las bebidas.
    drinks = soup.findAll("a", {"href": re.compile(r"^/drink/.+")})
    
    # Se almacenan en una lista
    for link in drinks:
        links.append(link.get("href"))

    time.sleep(0.1) # 100 milliseconds

baseurl = "https://www.thecocktaildb.com"

count = 0
# Iteramos sobre los links para obtener la información de cada uno de ellos.
for drinkLink in links:
    # if(count == 10): break

    # Se obtiene el html
    url = baseurl + drinkLink
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    # Se obtiene el nombre de la bebida y el link de la imagen
    nombreBebida = soup.table.tr.td.h2.text.strip()
    LinkImagen = soup.find("a", rel='prettyPhoto').get('href')
    

    # Se obtienen los ingredientes y las medidas.
    ingredients = soup.findAll("figcaption")
    
    # Se separa el ingrediente de su medida, y se guardan en listas separadas.
    ingredient = ["","","","","","","",""]
    measurement = ["","","","","","","",""]
    for index, element in enumerate(ingredients):
        string = element.text.replace("\r\n", "").replace("\n", "").replace("\r", "")
        values = string.split("  ")

        if index >= 8: break

        # print(index, values)
        if(len(values) == 1):
            ingredient[index] = values[0]
            measurement[index] = ""
        elif(len(values) > 1):
            ingredient[index] = values[1]
            measurement[index] = values[0]
    
    variables = list([nombreBebida, LinkImagen])
    inter = list(more_itertools.roundrobin(ingredient, measurement))
    ingredientes_list = variables + inter

    # Se almacena la nueva bebida en un dataframe de pandas.
    dataframe = dataframe.append(dict(zip(columns,ingredientes_list )), ignore_index = True)

    # count+=1
    time.sleep(0.1)

# Se exporta el contenido del dataframe a un archivo CSV
export_csv = dataframe.to_csv(r'.\dataframe_webscraping.csv', index = None, header=True)
