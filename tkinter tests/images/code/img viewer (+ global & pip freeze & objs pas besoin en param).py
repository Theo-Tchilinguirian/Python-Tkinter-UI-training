
from tkinter import *
from PIL import ImageTk, Image
# pip freeze dans cmd pr savoir quels modules installés

root = Tk()
root.title("Extremely Professional Image Viewer")
root.iconbitmap('../Mail.ico')  # exemple chemin relatif


# Pas besoin de passer img_list en paramètre !! (c un obj liste)
# mais obj pas modif à l'ext si redéf en local ds une fonction.
def forward(img_nb):
    global my_label, button_forward, button_back

    img_nb += 1
    
    my_label.grid_forget()
    my_label = Label(image=img_list[img_nb])
    button_forward = Button(root, text=">>", command=lambda: forward(img_nb))
    button_back = Button(root, text="<<", command=lambda: back(img_nb))

    if img_nb >= 2:
        button_forward = Button(root, text=">>", state=DISABLED)
    
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
    
    my_label.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)


# Initialisation :

my_img1 = ImageTk.PhotoImage(Image.open("../Envoyer.png"))
my_img2 = ImageTk.PhotoImage(Image.open("../Ecrire.png"))
my_img3 = ImageTk.PhotoImage(Image.open("../ImgViewIcon.png"))

img_list = [my_img1, my_img2, my_img3]


#global my_label, img_nb    PAS ICI !! (c'est QUE ds les def de fonctions)

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)  # init à la 1ere image

img_nb = 0
# Bouton précédent grisé de base (car sur 1ere image)
button_back = Button(root, text="<<", command=lambda: back(0), state=DISABLED) # command=back pas obligé, car désactivé
button_exit = Button(root, text="EXIT PROGRAM", command=root.destroy)
button_forward = Button(root, text=">>", command=lambda: forward(0))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)


root.mainloop()
