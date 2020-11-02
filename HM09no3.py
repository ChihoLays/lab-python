from tkinter import *
class CreateCircle:
    def __init__(self,root):
        self.window = root
        self.window.resizable (0, 0)
        self.frame = Canvas(width = 500, height = 350)
        self.frame .pack ()
        self.frame.bind ("<Button-1>", self.leftclick)
        self.frame.bind("<Button-3>",self.rightClick)
        self.frame.pack ()

    def leftclick(self,pos) :
        x = pos.x
        y = pos.y
        self.frame.create_oval (x-20,y-20,x+20,y+20,fill='white')

    def rightClick (self,pos) :
        x = pos.x
        y = pos.y
        self.frame.delete(self.frame.delete(self.frame.find_closest(x,y)))

root = Tk()
CreateCircle(root)
root.mainloop()
