
from tkinter import *


root = Tk()
root.title("Calculator")

ntry = Entry(root, width=35, borderwidth=5)
ntry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
# columnspan=3 : colonne de 3 colonnes
ntry.insert(0, 0)

global operationQueue
operationQueue = []

def button_click(number):
    current = ntry.get()
    ntry.delete(0, END)
    ntry.insert(0, str(current) + str(number))

def button_clear():
    ntry.delete(0, END)

def button_add():
    current = ntry.get()
    ntry.delete(0, END)
    ntry.insert(0, int(current) + int)

def button_sub():
    current = ntry.get()
    ntry.delete(0, END)
    operationQueue.append(int(current), "sub")

def button_mult():
    current = ntry.get()
    ntry.delete(0, END)
    operationQueue.append(int(current), "mult")

def button_div():
    current = ntry.get()
    ntry.delete(0, END)
    operationQueue.append(int(current), "div")

def button_equal():
    result = int()
    while not operationQueue == []:
        operation = operationQueue.pop(0)
        if operation == add:
            pass
        if operation == add:
            pass
        if operation == add:
            pass
        if operation == add:
            pass
        else:
            result 


# Defining buttons :

# Au lieu de : Button(root, text="1", padx=40, pady=20, command=button_click)
# On écrit : Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
# : le lambda dans "lambda: button_click(1)" va permettre de passer un paramètre.
# car on ne met pas les parenthèses au lambda (et lambda n'a pas de paramètres)
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

button_add = Button(root, text="+", padx=39, pady=20, command=button_add)
button_sub = Button(root, text="-", padx=40, pady=20, command=button_sub)
button_mult = Button(root, text="x", padx=39, pady=20, command=button_mult)
button_div = Button(root, text=":", padx=41, pady=20, command=button_div)
button_clear = Button(root, text="clear", padx=31, pady=20, command=button_clear)
button_equal = Button(root, text="=", padx=89, pady=20, command=button_equal)

# Putting buttons on screen :

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_0.grid(row=4, column=1)
button_add.grid(row=4, column=0)
button_clear.grid(row=4, column=2)

button_sub.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

button_mult.grid(row=4, column=3)
button_div.grid(row=5, column=3)


root.mainloop()
