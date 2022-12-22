
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Frames")


frame = LabelFrame(root, text="This is frame. Yis.", padx=50, pady=50)  # Padding intérieur
frame.pack(padx=100, pady=100)  # Padding extérieur

b = Button(frame, text="no.", padx=10, pady=5)
b.grid(column=0, row=0, pady=30)
# PS : On peut packer dans une frame et gridder en dehors, et inversement

b = Button(root)
b.pack()

root.mainloop()
