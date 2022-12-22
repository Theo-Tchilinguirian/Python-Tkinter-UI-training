
# Les listes en python sont des objets mutables (c a d il y a des méthodes
# mutateurs) et donc on modifie l'objet, pas la variable. Donc quand on passe
# une liste dans une fonction, l'objet contenu dans la variable est modifié.
# Différent pr les str : il faut réécrire l'objet dans la variable à chaque
# modification.

from tkinter import *
# Tout est widget dans tkinter

# Création de la fenêtre de base, le "widget racine"
root = Tk()

# Toujours deux étapes dans tkinter : définir, puis faire apparaitre
# dans la fenêtre.

# 1ere étape : la création
myLabel1 = Label(root, text="Hello World !")
myLabel2 = Label(root, text="My name is Théo Tchilinguirian")
myLabel3 = Label(root, text="    ")
# root : le Label va dans la fenêtre widget racine

# Il faut maintenant mettre ce widget dans le widget fenêtre
# On utilise pack (on le 'met' dedans, là où y'a dla place)

# Ici on utilise plutôt grid; pack laisse les choses au milieu de l'écran,
# grid va nous permettre de les positionner sur une grille.

# 2e étape : on met dans la fenêtre
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=4)
# Si l'on change les dimensions de la fenêtre, les phrases ne vont plus se
# recentrer automatiquement.
# Cependant, les colonnes sont relatives : il n'y a rien encore dans les
# colonnes 1, 2, 3... donc mettre colonne 4 est pareil que 1
myLabel3.grid(row=1, column=1)  # on peut donc remplir ces colonnes vides
# avec du texte d'espaces, pour donner une taille à ces colonnes

# qlqs PS : python : Orienté Objet, donc on peut faire les deux étapes
# en même temps, avec les méthodes :  (mais moins beau/lisible/propre)
mylabel4 = Label(root, text="a").grid(row=3, column=5)
# De plus, on ne peut pas packer ou gridder après le main loop, et on ne peut
# Que soit packer, soit gridder, mais pas les deux.

# On doit maintenant créer un Invent Loop (une boucle qui va pouvoir voir,
# par exemple, où est la souris, ... Le programme s'arrête souvent quand
# cette boucle s'arrête.)

root.mainloop()
# On imagine une grille 'grid' de carrés (lignes et colonnes) qui partent de 0.

