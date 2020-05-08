#Program to display a rolling dice simulator
import tkinter
import random

win = tkinter.Tk()

def Roll():
    n = (random.randint(1,6))
    t.delete('1.0', tkinter.END)
    t.insert(tkinter.END,str(n))
    

b = tkinter.Button(win,text = "Roll",command = Roll)
t = tkinter.Text(win,height = 2, width = 5)
b.pack()
t.pack()

win.mainloop() 