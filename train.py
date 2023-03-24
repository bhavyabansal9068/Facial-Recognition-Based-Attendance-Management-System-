from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Train Dataset")
        
       
       
        title_lbl = Label(self.root, text = "Train Dataset", font=("times new roman",34,'bold'),bg='white', fg ='red')
        title_lbl.place(x=0,y=0,width=1530,height=45)

        
        image_top = Image.open(r"images\t11.png")
        image_top = image_top.resize((1530,325),Image.ANTIALIAS)
        self.photoimage_top = ImageTk.PhotoImage(image_top)

        f_lbl = Label(self.root,image=self.photoimage_top)
        f_lbl.place(x=0,y=55,width=1530,height=325)

        image_bottom = Image.open(r"images\t12.webp")
        image_bottom = image_bottom.resize((1530,325),Image.ANTIALIAS)
        self.photoimage_bottom = ImageTk.PhotoImage(image_bottom)

        f_lbl = Label(self.root,image=self.photoimage_bottom)
        f_lbl.place(x=0,y=440,width=1530,height=325)   
        
        train_button = Button(self.root,text="TRAIN DATA",cursor="hand2",command = self.train_classifier,font = ("times new roman",20,"bold"), bg="red", fg="white")
        train_button.place(x=0,y=380,width=1530,height=60)  
        
    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces = []
        ids = []
        
        for image in path:
            img=Image.open(image).convert("L")  # convert greyscale
            imageNp = np.array(img,'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        
        
        # train classifier
        
        clf = cv2.face.LBPHFaceRecognizer_create()
        if len(faces)>0 or len(ids)>0:
            clf.train(faces,ids)
            clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training Datasets Completed!!!")
            
            
if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()