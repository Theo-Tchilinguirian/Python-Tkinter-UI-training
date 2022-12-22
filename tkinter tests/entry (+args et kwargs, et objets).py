
def abc(a1, a2, *args, kwa1, kwa2, **kwargs):
    pass
# + une fonction peut modifier un objet d'une de nos classes sans que l'on ai
# besoin de mettre l'objet en paramètre ! le nom de l'objet semble global, comme
# pour les noms des widgets ici, ou de nos classes custom.

from tkinter import *


root = Tk()

ntry = Entry(root, width=50, borderwidth=5)
# ntry est dans root.
ntry.pack()
ntry.insert(0, "nom par défaut")
# insert écrit qlq chose par défaut dans l'entry au lancement.


def myClick():
    DaBigElo = "Hélo " + ntry.get()
    myLabel = Label(root, text=DaBigElo, width=50)
    # get va récup le txt de ntry
    myLabel.pack()
myButton1 = Button(root, text="mété vot non", padx=50, pady=30, command=myClick, \
                   borderwidth=5, width=3, fg="white", bg="black")
myButton1.pack()


root.mainloop()
