import csv
from pylab import figure, plot, show, scatter, title, xlabel, ylabel

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

#Initialisation de notre saisie utilisateur 
CodeDep = str(input("Saisissez le Code Département dont lequel vous souhaitez obtenir la population totale : "))

#Initilisation de variables qui contiendront nos populations totales par années
Pop2008=0
Pop2016=0
Pop2021=0
Pop2023=0

#Récupération et Addition de la population Totale du département saisi 2008
for i in range(len(table2008)):
    if table2008[i][2] == CodeDep :
        Pop2008 += int(table2008[i][9])

#Récupération et Addition de la population Totale du département saisi en 2016
for i in range(len(table2016)):
    if table2016[i][2] == CodeDep :
        Pop2016 += int(table2016[i][9])

#Récupération du Nom de Département en fonction de son code
for i in range(len(tablemeta)):
    if tablemeta[i][2] == CodeDep :
        NomDep = tablemeta[i][3]

#Récupération et Addition de la population Totale du département saisi en 2021
for i in range(len(table2021)):
    if table2021[i][1] == CodeDep:
        Pop2021 += int(table2021[i][5])

#Récupération et Addition de la population Totale du département saisi en 2023
for i in range(len(table2023)):
    if table2023[i][2] == CodeDep :
        Pop2023 += int(table2023[i][10])


figure() #Initilisation du graphique
title(f"Evolution de la Population de {NomDep}") #Mise en place d'un titre
scatter([2008,2016,2021,2023],[Pop2008,Pop2016,Pop2021,Pop2023]) #Affichage des points
plot([2008,2016,2021,2023],[Pop2008,Pop2016,Pop2021,Pop2023],"-g") #Affichage du graphique
xlabel("Années") #Label des Abscisses
ylabel("Population") #Label des ordonnées
show()
