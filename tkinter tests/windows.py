
from tkinter import *
from PIL import ImageTk, Image

root = Tk()  # root window
root.title("New Windoowssss")

# on défini la nouvelle fenêtre
top = Toplevel()  # n'aura pas d'icone, même si le root en a un.
# aura cependant le même titre, mais on peut le changer:
top.title("aaaaaaaafenêtre secondaireaaaaaaaaaaa")
# fermer le root ferme toutes les autres fenêtres, mais pas l'inverse
label = Label(top, text="élo worlde").pack()  # fenêtre top


def open():
    winT = Toplevel()
    winT.title("une autre !")
    # peut être besoin de global les images PIL for some reason. quand ds autre 
    btn = Button(winT, text="close windows", command=winT.destroy).pack()

btn = Button(root, text="faire apparaitre une fenêtre", command=open).pack()

root.mainloop()
