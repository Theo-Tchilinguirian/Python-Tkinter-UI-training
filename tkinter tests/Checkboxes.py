
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Checkboxes")
#root.iconbitmap()
root.geometry("400x400")

# On crée une variable tkinter (objets avec mutateurs et accesseurs)
var = IntVar()
var.set(3)

c = Checkbutton(root, text="Check this boy", variable=var, onvalue=2, offvalue=34)
c.pack()  # var sera 2 ou 34; 3 de base
# Si est séléctionné par défaut, utiliser : c.deselect(); mais mettra la valeur offvalue de base.

myLabel = Label(root, text=var.get()).pack()


def Update():
    myLabel = Label(root, text=var.get()).pack()

myButton = Button(root, text="Update Selection", command=Update).pack()


def Change():
    global var
    global c
    var = StringVar()
    var.set('abc')
    c.pack_forget()
    c = Checkbutton(root, text="Check this boy", variable=var, onvalue="ON", offvalue="OFF")
    c.pack()  # var sera ON ou OFF; rien de base (var set à 'abc', sinon rien, ou 0 pr les IntVar)

b2 = Button(root, text="Change System", command=Change).pack()


root.mainloop()
