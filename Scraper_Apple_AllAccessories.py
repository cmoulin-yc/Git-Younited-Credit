

# Objectifs du Scrapper Seloger : construire un tableau à 2 colonnes permettant de récupérer les informations essentielles sur le bien à financeer

import urllib
import re
import pandas as pd
from bs4 import BeautifulSoup
import webbrowser

url_apple = 'https://www.apple.com/fr/shop/product/'

df = pd.read_excel ('Accessories_v2.xlsx', engine='openpyxl')
print(df)
img = []
references = pd.DataFrame(columns=('Part_Number','Filename'))

#Scrapper for Apple Bands
for entries in range(len(df)):
    try :
        img = []
        Part_Number = df.iloc[entries,1]
        print(Part_Number)
        filename = df.iloc[entries,2]
        print(filename)

        url = url_apple + Part_Number
        response = urllib.request.urlopen(url)
        produit = response.read()
        soup = BeautifulSoup(produit, "html.parser")

        #Extraction des caractéristiques suivantes : prix, charges de co-propriété
        for item in soup.find_all('img'):
            print(item['src'])
            img.append(item['src'])

        for index in range(len(img)):
            if img[index] == "":
                line = index
                break
        line = line + 1
        print(line)
        print(img[line])

        img = img[line]
        filename = filename.replace(" ", "_")
        filename = filename.replace("/", "_")
        print(filename)

        filename = filename+'.jpg'

        urllib.request.urlretrieve(img, filename)
        line = 0
    except: continue
