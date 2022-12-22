
from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Radio Buttons")


# Radio button widget

# tkinter variable  (..?)
#r = IntVar()
#r.set(2)    on set la valeur du premier

MODES_toppings = [
    ("pepperonini", 1),  # 1 pareil que "1"
    ("chese", "un"),  # donc on met "un"
    ("mushrom", "wat"),
    ("ananana", "ananana")
]

pizza = StringVar()  # transforme auto les int en str il semblerait
pizza.set("chese, or no chese.")  # Teste si pas set mdr

for text, mode in MODES_toppings:  # attr value = valeur de la variable pizza (qui de base vaut "chese")
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)

def clicked(value):
    #global myLabel
    #myLabel.pack_forget()
    myLabel = Label(root, text=value)
    myLabel.pack()


#Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
#Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()

#myLabel = Label(root, text=pizza.get())  # text = la valeur de la variable tkinter pizza
#myLabel.pack()

Button(root, text="click here", command=lambda: clicked(pizza.get())).pack()

root.mainloop()
