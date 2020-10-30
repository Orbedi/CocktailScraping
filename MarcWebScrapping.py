
# Fuente: https://towardsdatascience.com/web-scraping-using-python-libraries-fe3037152ed1

import re, string, requests, html5lib
import string
import requests
from bs4 import BeautifulSoup
import pandas as pd 

firstCharacter = list(string.digits + string.ascii_uppercase)
firstCharacter = ["a", "b"]

baseurl = "https://www.thecocktaildb.com/browse.php?b="
baseurl_bebida = "https://www.thecocktaildb.com"
list_links = []

for j in range(len(firstCharacter)):
    url_list = baseurl + firstCharacter[j]
    page = requests.get(url_list)
    print(page)
    soup = BeautifulSoup(page.text, "html.parser")
    drinks = soup.findAll("a", {"href": re.compile(r"^/drink/.+")})
    for link in drinks:
        #print(link.get("href"))
        list_links.append(link.get("href"))
        #print(Bebida)

print(list_links)

##############################################################################################

#creamos el data frame
df = pd.DataFrame()
columns= ["Bebida", "Ingrediente1", "Ingrediente2", "Ingrediente3", "Ingrediente4", "Ingrediente5", "Ingrediente6","Ingrediente7"]
#En cada pagina web, cogemos el nombre de la bebida y los ingredientes
for i in range(len(list_links)):
    url = baseurl_bebida + list_links[i]
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html5lib")
    print(soup.prettify())
    nombre_list = list()
    #Sacamos el nombre de la bebida:
    bebida = (soup.findAll ('title'))
    for i in bebida:
        nombre_list.append(i.text)
        nombre_bebida = str(nombre_list[0])
    nombre_bebida = nombre_bebida.split("|")[0]
    #Sacamos los ingredientes y lo convertimos en una lista:
    ingredientes = soup.findAll('figcaption')
    ingredientes_list = list ()
    for i in ingredientes:
        ingredientes_list.append(i.text)
    #Insertamos el nombre dentro de la lista de los ingredientes
    ingredientes_list.insert(0, nombre_bebida)
    #Lo incluimos dentro del dataframe
    df = df.append(dict(zip(columns,ingredientes_list )), ignore_index = True)

print(df)

export_csv = df.to_csv (r'C:\Users\mllui\OneDrive - Universitat Oberta de Catalunya\Uni\Data Science\Tipología y Ciclo de vida de los Datos\Bloque2\WebScrapping\TestWebScrapping\WebScrappingHML.csv', index = None, header=True)
