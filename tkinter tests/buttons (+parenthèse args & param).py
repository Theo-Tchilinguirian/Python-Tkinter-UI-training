
from tkinter import *


root = Tk()

# button widget. Premier paramètre : où on le met (dans la fenêtre)
myButton = Button(root, text="Click Me !", state=DISABLED)
# l'argument DISABLED le paramètre state empêche d'appuyer sur le bouton.
# Pour changer la taille du bouton, on utilise les paramètres padx et pady.

myButton.pack()
myButton = Button(root, text="Click Me !", padx=50, pady=30)
# Étrangement, le boutton ne se supprime pas pour se modifier, un autre est créé
myButton.pack()


# Pour faire fonctionner le bouton, on utilise une fonction.
def myClick():
    myLabel = Label(root, text="Clicked da bouton.")
    myLabel.pack()
# Le bouton va appeler la fonction.
myButton1 = Button(root, text="Appeler la fonction commande", command=myClick, fg="white", bg="black")
# On ne marque pas les parenthèses (ou sinon python l'apelle quand il le lit) et
# il ne marchera plus.
# fg change la couleur du foreground, etc... les codes couleur hex(a) (#ffffff, #000000, ...) marchent aussi.
myButton1.pack()
root.mainloop()
