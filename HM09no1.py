from tkinter import *
class KMITL_PHONE:
    def __init__(self,root):
        self.window = root
        root.geometry("175x148")
        root.title("KMITL Phone")
        root.resizable(0, 0)
        self.phonenum = []

        self.displaybox = Label(root,width=25,text="".join(self.phonenum),bg="White")
        self.displaybox.place(x=0,y=0)
        self.butt_1 = Button(root, text="1", width=7, height=2)
        self.butt_1.place(x=0,y=21)
        self.butt_2 = Button(root, text="2", width=7, height=2)
        self.butt_2.place(x=60,y=21)
        self.butt_3 = Button(root, text="3", width=7, height=2)
        self.butt_3.place(x=120,y=21)
        self.butt_4 = Button(root, text="4",width=7, height=2)
        self.butt_4.place(x=0,y=63)
        self.butt_5 = Button(root, text="5", width=7, height=2)
        self.butt_5.place(x=60,y=63)
        self.butt_6 = Button(root, text="6", width=7, height=2)
        self.butt_6.place(x=120,y=63)
        self.butt_7 = Button(root, text="7", width=7, height=2)
        self.butt_7.place(x=0,y=105)
        self.butt_8 = Button(root, text="8", width=7, height=2)
        self.butt_8.place(x=60,y=105)
        self.butt_9 = Button(root, text="9", width=7, height=2)
        self.butt_9.place(x=120,y=105)


root = Tk()
gui = KMITL_PHONE(root)
root.mainloop()
