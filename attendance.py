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


mydata = []
class Attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance Details")
        
        
        # === 
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()
        
        
        #Image 1

        i1 = Image.open(r"images\sd.jfif")
        i1 = i1.resize((800,200),Image.ANTIALIAS)
        self.photoi1 = ImageTk.PhotoImage(i1)

        f_lbl = Label(self.root,image=self.photoi1)
        f_lbl.place(x=0,y=0,width=800,height=200)
        
        #Image 2
        
        i2 = Image.open(r"images\st1.png")
        i2 = i2.resize((800,200),Image.ANTIALIAS)
        self.photoi2 = ImageTk.PhotoImage(i2)

        f_lbl = Label(self.root,image=self.photoi2)
        f_lbl.place(x=800,y=0,width=800,height=200)
        
        i5 = Image.open(r"C:\Users\bhavy\OneDrive\Pictures\1550175402868.jpg")
        i5 = i5.resize((1530,710),Image.ANTIALIAS)
        self.photoi5 = ImageTk.PhotoImage(i5)

        b_lbl = Label(self.root, background="black")
        b_lbl.place(x=0,y=130,width=1530,height=710)
        
        title_lbl = Label(b_lbl, text = "Attandance Management System", font=("times new roman",34,'bold'),bg='white', fg ='dark green')
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        main_frame = Frame(b_lbl, bd = 2)
        main_frame.place(x = 10, y =55 ,width=1500, height = 600)
        
        #Left Lable Frame
        
        llf = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Attendance details", font = ("times new roman",13,"bold"), bg="white", fg= "red")
        llf.place(x=10,y=10,width=730,height=580)
        
        
        img_left = Image.open(r"images\c1.jfif")
        img_left = img_left.resize((720,200),Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(llf,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=200)
        
        left_inside_frame = Frame(llf, bd = 2,bg="white", relief=RIDGE)
        left_inside_frame.place(x = 0, y =205 ,width=720, height = 370)
        
        #Attendance ID 
         
        s_id = Label(left_inside_frame,text="AttendanceID:", font = ("times new roman",13,"bold"), bg="white")
        s_id.grid(row = 0 , column=0, padx =10, pady = 5, sticky=W)
        
        AttendanceId_entry = ttk.Entry(left_inside_frame,textvariable = self.var_atten_id,width=20,font=("times new roman",13,"bold"))
        AttendanceId_entry.grid(row=0, column=1, padx = 10, pady = 5, sticky=W)
        
        #RollNo
         
        roll = Label(left_inside_frame,text="Roll:", font = ("times new roman",13,"bold"), bg="white")
        roll.grid(row = 0 , column=2, padx =10, pady = 5, sticky=W)
        
        roll_entry = ttk.Entry(left_inside_frame,textvariable = self.var_atten_roll,width=20,font=("times new roman",13,"bold"))
        roll_entry.grid(row=0, column=3, padx = 10, pady = 5, sticky=W)
        
        #Name 
         
        name = Label(left_inside_frame,text="Name:", font = ("times new roman",13,"bold"), bg="white")
        name.grid(row = 1 , column=0, padx =10, pady = 5, sticky=W)
        
        name_entry = ttk.Entry(left_inside_frame,textvariable = self.var_atten_name,width=20,font=("times new roman",13,"bold"))
        name_entry.grid(row=1, column=1, padx = 10, pady = 5, sticky=W)
        
        
        #Department 
         
        Dep = Label(left_inside_frame,text="Department:", font = ("times new roman",13,"bold"), bg="white")
        Dep.grid(row = 1 , column=2, padx =10, pady = 5, sticky=W)
        
        Dep_entry = ttk.Entry(left_inside_frame,width=20,textvariable = self.var_atten_dep,font=("times new roman",13,"bold"))
        Dep_entry.grid(row=1, column=3, padx = 10, pady = 5, sticky=W)
        
        #Time 
         
        Time = Label(left_inside_frame,text="Time:", font = ("times new roman",13,"bold"), bg="white")
        Time.grid(row = 2 , column=0, padx =10, pady = 5, sticky=W)
        
        Time_entry = ttk.Entry(left_inside_frame,textvariable = self.var_atten_time,width=20,font=("times new roman",13,"bold"))
        Time_entry.grid(row=2, column=1, padx = 10, pady = 5, sticky=W)

        #Date
         
        date = Label(left_inside_frame,text="Date:", font = ("times new roman",13,"bold"), bg="white")
        date.grid(row = 2 , column=2, padx =10, pady = 5, sticky=W)
        
        date_entry = ttk.Entry(left_inside_frame,width=20,textvariable = self.var_atten_date,font=("times new roman",13,"bold"))
        date_entry.grid(row=2, column=3, padx = 10, pady = 5, sticky=W)
        
        #attendance
        
        attendance_lbl = Label(left_inside_frame,text="Class Division", font = ("times new roman",13,"bold"), bg="white")
        attendance_lbl.grid(row = 3 , column=0, padx =8)
        
        self.attancance_status = ttk.Combobox(left_inside_frame,textvariable = self.var_atten_attendance,font = ("times new roman",13,"bold"), state="read only", width=18)
        self.attancance_status["values"] = ("Status","Present","Absent")
        self.attancance_status.grid(row = 3 , column=1, pady = 8)
        self.attancance_status.current(0)
        
        #button frame
        
        btn_frame = LabelFrame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0,y=280,width=715,height=200)
        
        save_btn = Button(btn_frame,text="Import csv",width = 35,command= self.importCsv , font = ("times new roman",13,"bold"), bg="blue", fg="white")
        save_btn.grid(row=1,column=0)
        
        update_btn = Button(btn_frame,text="Export_csv",width = 35,command = self.exportCsv,font = ("times new roman",13,"bold"), bg="blue", fg="white")
        update_btn.grid(row=1,column=1)
        
        delete_btn = Button(btn_frame,text="Show_Attendance_CSV",command = self.showcsv,width = 35,font = ("times new roman",13,"bold"), bg="blue", fg="white")
        delete_btn.grid(row=2,column=0)
        
        reset_btn = Button(btn_frame,command = self.reset_data,text="Reset",width = 35,font = ("times new roman",13,"bold"), bg="blue", fg="white")
        reset_btn.grid(row=2,column=1)
        
        #Right Lable Frame
        
        rlf = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Attendance Details", font = ("times new roman",12,"bold"), bg="white")
        rlf.place(x=750,y=10,width=720,height=580)
         
        
        table_frame = LabelFrame(rlf, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5,y=5,width=700,height=550)
        
        # === scroll bar ===
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.AttendanceReportTable = ttk.Treeview(table_frame,column = ("id","roll","name","department","time","date","attendance"), xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)


        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"] = "headings"
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)



        
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    # === fetch data ====
        
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
            
    def showcsv(self):
        with open("attandance.csv") as myfile:
            csvread = csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV", filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
            
            
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln = filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV", filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write = csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(fln)+"successfully")
        except Exception as ex:
            messagebox.showerror("Error",f"Due To:{str(ex)}",parent=self.root)
        
    def get_cursor(self, event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        row = content["values"]
        self.var_atten_id.set(row[0])
        self.var_atten_roll.set(row[1])
        self.var_atten_name.set(row[2])
        self.var_atten_dep.set(row[3])
        self.var_atten_time.set(row[4])
        self.var_atten_date.set(row[5])
        self.var_atten_attendance.set(row[6])
        
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")
        
if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()