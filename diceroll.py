import random
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Hello World")
root.geometry('1280x720')
root.configure(bg='black')
root.resizable(width=False, height=False)

l1 = Label(root, font=("Helvetica", 260))


def roll():
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    l1.config(text=f'{random.choice(dice)}{random.choice(dice)}')
    l1.pack()


b1 = Button(root, text="Roll The Dice!", fg="blue", command=roll)
b1.place(x=300, y=0)
b1.pack()

root.mainloop()
