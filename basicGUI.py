#from Tkinter import *
# if you are working under Python 3, comment the previous line and comment out the following line
from tkinter import *

root = Tk()

w = Label(root, text="Hello Tkinter!")
w.pack()
root = Tk()
logo = PhotoImage(file="~/Desktop/Picture1.gif")
w1 = Label(root, image=logo).pack(side="right")
explanation = """At present, only GIF and PPM/PGM
formats are supported, but an interface
exists to allow additional image file
formats to be added easily."""
w2 = Label(root,
           justify=LEFT,
           padx=10,
           text=explanation).pack(side="left")

root.mainloop()
