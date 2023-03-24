from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import mysql.connector

class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Details")
        
        
        # varibles
        self.var_dep=StringVar()
        self.var_course=StringVar() 
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        
        #Image 1

        i1 = Image.open(r"images\s2.jfif")
        i1 = i1.resize((500,130),Image.ANTIALIAS)
        self.photoi1 = ImageTk.PhotoImage(i1)

        f_lbl = Label(self.root,image=self.photoi1)
        f_lbl.place(x=0,y=0,width=500,height=130)
        
        #Image 2
        
        i2 = Image.open(r"images\s1.jfif")
        i2 = i2.resize((500,130),Image.ANTIALIAS)
        self.photoi2 = ImageTk.PhotoImage(i2)

        f_lbl = Label(self.root,image=self.photoi2)
        f_lbl.place(x=500,y=0,width=500,height=130)
        
        '''#Image 3
        
        i3 = Image.open(r"images\s3.jpg")
        i3 = i3.resize((200,130),Image.ANTIALIAS)
        self.photoi3 = ImageTk.PhotoImage(i3)

        f_lbl = Label(self.root,image=self.photoi3)
        f_lbl.place(x=750,y=0,width=200,height=130)'''
        
        #Image 4
        
        i4 = Image.open(r"images\s4.jfif")
        i4 = i4.resize((550,130),Image.ANTIALIAS)
        self.photoi4 = ImageTk.PhotoImage(i4)

        f_lbl = Label(self.root,image=self.photoi4)
        f_lbl.place(x=1000,y=0,width=550,height=130)
        
        
        #BG Image
        
        i5 = Image.open(r"images\s6.jfif")
        i5 = i5.resize((1530,710),Image.ANTIALIAS)
        self.photoi5 = ImageTk.PhotoImage(i5)

        b_lbl = Label(self.root,fg="black",bg="black")
        b_lbl.place(x=0,y=130,width=1530,height=710)
        
        title_lbl = Label(b_lbl, text = "Student Management System", font=("times new roman",34,'bold'),bg='white', fg ='dark green')
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        
        main_frame = Frame(b_lbl, bd = 2)
        main_frame.place(x = 10, y =55 ,width=1500, height = 600)
        
        #Left Lable Frame
        
        llf = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Information", font = ("times new roman",13,"bold"), bg="white",fg="red")
        llf.place(x=10,y=10,width=730,height=580)
         
        #LEFT IMAGE
         
        img_left = Image.open(r"images\s9.jpg")
        img_left = img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(llf,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)
        
        #current Course
        
        curr_course = LabelFrame(llf, bd=2, relief=RIDGE, text="Current Course Information", font = ("times new roman",13,"bold"), bg="white",fg="green")
        curr_course.place(x=5,y=135,width=720,height=150)
        
        #Department label
        
        D_lbl = Label(curr_course,text="Department*", font = ("times new roman",13,"bold"), bg="white")
        D_lbl.grid(row = 0 , column=0, padx =10)
        
        deep_d = ttk.Combobox(curr_course,textvariable=self.var_dep, font = ("times new roman",13,"bold"), state="read only")
        deep_d["values"] = ("Select Department","IT","CS","Civil","Electrical","Mechanical")
        deep_d.current(0)
        deep_d.grid(row = 0 , column=1, padx = 2, pady = 10, sticky=W)
        
        #course
        
        c_lbl = Label(curr_course,text="Course", font = ("times new roman",13,"bold"), bg="white")
        c_lbl.grid(row = 0 , column=2, padx =10)
        
        deep_c = ttk.Combobox(curr_course,textvariable=self.var_course,font = ("times new roman",13,"bold"), state="read only")
        deep_c["values"] = ("Select Course","FE","SE","TE","BE")
        deep_c.current(0)
        deep_c.grid(row = 0 , column=3, padx = 2, pady = 10, sticky=W)
        
        #Year
        
        y_lbl = Label(curr_course,text="Year", font = ("times new roman",13,"bold"), bg="white")
        y_lbl.grid(row = 1 , column=0, padx =10)
        
        deep_y = ttk.Combobox(curr_course, textvariable=self.var_year,font = ("times new roman",13,"bold"), state="read only")
        deep_y["values"] = ("Select Year","2020-21","2021-22","2022-23","2023-24")
        deep_y.current(0)
        deep_y.grid(row = 1 , column=1, padx = 2, pady = 10, sticky=W)
        
        
        #semster
        
        s_lbl = Label(curr_course,text="Semester", font = ("times new roman",13,"bold"), bg="white")
        s_lbl.grid(row = 1 , column=2, padx =10)
        
        deep_s = ttk.Combobox(curr_course, textvariable=self.var_semester,font = ("times new roman",13,"bold"), state="read only")
        deep_s["values"] = ("Select Semester","Semester-1","Semester-2")
        deep_s.current(0)
        deep_s.grid(row = 1 , column=3, padx = 2, pady = 10, sticky=W)
        
        
        #class student information
        class_student_frame = LabelFrame(llf, bd=2, relief=RIDGE, text="Student Class Information", font = ("times new roman",13,"bold"), bg="white", fg="purple")
        class_student_frame.place(x=5,y=250,width=720,height=300)
        
        #student ID 
         
        s_id = Label(class_student_frame,text="StudentID*:", font = ("times new roman",13,"bold"), bg="white")
        s_id.grid(row = 0 , column=0, padx =10, pady = 5, sticky=W)
        
        studentId_entry = ttk.Entry(class_student_frame,textvariable=self.var_std_id ,width=20,font=("times new roman",13,"bold"))
        studentId_entry.grid(row=0, column=1, padx = 10, pady = 5, sticky=W)
        
        #student Name
         
        s_name = Label(class_student_frame,text="Student Name*:", font = ("times new roman",13,"bold"), bg="white")
        s_name.grid(row = 0 , column=2, padx =10, pady = 5, sticky=W)
        
        studentname_entry = ttk.Entry(class_student_frame,width=20,textvariable=self.var_std_name,font=("times new roman",13,"bold"))
        studentname_entry.grid(row=0, column=3, padx = 10, pady = 5, sticky=W)
                             
        #Class division 
         
        class_div = Label(class_student_frame,text="Class Division:", font = ("times new roman",13,"bold"), bg="white")
        class_div.grid(row = 1 , column=0, padx =10, pady = 5, sticky=W)
        
        #class_div_entry = ttk.Entry(class_student_frame,width=20,textvariable=self.var_div,font=("times new roman",13,"bold"))
        #class_div_entry.grid(row=1, column=1, padx = 10, pady = 5, sticky=W)
        
        dev_combo = ttk.Combobox(class_student_frame, textvariable=self.var_div,font = ("times new roman",13,"bold"), state="read only", width=18)
        dev_combo["values"] = ("A","B","C")
        dev_combo.current(0)
        dev_combo.grid(row = 1 , column=1, padx = 10, pady = 5, sticky=W)
        
        #RollNO
         
        roll_no = Label(class_student_frame,text="Roll No:", font = ("times new roman",13,"bold"), bg="white")
        roll_no.grid(row = 1 , column=2, padx =10, pady = 5, sticky=W)
        
        roll_no_entity = ttk.Entry(class_student_frame,width=20,textvariable=self.var_roll,font=("times new roman",13,"bold"))
        roll_no_entity.grid(row=1, column=3, padx = 10, pady = 5, sticky=W)   
        
        #Gender
         
        gender = Label(class_student_frame,text="Gender:", font = ("times new roman",13,"bold"), bg="white")
        gender.grid(row = 2 , column=0, padx =10, pady = 5, sticky=W)
        
        #gender_entity = ttk.Entry(class_student_frame,width=20,textvariable=self.var_gender,font=("times new roman",13,"bold"))
        #gender_entity.grid(row=3, column=1, padx = 10, pady = 5, sticky=W)   
        
        gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_gender,font = ("times new roman",13,"bold"), state="read only", width=18)
        gender_combo["values"] = ("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row = 2 , column=1, padx = 10, pady = 5, sticky=W)
        
        
        #DOB 
         
        DOB = Label(class_student_frame,text="DOB:", font = ("times new roman",13,"bold"), bg="white")
        DOB.grid(row = 2 , column=2, padx =10, pady = 5, sticky=W)
        
        DOB_entity = ttk.Entry(class_student_frame,width=20,textvariable=self.var_dob,font=("times new roman",13,"bold"))
        DOB_entity.grid(row=2, column=3, padx = 10, pady = 5, sticky=W)   
        
        #Email 
         
        Email = Label(class_student_frame,text="Email:", font = ("times new roman",13,"bold"), bg="white")
        Email.grid(row = 3 , column=0, padx =10, pady = 5, sticky=W)
        
        Email_entity = ttk.Entry(class_student_frame,width=20,textvariable=self.var_email,font=("times new roman",13,"bold"))
        Email_entity.grid(row=3, column=1, padx = 10, pady = 5, sticky=W)   
        
        #Phone NO
         
        Phone = Label(class_student_frame,text="Phone N0:", font = ("times new roman",13,"bold"), bg="white")
        Phone.grid(row = 3 , column=2, padx =10, pady = 5, sticky=W)
        
        Phone_entity = ttk.Entry(class_student_frame,width=20,textvariable=self.var_phone,font=("times new roman",13,"bold"))
        Phone_entity.grid(row=3, column=3, padx = 10, pady = 5, sticky=W)   
        
        #Address
         
        Address = Label(class_student_frame,text="Address:", font = ("times new roman",13,"bold"), bg="white")
        Address.grid(row = 4 , column=0, padx =10, pady = 5, sticky=W)
        
        Address_entity = ttk.Entry(class_student_frame,width=20,textvariable=self.var_address,font=("times new roman",13,"bold"))
        Address_entity.grid(row=4, column=1, padx = 10, pady = 5, sticky=W)            

        #Teacher Name
         
        Teacher = Label(class_student_frame,text="Class Teacher Name:", font = ("times new roman",13,"bold"), bg="white")
        Teacher.grid(row = 4 , column=2, padx =10, pady = 5, sticky=W)
        
        Teacher_entity = ttk.Entry(class_student_frame,width=20,textvariable=self.var_teacher,font=("times new roman",13,"bold"))
        Teacher_entity.grid(row=4, column=3, padx = 10, pady = 5, sticky=W)  
        
        #radio button
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(class_student_frame,text = "Take Photo Sample",variable=self.var_radio1, value = "Yes")
        radiobtn1.grid(row=5,column=0)

        radiobtn1 = ttk.Radiobutton(class_student_frame,text = "No Photo Sample",variable=self.var_radio1, value = "No")
        radiobtn1.grid(row=5,column=1)
        
        #button frame
        
        btn_frame = LabelFrame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=5,y=200,width=715,height=70)
        
        save_btn = Button(btn_frame,text="Save",width = 17,command = self.add_data,font = ("times new roman",13,"bold"), bg="blue", fg="white")
        save_btn.grid(row=1,column=0)
        
        update_btn = Button(btn_frame,text="Update",command= self.update_data,width = 17,font = ("times new roman",13,"bold"), bg="blue", fg="white")
        update_btn.grid(row=1,column=1)
        
        delete_btn = Button(btn_frame,text="Delete",command= self.delete_data,width = 17,font = ("times new roman",13,"bold"), bg="blue", fg="white")
        delete_btn.grid(row=1,column=3)
        
        reset_btn = Button(btn_frame,text="Reset",width = 17,command= self.reset_data,font = ("times new roman",13,"bold"), bg="blue", fg="white")
        reset_btn.grid(row=1,column=4)
        
        btn_frame2 = LabelFrame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame2.place(x=5,y=235,width=715,height=35)
        
        take_photo_btn = Button(btn_frame2,text="Take Photo Sample",command=self.genrate_dateset,width = 35,font = ("times new roman",13,"bold"), bg="blue", fg="white")
        take_photo_btn.grid(row=0,column=0)
        
        update_photo_btn = Button(btn_frame2,text="Update Photo Sample",width = 35,font = ("times new roman",13,"bold"), bg="blue", fg="white")
        update_photo_btn.grid(row=0,column=1)
        
        
        
        
        #Right Lable Frame
        
        rlf = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details", font = ("times new roman",13,"bold"), bg="white",fg="dark orange")
        rlf.place(x=750,y=10,width=720,height=580)
         
        # LEFT IMAGE
         
        img_right = Image.open(r"images\s10.jfif")
        img_right = img_right.resize((720,250),Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(rlf,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=720,height=250)
        
        
        #+=========search system ========
        
        search_frame = LabelFrame(rlf, bd=2, relief=RIDGE, text="View Student Details & Search System", font = ("times new roman",13,"bold"), bg="white", fg="purple")
        search_frame.place(x=5,y=250,width=710,height=70)
        
        searchby = Label(search_frame,text="Search By", font = ("times new roman",13,"bold"), bg="red", fg="white")
        searchby.grid(row = 0 , column=0, padx =10, pady = 5, sticky=W)
        
        search_combo = ttk.Combobox(search_frame, font = ("times new roman",13,"bold"), state="read only")
        search_combo["values"] = ("Select","Roll_No","Phone_No")
        search_combo.current(0)
        search_combo.grid(row = 0 , column=1, padx = 2, pady = 10, sticky=W)
        
        search_combo_entity = ttk.Entry(search_frame,width=12,font=("times new roman",13,"bold"))
        search_combo_entity.grid(row=0, column=2, padx = 10, pady = 5, sticky=W)  
        
        
        search_button = Button(search_frame,text="Search",width = 12,font = ("times new roman",13,"bold"), bg="blue", fg="white")
        search_button.grid(row=0,column=3,padx= 4)
        
        showall_button = Button(search_frame,text="Show All", command = self.fetch_data,width = 12,font = ("times new roman",13,"bold"), bg="blue", fg="white")
        showall_button.grid(row=0,column=4,padx= 4)
        
        
        # table frame
        
        table_frame = Frame(rlf, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5,y=320,width=710,height=250)
        
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table = ttk.Treeview(table_frame, column=("id","dep","course","year","sem","name","div","roll","gender","dob","email","phone","address","teacher","photo"))
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("gender", text = "Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"] = "headings"
        
        self.student_table.column("id",width=100)
        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo",width=150)     
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
    
    # function to add data
    
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get() == "":
            messagebox.showerror("Error","ALL fields are required", parent=self.root)
        else:
            # will add data in database
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
                my_cursor = conn.cursor()
                #messagebox.showinfo("Success",my_cursor,parent=self.root)
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_std_id.get(),
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
                
            except Exception as ex:
                messagebox.showerror("Error",f"Due To:{str(ex)}",parent=self.root)
                
    #=====fetch data=====
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="root", database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()      
        
    # will show data in combo boxes
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        print(data)
        if len(data)>0:
            self.var_std_id.set(data[0]),
            self.var_dep.set(data[1]),
            self.var_course.set(data[2]),
            self.var_year.set(data[3]),
            self.var_semester.set(data [4]),
            self.var_std_name.set(data [5]),
            self.var_div.set(data[6]),
            self.var_roll.set(data[7]),
            self.var_gender.set(data [8]),
            self.var_dob.set(data[9]),
            self.var_email.set(data[10]),
            self.var_phone.set(data[11]),
            self.var_address.set(data[12]),
            self.var_teacher.set(data[13]),
            self.var_radio1.set(data[14])
        
    #update
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","ALL fields are required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update","Do you want to update this student details", parent=self.root)
                if Update>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="root", database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Dep=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s where Student_id=%s",(
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()              
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student Details are succesfully Updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as ex:
                messagebox.showerror("Error",f"Due To:{str(ex)}")
                
    def delete_data(self):
        if self.var_std_id.get()=="":   
            messagebox.showerror("Error","Student ID must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page", "Do you want to delete this student", parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="root", database="face_recognizer")
                    my_cursor = conn.cursor()
                    sql = "delete from student where Student_id=%s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as ex:
                messagebox.showerror("Error",f"Due To:{str(ex)}")

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course") 
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
        

    # genrate dataset
    def genrate_dateset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","ALL fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="root", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                cursor_focus=self.student_table.focus()
                if cursor_focus:
                    content=self.student_table.item(cursor_focus)
                    data=content["values"]
                    
                    id = data[0]
                my_cursor.execute("update student set Dep=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s where Student_id=%s",(
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()==id+1,               
                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                
                #====load predefined data on face frontals from opencv========
                
                
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                
                def face_cropped(img):
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    
                    for (x,y,w,h) in faces:
                        face_cropped = img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap = cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face = cv2.resize(face_cropped(my_frame),(450,450))
                        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Crooped Face", face)
                        
                    if cv2.waitKeyEx(1)==13 or int(img_id)==200:
                        break
                    
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed!!!")
            except Exception as ex:
                messagebox.showerror("Error",f"Due To:{str(ex)}")
    
                
                
if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()

