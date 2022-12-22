
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Sliders")
root.geometry("400x300")


# scale widget
vertical = Scale(root, from_=10, to=2400)  # "from_" car "from" est un keyword
vertical.pack()  # Bizarrement, on ne peut pas directement le pack.

horizontal = Scale(root, from_=10, to=400, orient=HORIZONTAL)
horizontal.pack()


my_label = Label(root, text=horizontal.get()).pack()

# DOIT ETRE DEFINIE AVANT le pack du bouton !!
def slide():  # Update le label à chaque press du bouton
    my_label = Label(root, text="somme = " + str(horizontal.get()+vertical.get())).pack()
    root.geometry("{}x{}".format(vertical.get(), horizontal.get()))

my_btn = Button(root, text="click.", command=slide).pack()



def slide(var):  # On redéfinie slide, mais l'argument est passé par les sliders
    my_label = Label(root, text="somme = " + str(horizontal.get()+vertical.get())).pack()
    root.geometry("{}x{}".format(vertical.get(), horizontal.get()))

# Sliders qui updatent auto :  On donne l'argument direct en commande à une fonction
vertical2 = Scale(root, from_=100, to=500, command=slide)
vertical2.pack()

horizontal2 = Scale(root, from_=100, to=500, orient=HORIZONTAL, command=slide)
horizontal2.pack()

# Bouton mieux, marche mieux.



root.mainloop()
