"""
Lire la suite des prix (en euros entiers et terminée par zéro)
 des achats d’un client. 
Calculer la somme qu’il doit, lire la somme qu’il paye, 
et simuler la remise de la monnaie en affichant les textes "10 Euros", "5 Euros" et "1 Euro" 
autant de fois qu’il y a de coupures de chaque sorte à rendre.

"""

prixArticle=1
sommeDue=0
while prixArticle !=0:
    prixArticle = int(input("\nenter le montant de l'article: \t"))
    sommeDue += prixArticle
    break
print("\nVous devez :\t", sommeDue," euros.")
montantVersé =int(input("\nentez  montant versé:\t"))
Reste = montantVersé - sommeDue

Nmb50E =0

while Reste >=50:
    Nmb50E +=1
    Reste -=50
Nmb20E =0

while Reste >=20:
    Nmb20E +=1
    Reste -=20

   
Nmb10E =0

while Reste >=10:
    Nmb10E +=1
    Reste -=10
Nmb5E =0

if Reste >=5:
    Nmb5E =1 
    Reste -= 5
    print("reste monnaire:\t",Reste)
print("--------------------------\n") 
print("Rendu de la monnaie :\n") 
print("Billets de 50 Euros : ", Nmb50E, "\n") 
print("Billets de 20 Euros : ", Nmb20E, "\n") 
print("Billets de 10 Euros : ", Nmb10E, "\n") 
print("Billets de 5 Euros : ", Nmb5E, "\n") 
print("Pièces de 1 Euros : ", Reste, "\n") 
print("--------------------------\n") 