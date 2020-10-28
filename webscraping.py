# Fuente: https://towardsdatascience.com/web-scraping-using-python-libraries-fe3037152ed1

import re
import string
import requests
from bs4 import BeautifulSoup

firstCharacter = list(string.digits + string.ascii_uppercase)
print(firstCharacter)

url = "https://www.thecocktaildb.com/browse.php?b=A"

page = requests.get(url)
print(page)

soup = BeautifulSoup(page.text, "html.parser")
drinks = soup.findAll("a", {"href": re.compile(r"^/drink/.+")})
for link in drinks:
    print(link.get("href"))