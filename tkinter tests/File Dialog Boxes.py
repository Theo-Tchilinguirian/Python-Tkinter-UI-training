
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("File Dialog Boxes")


def openfile():
    global my_image  # sinon marche pas car se fait détruire après la
    #                  fermeture de la fonction (car était locale !!)
    root.filename = filedialog.askopenfilename(initialdir="../tkinter", title="Select a file" \
                                           , filetypes=(("png files", "*.png"), ("all files", "*.*")))
    # On a la position de l'image
    my_label = Label(root, text=root.filename).pack()  # le chemmin du fichier !

    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()



my_button = Button(root, text="Open file", command=openfile).pack()


root.mainloop()
