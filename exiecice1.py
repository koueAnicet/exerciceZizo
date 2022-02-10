liste = []
suggestion="oui"
while suggestion=="oui":
    
    lettre= str(input("donne une lettre de l'aphabet") )
    liste.append(lettre)
    sorted(liste)#ordorner la liste
    suggestion =input("veux tus ajouter d'autres lettre?")    
print(liste)
