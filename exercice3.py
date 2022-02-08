"""
le programme demandera successivement 10 nombres à l’utilisateur, et qui lui dira 
ensuite quel était le plus grand parmi ces 20 nombres : 
Entrez le nombre numéro 1 : 12 Entrez le nombre numéro 2 : 14 etc. Entrez le nombre numéro 10 : 6 
Le plus grand de ces nombres est : 14 Modifiez ensuite l’algorithme pour que le
programme affiche de surcroît en quelle position avait été saisie ce nombre : 
C’était le nombre numéro 2
"""
liste=[]
n =0
for i in range(0, 10):
    b= int(input('\nenter un nombre: \t'))
    if i == 1 or b > n:
        liste.append(b)
        indexe= liste.index(max(liste))
        indexe+=1
print("le plus grand parmi ces nombre est:\t", max(liste)," saisie à la position:\t", indexe, "\n")
