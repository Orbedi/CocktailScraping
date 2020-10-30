import csv, ast, json, argparse, requests, os, string
import pandas as pd 

baseurl = "https://www.thecocktaildb.com/api/json/v1/1/search.php?f="
alphanumeric_chars = list(string.digits + string.ascii_uppercase)
df = pd.DataFrame()

for char in alphanumeric_chars:
    url_list = baseurl + char
    response = requests.get(url_list)
    data = response.text
    parsed = json.loads(data)
    if parsed['drinks']:
        for drink in parsed['drinks']:
            new_bebida = {  'Bebida' :          drink["strDrink"] ,
                            'LinkImagen' :      drink["strDrinkThumb"],
                            'Categoria' :       drink["strCategory"],
                            'Tipo de Bebida' :  drink["strAlcoholic"],
                            'Tipo de Vaso' :    drink["strGlass"],
                            'Medida1' :         drink["strMeasure1"],
                            'Ingrediente1' :    drink["strIngredient1"],
                            'Medida2' :         drink["strMeasure2"],
                            'Ingrediente2' :    drink["strIngredient2"],
                            'Medida3' :         drink["strMeasure3"],
                            'Ingrediente3' :    drink["strIngredient3"],
                            'Medida4' :         drink["strMeasure4"],
                            'Ingrediente4' :    drink["strIngredient4"],
                            'Medida5' :         drink["strMeasure5"],
                            'Ingrediente5' :    drink["strIngredient5"],
                            'Medida6' :         drink["strMeasure6"],
                            'Ingrediente6' :    drink["strIngredient6"]}
            df = df.append(new_bebida, ignore_index = True)

print (df)
df = df [['Bebida',	'LinkImagen' , 'Categoria' , 'Tipo de Bebida', 'Tipo de Vaso',
          'Medida1', 	'Ingrediente1',      'Medida2', 	'Ingrediente2', 
          'Medida3', 	'Ingrediente3',      'Medida4', 	'Ingrediente4', 
          'Medida5', 	'Ingrediente5', 'Medida6', 	'Ingrediente6']]

export_csv = df.to_csv (r'.\dataframe.csv', index = None, header=True)
