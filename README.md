CocktailScraping
======
## Tipología y ciclo de vida de los datos.
### Práctica 1

En esta práctica se realiza la extracción de datos de una web utilizando dos técnicas: **Web Scraping** y **API**. 

La web utilizada es [TheCocktailBD](https://www.thecocktaildb.com/). Esta web tiene información sobre 604 cócteles. Para cada cóctel se proporciona una imagen y una lista con los ingredientes y su medida.

Este codigo ha sido realizado por **Orlando Belloch y Marc Lluis**

#### Español

Para la correcta ejecucion de este codigo, es necesario instalar las siguientes bibliotecas:
- pip install pandas
- pip install requests
- pip install beautifulsoup4
- pip install more_itertools 

#### Atributos
Los atributos obtenidos con Web Scraping son los siguientes:
- Nombre de la bedida
- Link de la imagen
- Ingredientes (De 1 a 8)
- Medidas de los ingredientes (De 1 a 8)
