from os import listdir
from os.path import isfile, join
import pandas as pd
monRepertoire = r"C:\Users\CharlesMOULIN\Desktop\Scrapping_Apple\Accessoires"
fichiers = [f for f in listdir(monRepertoire) if isfile(join(monRepertoire, f))]
fichiers = pd.DataFrame(fichiers)
print(fichiers)

import openpyxl
with pd.ExcelWriter('Missing_Accessories_Complement.xlsx', mode='a', engine='openpyxl') as writer:
    fichiers.to_excel(writer, sheet_name="new")
