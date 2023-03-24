from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from time import strftime
from datetime import datetime
import time

class Face_recognition:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face_recognition Details")
        
        title_lbl = Label(self.root, text = "Face Recognition", font=("times new roman",34,'bold'),bg='white', fg ='red')
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        #image1
        image_top = Image.open(r"images\x1.jpeg")
        image_top = image_top.resize((650,700),Image.ANTIALIAS)
        self.photoimage_top = ImageTk.PhotoImage(image_top)

        f_lbl = Label(self.root,image=self.photoimage_top)
        f_lbl.place(x=0,y=55,width=650,height=700)
        
        #image2
        image_bottom = Image.open(r"images\x4.jpg")
        image_bottom = image_bottom.resize((950,700),Image.ANTIALIAS)
        self.photoimage_bottom = ImageTk.PhotoImage(image_bottom)

        f_lbl = Label(self.root,image=self.photoimage_bottom)
        f_lbl.place(x=650,y=55,width=950,height=700)   
        
        #button
        train_button = Button(f_lbl,text="Face Recognition",cursor="hand2", command = self.face_recog ,font = ("times new roman",14,"bold"), bg="sky blue", fg="dark blue")
        train_button.place(x=370,y=620,width=200,height=40)   
        
        
    def mark_attendance(self,i,r,n,d):
        with open("attandance.csv", "r+", newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry = line.split((","))
                name_list.append(entry[0])
                print(name_list)
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and ( d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d}, {dtString}, {d1}, Preset")
    
    
    
    
        
    #face recognition
    
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbour,color,text,clf):
            grey_image = cv2.cvtColor(img,cv2.COLOR_BGRA2GRAY)
            features = classifier.detectMultiScale(grey_image,scaleFactor,minNeighbour)
            
            coord = []
            
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict = clf.predict(grey_image[y:y+h,x:x+w])
                confidence = int((100*(1-predict/100)))
                
                conn = mysql.connector.connect(host="localhost", username="root", password="root", database="face_recognizer")
                my_cursor = conn.cursor()
                
                my_cursor.execute("select Name from student where Student_id="+str(id))
                n = my_cursor.fetchone()
                if n:   
                    n="+".join(n)
                
                my_cursor.execute("select Roll from student where Student_id="+str(id))
                r = my_cursor.fetchone()
                if r:   
                    r="+".join(r)
                
                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d = my_cursor.fetchone()
                if d:   
                    d="+".join(d)
                
                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                i = my_cursor.fetchone()
                if i:   
                    i="+".join(i)
                
                
                
                if confidence>60:
                    cv2.putText(img,f"ID: {i}", (x,y-75),cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                    cv2.putText(img,f"Roll: {r}", (x,y-55),cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                    cv2.putText(img, f"Name: {n}", (x,y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                    cv2.putText(img, f"Department: {d}", (x,y-5),cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                    self.mark_attendance(i,r,n,d)
                    
                else:
                    cv2.rectangle(img,(x,y), (x+w, y+h), (0,0,255), 3)
                    cv2.putText(img, "Unknown Face", (x,y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                
                coord=[x,y,w,y]
                 
            return coord
        
        def recognize(img,clf,faceCascade):
            coord = draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
                    
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        
        video_cap = cv2.VideoCapture(0)
        
        while True:
            ret,img = video_cap.read()
            img = recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognition",img)
            
            if cv2.waitKey(1) ==13:
                messagebox.showinfo("Succes","Attandence Marked Successfully!!")
                break
            
        video_cap.release()
        cv2.destroyAllWindows()      
        
        
        
if __name__ == "__main__":
    root = Tk()
    obj = Face_recognition(root)
    root.mainloop()