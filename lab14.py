import os
import pickle
import string
from tkinter import *
from tkinter import filedialog

print("A URL Favourite Manager")
print("Press + to add new URL (no repeating URLs Are stored in the list).")
print("Press - to delete a URL.")
print("Press i to get a URL by specifying its index of the list.")
print("Press s to save all URL to a file.")
print("Press l to load previous saved URL from a file.")
print("Press p to print out all URLs in the list.")
print("Press q to quit the program.")

url_list = []

cmd = input("Enter command: ")
cmd = cmd.lower()

while( cmd != 'q' ):
    if(cmd == "+"):
        url = input("Enter URL: ")
        if(url in url_list):
            print("URL already exist in the list.")
        else:
            url_list.append(url)

    elif(cmd == "-"):
        for index in range(len(url_list)):
            print(f"{index}: {url_list[index]}\n")
        del_index = int(input("Enter which URL to delete: "))
        try:
            del url_list[del_index]
        except IndexError:
            print("Index out of range!")

    elif(cmd == "f"):
        find = int(input("Enter index: "))
        try:
            print(url_list[find])
        except IndexError:
            print("URL not found!")

    elif(cmd == "s"):
        root = Tk()
        root.file = filedialog.asksaveasfilename()

        if os.path.isfile(root.file):
            raise FileExistsError("File Already Exist!")
        else:
            urlfile = open(root.file, "wb")
            pickle.dump(url_list, urlfile)
            print("File saved!")
            urlfile.close()

    elif(cmd == "l"):
        count = 0
        while True:
            root = Tk()
            root.file = filedialog.askopenfilename()
            try:
                if not os.path.exists(root.file):
                    raise FileNotFoundError("The file doesn't exist")
                urlfile = open(root.file, "rb")
                url_list = pickle.load(urlfile)
                urlfile.close()
                break
            except FileNotFoundError as err:
                print(err)

    elif(cmd == "p"):
        for index in range(len(url_list)):
            print(f"{index}: {url_list[index]}\n")
    else:
        print("Unknown Command")
    cmd = str(input("Enter command: "))

class TimeSettingError(RuntimeError):
    def __init__(self,h,m,s):
        super().__init__()
        self.h = h
        self.m = m
        self.s = s
    def __str__(self):
        error = ""
        if type(self.h) == float:
            error += "The Hour should be int not float\n"
        elif type(self.h) == str:
            error += "The Hour should be int not string\n"
        elif self.h < 0 or self.h > 23:
            error += "The Hour should be 0 <= hr <= 23\n"
        if type(self.m) == float:
            error += "The Minute should be int not float\n"
        elif type(self.m) == str:
            error += "The Minute should be int not string\n"
        elif self.m < 0 or self.m > 59:
            error += "The Minute should be 0 <= min <= 59\n"
        if type(self.s) == float:
            error += "The Second should be int not float\n"
        elif type(self.s) == str:
            error += "The Second hould be int not string\n"
        elif self.s < 0 or self.s > 59:
            error += "The Second should be 0 <= sec <= 59\n"
        return error

class Time:
    def __init__(self,hh,mm,ss):
        self.setTime(hh,mm,ss)

    def setTime(self,h,m,s):
        try:
            if (type(h) == float or type(m) == float or type(s) == float):
                        raise TimeSettingError(h,m,s)

            elif (h < 0 or h > 23 or m < 0 or m >59 or s < 0 or s > 59):
                    raise TimeSettingError(h,m,s)
            else:
                    self.hh = h
                    self.mm = m
                    self.ss = s
        except TypeError:
            raise TimeSettingError(h,m,s)
        except TimeSettingError as err:
            print(err)
    def __str__(self):
        return f"{self.hh:02d}:{self.mm:02d}:{self.ss:02d} Hrs."

try:
    time1 = Time(20, 20, 20)
except TimeSettingError as err:
    print(err)
else:
    print(time1)



