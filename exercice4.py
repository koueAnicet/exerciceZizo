"""Réécrire l’algorithme précédent, mais cette fois-ci on ne connaît 
pas d’avance combien l’utilisateur souhaite saisir de nombres. 
La saisie des nombres s’arrête lorsque l’utilisateur entre un zéro"""
liste=[]
n =0
for i in range(0, 10):
    b= int(input('\nenter un nombre: \t'))
    if i == 1 or b > n:
        liste.append(b)
    elif b==0:
        print("Au revoir!\n")
        break
print("le plus grand parmi ces nombre est:\t", max(liste),"\n")