
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox  # on import ce module (tkinter aussi un package ?)

root = Tk()
root.title("Message boxes")


def popup():
    messagebox.showinfo("This is my POPUUUUP", "Hello worlde")  # titre, message, type
    # types : showinfo, showwarning, showerror, askquestion, askokcancel, askyesno, (... ?)
    # ici c'est un showinfo.  Il y a un son diff pr chaque
    # Pour askquestion par exe, il y a Oui ou Non, ou Oui ou annuler, ou etc...
    # On récup la réponse :
    réponse = messagebox.askokcancel("what's going on ?", "help me.")
    Label(root, text=réponse).pack()  # réponse est un bool True ou False, donc 1 ou 0.
    # pour askyesno, croix grisée car booléen, donc pas de réponse annulation.
    if réponse == 1:
        messagebox.showinfo("Thank you for résponse", "now giv bank")
    # peut répondre yes, no, 1, 0, ok, ...
    
# un widget message box est un pop-up
Button(root, text="Popup", command=popup).pack()




mainloop()
