

# Objectifs du Scrapper Seloger : construire un tableau à 2 colonnes permettant de récupérer les informations essentielles sur le bien à financeer

import urllib
import urllib.request
import re
import pandas as pd
from bs4 import BeautifulSoup
import webbrowser

url_apple = 'https://www.apple.com/fr/shop/product/'

df = pd.read_excel ('Accessories_Cases.xlsx', engine='openpyxl')
print(df)
img = []
references = pd.DataFrame(columns=('Part_Number','Filename'))

#Test
#Part_Number = df.iloc[37,0]
#print(Part_Number)
#filename = df.iloc[37,1]
#print(filename)

#url = url_apple + Part_Number
#response = urllib.request.urlopen(url)
#produit = response.read()
#soup = BeautifulSoup(produit, "html.parser")

#for item in soup.find_all('img', height='572'):
#    print(item)
#   img.append(item['src'])

#print(img)

#Scrapper for Apple Bands
for entries in range(len(df)):
    try :
        Part_Number = df.iloc[entries,0]
        print(Part_Number)
        filename = df.iloc[entries,1]
        print(filename)

        url = url_apple + Part_Number
        response = urllib.request.urlopen(url)
        produit = response.read()
        soup = BeautifulSoup(produit, "html.parser")

        #Extraction des caractéristiques suivantes : prix, charges de co-propriété
        for item in soup.find_all('img', height='572'):
            print(item['src'])
            img.append(item['src'])

        #for index in range(len(img)):
        #   if img[index] == "":
        #        line = index
        #       break
        #line = line + 1
        #print(line)
        #print(img[line])

        #img = img[line]
  
        filename = filename.replace(" ", "_")
        filename = filename.replace("/", "_")
        print(filename)

        filename = r"C:\Users\CharlesMOULIN\Documents\Git Younited Credit\Apple"+filename+".jpg"
        print(filename)
        print(img[1])

        urllib.request.urlretrieve(img[1], filename)
        img = []
        
    except: continue

    

