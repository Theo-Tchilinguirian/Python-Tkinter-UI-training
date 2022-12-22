
from tkinter import *
from PIL import ImageTk, Image
from os import listdir
from os.path import isfile, join
from os import system as os_system


root = Tk()
root.title("Extremely Professional Image Viewer")
root.iconbitmap('../icone/ImgViewIcon.ico')


# Def fonctions :

def forward(img_nb):
    global my_label, button_forward, button_back

    img_nb += 1
    
    my_label.grid_forget()
    my_label = Label(image=img_list[img_nb])
    button_forward = Button(root, text=">>", command=lambda: forward(img_nb))
    button_back = Button(root, text="<<", command=lambda: back(img_nb))

    if img_nb >= len(img_list)-1:
        button_forward = Button(root, text=">>", state=DISABLED)

    # griddation
    my_label.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)

def back(img_nb):
    global my_label, button_forward, button_back

    img_nb -= 1

    my_label.grid_forget()
    my_label = Label(image=img_list[img_nb])
    button_forward = Button(root, text=">>", command=lambda: forward(img_nb))
    button_back = Button(root, text="<<", command=lambda: back(img_nb))

    if img_nb <= 0:
        button_back = Button(root, text="<<", state=DISABLED)

    # griddation
    my_label.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)


# Initialisation :

fichImg = [f for f in listdir('../') if isfile(join('../', f))]
img_list = [ImageTk.PhotoImage(Image.open("../" + f)) for f in fichImg if ".png" in f or ".jpg" in f or ".ico" in f]
if img_list == []:
    label_0 = Label(text="Pas d'images dans le dossier")
    label_0.pack()
    button_exit = Button(root, text="ok boomer", command=root.destroy)
    button_exit.pack()
else:
    my_label = Label(image=img_list[0])
    my_label.grid(row=0, column=0, columnspan=3)  # init à la 1ere image

    img_nb = 0
    # Bouton précédent grisé de base (car sur 1ere image)
    button_back = Button(root, text="<<", command=lambda: back(0), state=DISABLED) # command=back pas obligé, car désactivé
    button_exit = Button(root, text="EXIT PROGRAM", command=root.destroy)
    if len(img_list) == 1:
        button_forward = Button(root, text=">>", state=DISABLED)
    else:
        button_forward = Button(root, text=">>", command=lambda: forward(0))

    button_back.grid(row=1, column=0)
    button_exit.grid(row=1, column=1)
    button_forward.grid(row=1, column=2)


root.mainloop()
