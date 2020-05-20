#Requirements 
#Tkinter , PIL
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import ttk, colorchooser
from PIL import Image,ImageTk
from tkinter.ttk import Style
import os

class main:
    def __init__(self,win):
        self.style = Style()
        self.style.configure('W.TButton', font =('calibri', 10, 'bold', 'underline'), foreground = 'red') 
        self.win = win
        self.fg = 'black'
        self.bg = 'white'
        self.oldx = None
        self.oldy = None
        self.width = 3
        self.draw()
        #Binding the events to the canvas widget
        self.win.bind('<KeyPress>',self.bsize)
        self.c.bind('<B1-Motion>',self.paint)
        self.c.bind('<ButtonRelease-1>',self.reset)
        self.win.config(cursor = 'pencil')
        

    #Paint method to draw on user input
    def paint(self,e):
        if self.oldx and self.oldy:
            self.c.create_line(self.oldx,self.oldy,e.x,e.y,width = self.width,fill = self.fg , capstyle = ROUND ,smooth = True)
        self.oldx = e.x
        self.oldy = e.y
    
    #Sets the cursor to inital state
    def reset(self,e):
        self.oldx = None
        self.oldy = None

    #Choose eraser
    def set_eraser(self):
        self.win.config(cursor = 'dot')
        self.fg = self.bg
    #Choose brush
    def set_brush(self):
        self.win.config(cursor = 'pencil')
        self.fg = 'black' 
        
    #Choose brush size by hotkey detection
    # + for increasing and - for decreasing
    def bsize(self,e):
        if(e.char == '+'):
            self.width += 5  
        else:
            self.width -= 5
            if(self.width < 0):
                self.width = 1
    
    #Setting the Brush color
    def getPenColor(self):
        color = colorchooser.askcolor()
        if color != None:
            self.fg = (str(color)[-9:-2])

    #Fill tool 
    def fillbg(self):
        color = colorchooser.askcolor()
        if color != None:
            self.bg = (str(color)[-9:-2])
        self.c.config(background = self.bg)
    
    #Clears the content of the screen
    def clear(self):
        self.c.config(background = 'white')
        self.bg = 'white'
        self.c.delete(ALL)
    
    #Utility function for palette
    def setfg(self,color):
        self.fg = color
        

    #Method to dislpay all the sub widgets on the canvas    
    def draw(self):
        
        def load():
            filename = askopenfilename()
            img = Image.open(filename)
            self.c.image = ImageTk.PhotoImage(img)
            self.c.create_image(0,0, image = self.c.image, anchor = 'nw')
        
        #Save function
        def write(canvas,fileName):
            canvas.postscript(file = fileName + '.eps') 
            img = PIL.Image.open(fileName + '.eps') 
            img.save(fileName + '.png', 'png') 
         
        
        def save():
            filename = asksaveasfilename(title="Save Pictures As...")
            self.c.postscript(file = filename + '.eps') 
            img = Image.open(filename + '.eps') 
            img.save(filename + '.png', 'png')
            img.close()
            os.remove(filename + '.eps')


        #Menu bar
        bar = Menu(self.win)
        bar.add_cascade(label="New", command = self.clear)
        bar.add_cascade(label="Open",command = load)
        bar.add_cascade(label="Save as",command = save)
        self.win.config(menu=bar)
        
        #Canvas
        self.c = Canvas(self.win,width = 800,height = 600,bg = self.bg)
        self.c.pack(side=LEFT)
        
        #Sidebar
        self.sideBar = Frame(self.win, padx=5, pady=5,height = 600,width = 350)
        self.sideBar.pack(side=RIGHT, fill=BOTH)
       
        #Buttons
        self.b1 = ttk.Button(self.sideBar,text = 'Exit',command = self.win.destroy)
        self.b1.pack()
        self.b2 = ttk.Button(self.sideBar,text = 'Clear',command = self.clear)
        self.b2.pack()
        
        self.eraser = ttk.Button(self.sideBar,text = 'Eraser',command = self.set_eraser)
        self.eraser.pack()
        self.brush = ttk.Button(self.sideBar,text = 'Brush',command = self.set_brush)
        self.brush.pack()
        
        self.color = ttk.Button(self.sideBar, text = "Pen Color" ,command=self.getPenColor)
        self.color.pack()
        
        self.fill = ttk.Button(self.sideBar, text = "Fill BG", command=self.fillbg)
        self.fill.pack()
        
        
        #Color Pallete
        self.colors = Canvas(self.sideBar,width = 320,height = 200 , bg = 'white')
        self.colors.pack(pady = 80)
            
        self.red = Button(self.colors,text = " " ,background = 'red' , height = 1,width = 1,command = lambda : self.setfg('red'))
        self.red.grid(row = 1,column = 1,padx = 5)
        
        self.red = Button(self.colors,text = " " ,background = 'blue' , height = 1,width = 1,command = lambda :self.setfg('blue'))
        self.red.grid(row = 1,column = 2,padx = 5)
        
        self.red = Button(self.colors,text = " " ,background = 'yellow', height = 1,width = 1,command =lambda : self.setfg('yellow'))
        self.red.grid(row = 1,column = 3,pady = 4)
        
        self.red = Button(self.colors,text = " " ,background = 'green', height = 1,width = 1,command =lambda : self.setfg('green'))
        self.red.grid(row = 2,column = 1)
        
        self.red = Button(self.colors,text = " " ,background = 'black', height = 1,width = 1,command =lambda : self.setfg('black'))
        self.red.grid(row = 2,column = 2)
        
        self.red = Button(self.colors,text = " " ,background = 'orange', height = 1,width = 1,command =lambda : self.setfg('orange'))
        self.red.grid(row = 2,column = 3,pady = 4)
        
        self.red = Button(self.colors,text = " " ,background = 'misty rose' , height = 1,width = 1,command =lambda : self.setfg('misty rose'))
        self.red.grid(row = 3,column = 1)
        
        self.red = Button(self.colors,text = " " ,background = 'indian red' , height = 1,width = 1,command =lambda : self.setfg('indian red'))
        self.red.grid(row = 3,column = 2)
        
        self.red = Button(self.colors,text = " " ,background = 'red4', height = 1,width = 1,command =lambda : self.setfg('red4'))
        self.red.grid(row = 3,column = 3,pady = 4)
        
        self.red = Button(self.colors,text = " " ,background = 'lime green', height = 1,width = 1,command =lambda : self.setfg('lime green'))
        self.red.grid(row = 4,column = 1)
        
        self.red = Button(self.colors,text = " " ,background = 'gold2', height = 1,width = 1,command = lambda : self.setfg('gold2'))
        self.red.grid(row = 4,column = 2)
        
        self.red = Button(self.colors,text = " " ,background = 'gray44', height = 1,width = 1,command =lambda : self.setfg('gray44'))
        self.red.grid(row = 4,column = 3,padx = 5,pady = 4)
        
#Main program to run the application
if __name__ == '__main__':
    win = Tk()
    main(win)
    win.title('PyPaint')
    win.mainloop()