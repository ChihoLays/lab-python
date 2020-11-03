from tkinter import *
import tkinter.messagebox
class KMITL_PHONE:
    def __init__(self,root):
        self.window = root
        root.geometry("233x390")
        root.title("KMITL Phone")
        root.configure(bg="Darkgrey")
        self.phonenum = []
        self.displaybox = Label(root, width=31, text="".join(self.phonenum), bg="White")
        self.displaybox.place(x=5, y=5)
        self.butt_1 = Button(root, text="1", width= 9, height=4, command= lambda:self.addsome("1"))
        self.butt_1.place(x=5, y=28)
        self.butt_2 = Button(root, text="2", width=9, height=4, command= lambda:self.addsome("2"))
        self.butt_2.place(x=80, y=28)
        self.butt_3 = Button(root, text="3", width=9, height=4, command= lambda:self.addsome("3"))
        self.butt_3.place(x=155, y=28)
        self.butt_4 = Button(root, text="4", width=9, height=4, command= lambda:self.addsome("4"))
        self.butt_4.place(x=5, y=100)
        self.butt_5 = Button(root, text="5", width=9, height=4, command= lambda:self.addsome("5"))
        self.butt_5.place(x=80, y=100)
        self.butt_6 = Button(root, text="6", width=9, height=4, command= lambda:self.addsome("6"))
        self.butt_6.place(x=155, y=100)
        self.butt_7 = Button(root, text="7", width=9, height=4, command= lambda:self.addsome("7"))
        self.butt_7.place(x=5, y=172)
        self.butt_8 = Button(root, text="8", width=9, height=4, command= lambda:self.addsome("8"))
        self.butt_8.place(x=80, y=172)
        self.butt_9 = Button(root, text="9", width=9, height=4, command= lambda:self.addsome("9"))
        self.butt_9.place(x=155, y=172)
        self.butt_star = Button(root, text="*", width=9, height=4, command= lambda:self.addsome("*"))
        self.butt_star.place(x=5, y=245)
        self.butt_0 = Button(root, text="0", width=9, height=4, command= lambda:self.addsome("0"))
        self.butt_0.place(x=80, y=245)
        self.butt_sharp = Button(root, text="#", width=9, height=4, command= lambda:self.addsome("#"))
        self.butt_sharp.place(x=155, y=245)
        self.talk_butt = Button(root, text="Talk", width=14, height=4,command=self.calling)
        self.talk_butt.place(x=5, y=316)
        self.del_butt = Button(root, text="<", width=15, height=4,command=self.delete_right)
        self.del_butt.place(x=115, y=316)

    def addsome(self,data):
        self.phonenum.append(data)
        self.displaybox['text'] = "".join(self.phonenum)

    def delete_right(self):
        self.phonenum.remove(self.phonenum[-1])
        self.displaybox['text'] = "".join(self.phonenum)

    def calling(self):
        tkinter.messagebox.showinfo("KMITL Phone",f"Dialling<<{''.join(self.phonenum)}>>")

root = Tk()
gui = KMITL_PHONE(root)
root.mainloop()
