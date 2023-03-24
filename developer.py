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


class Developer:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Developer Details")
        
        
        title_lbl = Label(self.root, text = "DEVELOPER", font=("times new roman",34,'bold'),bg='white', fg ='blue')
        title_lbl.place(x=0,y=0,width=1530,height=45)

        
        image_top = Image.open(r"images\d.webp")
        image_top = image_top.resize((1530,720),Image.ANTIALIAS)
        self.photoimage_top = ImageTk.PhotoImage(image_top)

        f_lbl = Label(self.root,image=self.photoimage_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)


        #frame
        main_frame = Frame(f_lbl, bd = 2)
        main_frame.place(x = 0, y =0 ,width=500, height = 600)
        
           
        img_top = Image.open(r"images\b.jfif")
        img_top = img_top.resize((200,200),Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(main_frame,image=self.photoimg_top)
        f_lbl.place(x=0,y=0,width=200,height=200)
       
       #Developer info
        
        D_lbl = Label(main_frame,text = "Hello Everyone,\nMy name is Bhavya Bansal \n I am a Software Developer \n and currently pursuing \n my B.Tech from \n B.S.A.C.E.T", font = ("times new roman",18,"bold"))
        D_lbl.place(x=200,y=5)
        
        '''D_lbl = Label(main_frame,text = "I am Software Developer", font = ("times new roman",16,"bold"), bg="white")
        D_lbl.place(x=0,y=50)'''
        
        i1 = Image.open(r"images\college.jfif")
        i1 = i1.resize((500,400),Image.ANTIALIAS)
        self.photoi1 = ImageTk.PhotoImage(i1)

        f_lbl = Label(main_frame,image=self.photoi1)
        f_lbl.place(x=0,y=200,width=500,height=400)
    
        
if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()