#Q1
from tkinter import *

class Spinner:
    def __init__(self,root):
        self.window = root
        self.numcount = 0
        root.title("Spinner")

        self.label = Label(root,text=self.numcount,height=10,width=10)
        self.label.pack()

        self.plusbutt = Button(root,text="+",height=5,width=5,command= self.addcom)
        self.plusbutt.pack()

        self.minubutt = Button(root, text="-", height=5, width=5,command= self.minuscom)
        self.minubutt.pack()

        self.resetbutt = Button(root, text="reset", height=5, width=5,command= self.resetcom)
        self.resetbutt.pack()

    def addcom(self):
        self.numcount += 1
        self.label["text"] = self.numcount

    def minuscom(self):
        self.numcount -= 1
        self.label["text"] = self.numcount

    def resetcom(self):
        self.numcount = 0
        self.label["text"] = self.numcount

root = Tk()
gui = Spinner(root)
root.mainloop()

#Q2
from tkinter import *
import tkinter.messagebox

class CC:
    def __init__(self,root):
        self.window = root
        self.money = IntVar()
        root.title("Currency Converter")

        self.box = Entry(root, width = 10,textvariable= self.money)
        self.box.pack()

        self.utbutt = Button(root,width = 10,height = 5,text = "USD -> THB",command=self.conut)
        self.utbutt.pack()

        self.tubutt = Button(root,width = 10,height = 5,text = "THB -> USD",command=self.contu)
        self.tubutt.pack()

    def conut(self):
        usd = int(self.money.get())
        thb = int(self.money.get())
        thb *= 30.00
        tkinter.messagebox.showinfo("USD -> THB",f"{usd:.2f} USD = {thb:.2f} THB")

    def contu(self):
        thb = int(self.money.get())
        usd = int(self.money.get())
        usd /= 30.00
        tkinter.messagebox.showinfo("USD -> THB",f"{thb:.2f} THB = {usd:.2f} USD")

root = Tk()
gui = CC(root)
root.mainloop()

#Q3
from tkinter import *
class Paint:
   def __init__(self,root):

       self.window = root

       self.canvas = Canvas(root, width = 300, height = 200)
       self.canvas.pack()

       self.label = Label(root, text = "Drag the mouse to draw")
       self.label.pack()

       self.button = Button(root,bg="grey",width = 30, text = "Clear",command = self.clear)
       self.button.pack()

       self.canvas.bind("<B1-Motion>",self.mouseEvent)

   def mouseEvent(self,event):

       black = "#000000"
       x1 = event.x - 1
       y1 = event.y - 1
       x2 = event.x + 1
       y2 = event.y + 1
       self.canvas.create_oval(x1,y1,x2,y2,fill = black)

   def clear(self):
       self.canvas.delete("all")

root = Tk()
gui = Paint(root)
root.mainloop()

#Q4
from tkinter import *
import tkinter.messagebox
import random

class Paint:

   def __init__(self,root):

       self.window = root
       self.window["bg"] = "Dark grey"
       self.window.geometry("500x250")

       self.canvas = Canvas(root, width = 350, height = 200,highlightthickness=1, highlightbackground="black")
       self.canvas.pack()

       self.label = Label(root, text = "Click the mouse to draw")
       self.label.pack()

       self.button = Button(root,width = 30, text = "Clear",command = self.clear)
       self.button.pack()

       self.canvas.bind("<Button-1>",self.mouseEvent)

   def mouseEvent(self,event):

       color = ['black','red','green','blue','cyan','yellow','magenta']
       x1 = event.x
       y1 = event.y
       x2 = event.x
       y2 = event.y
       print(f"x1 = {x1}\ny1 = {y1}\nx2 = {x2}\ny2 = {y2}\n")
       if (5 <= x1 < 350 >= 5 and 5 <= y1 < 200 and x2 < 350 and 5 <= y2 < 200):
           x1 -= 5
           y1 -= 5
           x2 += 5
           y2 += 5
       else:
           tkinter.messagebox.showinfo("Warning","Mouse pointer is not in the rectangle")
       self.canvas.create_oval(x1,y1,x2,y2,fill = color[random.randint(0,6)])

   def clear(self):
       self.canvas.delete("all")

root = Tk()
gui = Paint(root)
root.mainloop()
