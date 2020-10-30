import csv, ast, json, argparse, requests, os, string
import pandas as pd 

baseurl = "https://www.thecocktaildb.com/api/json/v1/1/search.php?f="
list_ABC = list(string.digits + string.ascii_uppercase)
df = pd.DataFrame()

for j in range(len(list_ABC)):
    url_list = baseurl + list_ABC[j]
    response = requests.get(url_list)
    data = response.text
    parsed = json.loads(data)
    if parsed['drinks']:
        for i in range(len(parsed['drinks'])):
            new_bebida = {'Bebida' : parsed["drinks"][i]["strDrink"] ,
                          'LinkImagen' : parsed["drinks"][i]["strDrinkThumb"],
                          'Categoria' : parsed["drinks"][i]["strCategory"],
                          'Tipo de Bebida' : parsed["drinks"][i]["strAlcoholic"],
                          'Tipo de Vaso' : parsed["drinks"][i]["strGlass"],
                         'Medida1' :  parsed["drinks"][i]["strMeasure1"],
                        'Ingrediente1' : parsed["drinks"][i]["strIngredient1"],
                         'Medida2' :  parsed["drinks"][i]["strMeasure2"],
                        'Ingrediente2' : parsed["drinks"][i]["strIngredient2"],
                         'Medida3' :  parsed["drinks"][i]["strMeasure3"],
                        'Ingrediente3' : parsed["drinks"][i]["strIngredient3"],
                         'Medida4' :  parsed["drinks"][i]["strMeasure4"],
                        'Ingrediente4' : parsed["drinks"][i]["strIngredient4"],
                         'Medida5' :  parsed["drinks"][i]["strMeasure5"],
                        'Ingrediente5' : parsed["drinks"][i]["strIngredient5"],
                         'Medida6' :  parsed["drinks"][i]["strMeasure6"],
                        'Ingrediente6' : parsed["drinks"][i]["strIngredient6"]}
            df = df.append(new_bebida, ignore_index = True)
print (df)
df = df [['Bebida',	'LinkImagen' , 'Categoria' , 'Tipo de Bebida', 'Tipo de Vaso',
          'Medida1', 	'Ingrediente1',      'Medida2', 	'Ingrediente2', 
          'Medida3', 	'Ingrediente3',      'Medida4', 	'Ingrediente4', 
          'Medida5', 	'Ingrediente5', 'Medida6', 	'Ingrediente6']]
export_csv = df.to_csv (r'C:\Users\mllui\OneDrive - Universitat Oberta de Catalunya\Uni\Data Science\Tipología y Ciclo de vida de los Datos\Bloque2\WebScrapping\TestWebScrapping\dataframe.csv', index = None, header=True)
