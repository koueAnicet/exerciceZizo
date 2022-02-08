"""
Ecrire un programme qui demande un nombre à l'utlisateur compris entre 10 et 20, jusqu’à ce que la réponse convienne.
En cas de réponse supérieure à 20, on fera apparaître un message : « Plus petit ! »,
et inversement, « Plus grand ! » si le nombre est inférieur à 10.
"""


while True:
    nombre=int(input("\nentrer un nombre:\t"))
    if nombre <=10 :
        print("entre un nombre plus grand que 10 !\n")
        
    elif nombre >= 20:
        print("entre un nombre plus petit que 20 !\n")
    else:
        print("\ntiens ça convient!\n")  
        break 
    