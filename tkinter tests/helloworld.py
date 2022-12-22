
from tkinter import *
# Tout est widget dans tkinter

# Création de la fenêtre de base, le "widget racine"
root = Tk()

# Toujours deux étapes dans tkinter : définir, puis faire apparaitre
# dans la fenêtre.

myLabel = Label(root, text="Hello World !")
# root : le Label va dans la fenêtre widget racine

# Il faut maintenant mettre ce widget dans le widget fenêtre
# On utilise pack (on le 'met' dedans, là où y'a dla place)

myLabel.pack()


# On doit maintenant créer un Invent Loop (une boucle qui va pouvoir voir,
# par exemple, où est la souris, ... Le programme s'arrête souvent quand
# cette boucle s'arrête.)

root.mainloop()
