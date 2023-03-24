from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
from train import Train
from face_recognition import Face_recognition
from attendance import Attendance
from developer import Developer
import os
from help import Help
import tkinter
from time import strftime
from datetime import datetime


class Face_Recognition_system:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face_Recognition_system")
        
        #Image 1

        i1 = Image.open(r"images\i1.jfif")
        i1 = i1.resize((550,130),Image.ANTIALIAS)
        self.photoi1 = ImageTk.PhotoImage(i1)

        f_lbl = Label(self.root,image=self.photoi1)
        f_lbl.place(x=0,y=0,width=550,height=130)
        
        #Image 2
        
        i2 = Image.open(r"images\i2.jfif")
        i2 = i2.resize((150,130),Image.ANTIALIAS)
        self.photoi2 = ImageTk.PhotoImage(i2)

        f_lbl = Label(self.root,image=self.photoi2)
        f_lbl.place(x=550,y=0,width=150,height=130)
        
        #Image 3
        
        i3 = Image.open(r"images\i3.jpg")
        i3 = i3.resize((300,130),Image.ANTIALIAS)
        self.photoi3 = ImageTk.PhotoImage(i3)

        f_lbl = Label(self.root,image=self.photoi3)
        f_lbl.place(x=700,y=0,width=300,height=130)
        
        #Image 4
        
        i4 = Image.open(r"images\i4.jfif")
        i4 = i4.resize((550,130),Image.ANTIALIAS)
        self.photoi4 = ImageTk.PhotoImage(i4)

        f_lbl = Label(self.root,image=self.photoi4)
        f_lbl.place(x=1000,y=0,width=550,height=130)
        
        #BG Image
        
        i5 = Image.open(r"images\u1.jpg")
        i5 = i5.resize((1540,710),Image.ANTIALIAS)
        self.photoi5 = ImageTk.PhotoImage(i5)

        b_lbl = Label(self.root,image=self.photoi5)
        b_lbl.place(x=0,y=130,width=1540,height=710)
        
        title_lbl = Label(b_lbl, text = "Facial Recognition Attendance Management System", font=("times new roman",34,'bold'),bg='white', fg ='red')
        title_lbl.place(x=0,y=0,width=1540,height=46)
        
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000,time)
            
        lbl = Label(title_lbl,font = ('times new roman',18,'bold'),background='white',foreground='black')
        lbl.place(x=0,y=0,width=130,height=50)
        time()
        
        #Button 1 (student details)
        
        i6 = Image.open(r"images\sd.jfif")
        i6 = i6.resize((220,220),Image.ANTIALIAS)
        self.photoi6 = ImageTk.PhotoImage(i6)

        b1 = Button(b_lbl, image = self.photoi6,cursor='hand2', command=self.student_details)
        b1.place(x=200,y=100,width=220,height=220)
        
        b1_1= Button(b_lbl, text = "Student Details", cursor='hand2', font=("times in roman",13,"bold"),command=self.student_details)
        b1_1.place(x=200,y=300,width=220,height=40)
        
        #Button 2
        
        i7 = Image.open(r"images\fd.jfif")
        i7 = i7.resize((220,220),Image.ANTIALIAS)
        self.photoi7 = ImageTk.PhotoImage(i7)

        b1 = Button(b_lbl, command= self.face_data,image = self.photoi7,cursor='hand2')
        b1.place(x=500,y=100,width=220,height=220)
        
        b1_1= Button(b_lbl, command= self.face_data, text = "Face Recognition", cursor='hand2', font=("times in roman",13,"bold"))
        b1_1.place(x=500,y=300,width=220,height=40)
        
        #Button 3
        
        i8 = Image.open(r"images\at.jfif")
        i8 = i8.resize((220,220),Image.ANTIALIAS)
        self.photoi8 = ImageTk.PhotoImage(i8)

        b1 = Button(b_lbl, image = self.photoi8,cursor='hand2', command=self.attendance_sys)
        b1.place(x=800,y=100,width=220,height=220)
        
        b1_1= Button(b_lbl, text = "Attendance", cursor='hand2',command=self.attendance_sys, font=("times in roman",13,"bold"))
        b1_1.place(x=800,y=300,width=220,height=40)
        
        #Button 4
        
        i9 = Image.open(r"images\hd.jfif")
        i9 = i9.resize((220,220),Image.ANTIALIAS)
        self.photoi9 = ImageTk.PhotoImage(i9)

        b1 = Button(b_lbl,command=self.Help_func , image = self.photoi9,cursor='hand2')
        b1.place(x=1100,y=100,width=220,height=220)
        
        b1_1= Button(b_lbl, text = "Help",command=self.Help_func, cursor='hand2', font=("times in roman",13,"bold"))
        b1_1.place(x=1100,y=300,width=220,height=40)
        
        
        #Button 5
        
        i10 = Image.open(r"images\train.jfif")
        i10 = i10.resize((220,220),Image.ANTIALIAS)
        self.photoi10 = ImageTk.PhotoImage(i10)

        b1 = Button(b_lbl,command=self.train_data, image = self.photoi10,cursor='hand2')
        b1.place(x=200,y=400,width=220,height=220)
        
        b1_1= Button(b_lbl,command=self.train_data, text = "Train Data", cursor='hand2', font=("times in roman",13,"bold"))
        b1_1.place(x=200,y=600,width=220,height=40)
        
        #Button 6
        
        i11 = Image.open(r"images\photo.jfif")
        i11 = i11.resize((220,220),Image.ANTIALIAS)
        self.photoi11 = ImageTk.PhotoImage(i11)

        b1 = Button(b_lbl, image = self.photoi11,cursor='hand2',command=self.open_img)
        b1.place(x=500,y=400,width=220,height=220)
        
        b1_1= Button(b_lbl, text = "Photos", command=self.open_img,cursor='hand2', font=("times in roman",13,"bold"))
        b1_1.place(x=500,y=600,width=220,height=40)
        
        #Button 7
        
        i12 = Image.open(r"images\developer.jfif")
        i12 = i12.resize((220,220),Image.ANTIALIAS)
        self.photoi12 = ImageTk.PhotoImage(i12)

        b1 = Button(b_lbl, image = self.photoi12, command = self.Dev_data,cursor='hand2')
        b1.place(x=800,y=400,width=220,height=220)
        
        b1_1= Button(b_lbl, text = "Developer", command = self.Dev_data, cursor='hand2', font=("times in roman",13,"bold"))
        b1_1.place(x=800,y=600,width=220,height=40)
        
        #Button 8
        
        i13 = Image.open(r"images\exit.jfif")
        i13 = i13.resize((220,220),Image.ANTIALIAS)
        self.photoi13 = ImageTk.PhotoImage(i13)

        b1 = Button(b_lbl,command = self.Exit_func, image = self.photoi13,cursor='hand2')
        b1.place(x=1100,y=400,width=220,height=220)
        
        b1_1= Button(b_lbl,command = self.Exit_func, text = "Exit", cursor='hand2', font=("times in roman",13,"bold"))
        b1_1.place(x=1100,y=600,width=220,height=40)
        
    def open_img(self):
        os.startfile("data")
        
        
        
        
    # ==== Function =====

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)


    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)
        
    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_recognition(self.new_window)
        
    def attendance_sys(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)
        
    def Dev_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)
        
    def Help_func(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)
        
    def Exit_func(self):
        self.exit = tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project",parent = self.root)
        if self.exit > 0:
            self.root.destroy()
        else:
            return


















if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_system(root)
    root.mainloop()

