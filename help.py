from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import mysql.connector
import os
import csv
from tkinter import filedialog


class Help:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Help Details")
        
        title_lbl = Label(self.root, text = "Help Desk", font=("times new roman",34,'bold'),bg='white', fg ='blue')
        title_lbl.place(x=0,y=0,width=1530,height=45)

        
        image_top = Image.open(r"images\t1.jpg")
        image_top = image_top.resize((1530,720),Image.ANTIALIAS)
        self.photoimage_top = ImageTk.PhotoImage(image_top)

        f_lbl = Label(self.root,image=self.photoimage_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)

        D_lbl = Label(f_lbl,text = "Email: bhavyabansal4321@gmail.com", font = ("times new roman",20,"bold"), bg="black",fg = "white")
        D_lbl.place(x=550,y=300)
        
        
if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()