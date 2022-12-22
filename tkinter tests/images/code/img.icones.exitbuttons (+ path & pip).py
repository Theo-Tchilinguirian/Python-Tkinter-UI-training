
from tkinter import *
from PIL import ImageTk, Image
# pip freeze dans cmd pr savoir quels modules installés

root = Tk()
root.title("Icones, Images, Boutons de Sortie.")
root.iconbitmap('../mail.ico')  # exemple chemin relatif


# Ici, 3 étapes: 1, définir :
my_img = ImageTk.PhotoImage(Image.open("../Envoyer.png"))
# 2, on met l'image autre part :
my_label = Label(image=my_img)
# 3, on met ce qlq chose sur l'écran :
my_label.pack()
# Il est possible de mettre une image sur quasiment tous les widgets tkinter



button_quit = Button(root, text="Exit Program", command=root.destroy)
button_quit.pack()


root.mainloop()
