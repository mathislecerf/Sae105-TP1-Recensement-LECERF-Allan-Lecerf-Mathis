import csv
from pylab import figure, plot, show, scatter

#Données de 2008
table2008 = []
with open('donnees_2008.csv', newline="") as csvfile:
    reader=csv.reader(csvfile,delimiter=',')
    for row in reader:
        table2008.append(row)

#Données de 2016
table2016 = []
with open('donnees_2016.csv', newline="") as csvfile:
    reader=csv.reader(csvfile,delimiter=',')
    for row in reader:
        table2016.append(row)

#Données de 2021
table2021 = []
with open('donnees_2021.csv', newline="") as csvfile:
    reader=csv.reader(csvfile,delimiter=';')
    for row in reader:
        table2021.append(row)

#Données de 2023
table2023 = []
with open('donnees_2023.csv', newline="") as csvfile:
    reader=csv.reader(csvfile,delimiter=';')
    for row in reader:
        table2023.append(row)

#Méta données
tablemeta = []
with open('metadonnees_communes.csv', newline="") as csvfile:
    reader=csv.reader(csvfile,delimiter=';')
    for row in reader:
        tablemeta.append(row)

#Filtrage de la population Totale de Auxerre en 2008
for i in range(len(table2008)):
    if table2008[i][6] == "Auxerre" :
        Pop2008=int(table2008[i][9])

#Filtrage de la population Totale de Auxerre en 2016
for i in range(len(table2016)):
    if table2016[i][6] == "Auxerre" :
        Pop2016=int(table2016[i][9])

#Récupération du CodeCommune en fonction de son nom
for i in range(len(tablemeta)):
    if tablemeta[i][3] == 'Auxerre' :
        CodeCom = tablemeta[i][2]

#Filtrage de la population Totale de Auxerre en 2021
for i in range(len(table2021)):
    if table2021[i][2] == CodeCom:
        Pop2021=int(table2021[i][5])

#Filtrage de la population Totale de Auxerre en 2023
for i in range(len(table2023)):
    if table2023[i][7] == "Auxerre" :
        Pop2023=int(table2023[i][10])


figure()
scatter([2008,2016,2021,2023],[Pop2008,Pop2016,Pop2021,Pop2023])
plot([2008,2016,2021,2023],[Pop2008,Pop2016,Pop2021,Pop2023],"-g")
show()
