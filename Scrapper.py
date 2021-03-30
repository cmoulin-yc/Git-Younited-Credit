# Objectifs du Scrapper Seloger : construire un tableau à 2 colonnes permettant de récupérer les informations essentielles sur le bien à financeer

import urllib.request
import re
import pandas as pd
from bs4 import BeautifulSoup

url_apple = 'https://wwww.apple.com/ae/shop/product/';

Part_Number = 'MQ4U2ZM/A/'

url = 'https://wwww.apple.com';

response = urllib.request.urlopen(url)
produit = response.read()
soup = BeautifulSoup(produit, "html.parser")
print(soup)

categories = ['typebien','Codepostal', 'Adresse', 'prix','nb_pieces','nb_chambre','surface','chargescopro','DiagEnergétique']
df = pd.DataFrame(columns=categories)

print(df)


#Extraction des caractéristiques suivantes : prix, charges de co-propriété
montant = []
for tag in soup.find_all('span', {'class' : {'global-styles__TextNoWrap-sc-1aeotog-6 dVzJN'}}) :
 montant.append(tag.get_text())
print(montant)
n = 2
while n > 0:
 montant[n-1] = re.findall('\d+\s+\d+', montant[n-1])
 n -= 1
#prix du bien
prix = "".join(montant[0])
print(prix)
#montant des charges de coprop
charges_copro = "".join(montant[1])

#Extraction des caractéristiques suivantes : nature du bien
type_bien = soup.find('div',{'class' : {"Summarystyled__Title-tzuaot-3 bQVvuG"}})
type_bien = type_bien.get_text()
print(type_bien)

#Extraction des caractéristiques suivantes : # de pièces, # de chambres, surface
caracteristiques = []
for tag in soup.find_all('div',{'class' : {"TagsWithIcon__TagContainer-j1x9om-2 fmGXPj"}}) :
 caracteristiques.append(tag.get_text())
n = 3
while n > 0:
 caracteristiques[n-1] = re.findall('\d+', caracteristiques[n-1])
 n -= 1
nb_pieces = "".join(caracteristiques[0])
print(nb_pieces)
nb_chambres = "".join(caracteristiques[1])
print(nb_chambres)
surface = "".join(caracteristiques[2])
print(surface)

#Extraction de la ville et de l'arrondissement
ville = soup.find('div',{'class' : {"Summarystyled__Address-tzuaot-5 jqlODu"}})
ville = ville.get_text()
ville = ville.split(" ")
print(ville)
quartier = "".join(ville[1])
#print(quartier)
ville = "".join(ville[0])
#print(ville)

#Extraction du nombre de lots
try :
 copropriete = soup.find('p',{'class' : {"Coownership__ContentWrapper-l39md3-0 fnALhy"}})
 copropriete = copropriete.get_text()
 copropriete = re.findall('\d+', copropriete)
 copropriete = int(copropriete[0])
except:
 copropriete = ""
print(copropriete)

#Extraction des charges de copropriete
#try :
# charges_corpro = soup.find('span',{'class' : {"global-styles__TextNoWrap-sc-1aeotog-6 dVzJN"}})
# print(charges_corpro)
# charges_corpro = charges_corpro.get_text()
# charges_corpro = re.findall('\d+', charges_corpro)
# charges_corpro = charges_corpro[0]
#except:
# charges_corpro = ""
#print(charges_corpro)

#Stockage des informations dans la base de donnée
import sqlite3
conn = sqlite3.connect('MonPatrimoine.sqlite3')
cur = conn.cursor()


cur.execute('SELECT url FROM annonces WHERE url = ?;', [url])
row = cur.fetchone()
print(row)
if row is None:
 cur.execute('INSERT INTO annonces (url, type_bien, quartier, ville, surface, nb_pieces, nb_chambres, prix, charges_copro) VALUES (?,?,?,?,?,?,?,?,?);',[url, type_bien, quartier, ville, surface, nb_pieces, nb_chambres, prix, charges_copro])
else:
 cur.execute('UPDATE annonces SET (type_bien, quartier, ville, surface, nb_pieces, nb_chambres, prix, charges_copro) = (?,?,?,?,?,?,?,?) WHERE url = ? ;',[type_bien, quartier, ville, surface, nb_pieces, nb_chambres, prix, charges_copro, url])

conn.commit()
